#!/usr/bin/env python3
from typing import List
import json


class DxsEntry:
    def __init__(self, dxsId, value):
        super().__init__()
        self.dxsId = dxsId
        self.value = value

    @classmethod
    def from_json(cls, data):
        return cls(**data)


class DxsSessionData:
    def __init__(self, sessionId, roleId):
        super().__init__()
        self.session_id = sessionId
        self.role_id = roleId

    @classmethod
    def from_json(cls, data):
        return cls(**data)


class DxsStatus:
    def __init__(self, code):
        super().__init__()
        self.code = code

    @classmethod
    def from_json(cls, data):
        return cls(**data)


class DxsResponse:
    __dxs_entries: List[DxsEntry]
    session: DxsSessionData
    status: DxsStatus

    def __init__(self, dxsEntries, session, status):
        super().__init__()
        self.__dxs_entries = list(map(DxsEntry.from_json, dxsEntries))
        self.__session = DxsSessionData.from_json(session)
        self.status = DxsStatus.from_json(status)

    def get_entry_by_id(self, dxs_id: int):
        for i in self.__dxs_entries:
            if i.dxsId == dxs_id:
                return i
        return None

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)
