#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional

from kostal.DxsApi import DxsEntry


@dataclass(frozen=True)
class Event:
    timestamp: int
    date: datetime
    code: int
    env: str
    raw: tuple[int, ...]


class InfoEvents:
    EVENT_COUNT = 234881792
    FIRST_EVENT = 234881537
    MAX_EVENTS = 10
    EVENT_IDS = tuple(range(FIRST_EVENT, FIRST_EVENT + MAX_EVENTS))

    def __init__(self, inverter) -> None:
        self.__inverter = inverter

    async def events(self) -> list[Event]:
        response = await self.__inverter.fetch_props(self.EVENT_COUNT, *self.EVENT_IDS)
        count_entry = response.get_entry_by_id(self.EVENT_COUNT)
        count = self.__event_count(count_entry)

        events = []
        for dxs_id in self.EVENT_IDS[:count]:
            entry = response.get_entry_by_id(dxs_id)
            event = self.parse_event(entry.value if entry is not None else None)
            if event is not None:
                events.append(event)

        return events

    @staticmethod
    def parse_event(value: list[int] | None) -> Optional[Event]:
        if value is None or len(value) != 8 or all(part == 0 for part in value):
            return None

        timestamp = (
            (value[0] << 0)
            + (value[1] << 8)
            + (value[2] << 16)
            + (value[3] << 24)
        )
        code = (value[4] << 0) + (value[5] << 8)
        env = f"{((value[6] << 0) + (value[7] << 8)):04X}h"

        return Event(
            timestamp=timestamp,
            date=datetime.fromtimestamp(timestamp, tz=timezone.utc),
            code=code,
            env=env,
            raw=tuple(value),
        )

    @staticmethod
    def __event_count(entry: DxsEntry | None) -> int:
        if entry is None:
            return 0
        return max(0, min(int(entry.value), InfoEvents.MAX_EVENTS))
