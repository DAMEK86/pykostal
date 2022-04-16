#!/usr/bin/env python3

from typing import List

import aiohttp
import async_timeout
import asyncio
import json

from kostal.const import *

DXS_ENDPOINT = "/api/dxs.json"
LOG_DATA_ENDPOINT = "/LogDaten.dat"

DEFAULT_USERNAME = 'pvserver'
DEFAULT_PASSWORD = 'pvwr'


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


class Piko:
    """ 
    Interface to communicate with the Kostal Piko over http request
    Attributes:
        session     The AIO session
        url         the url for reaching of the inverter
                    (i.e. http://192.168.0.123)
        username    inverter username (default pvserver)
        password    inverter password (default pvwr)
        timeout     HTTP timeout in seconds
     """

    def __init__(self, session: aiohttp.ClientSession, url: str = None, username: str = DEFAULT_USERNAME,
                 password: str = DEFAULT_PASSWORD,
                 timeout: int = 10):
        """ Constructor """
        if url is None:
            raise ValueError("Parameter url can not be None")

        self.__client = session
        self.__url = url + DXS_ENDPOINT
        self.__username = username
        self.__password = password
        self.__timeout = timeout

    async def __fetch_data(self, request_params):
        """ fetch data """
        auth = aiohttp.BasicAuth(self.__username, self.__password)
        try:
            async with async_timeout.timeout(self.__timeout):
                async with self.__client.get(self.__url,
                                             params=request_params,
                                             auth=auth,
                                             timeout=self.__timeout) as resp:
                    assert resp.status == 200
                    return await resp.json(content_type='text/plain')
        except (asyncio.TimeoutError, aiohttp.ClientError):
            raise ConnectionError(
                "Connection to Kostal device failed at {}.".format(self.__url))
        except json.JSONDecodeError:
            raise ValueError(
                "Device returned a non-JSON reply at {}.".format(self.__url))

    async def fetch_props(self, *prop_ids):
        response = await self.__fetch_data({'dxsEntries': prop_ids})
        return DxsResponse(**response)

    async def analog_1(self) -> DxsEntry:
        return (await self.fetch_props(ActualAnalogInputs.ANALOG1)) \
            .get_entry_by_id(ActualAnalogInputs.ANALOG1)

    async def analog_2(self) -> DxsEntry:
        return (await self.fetch_props(ActualAnalogInputs.ANALOG2)) \
            .get_entry_by_id(ActualAnalogInputs.ANALOG2)

    async def analog_3(self) -> DxsEntry:
        return (await self.fetch_props(ActualAnalogInputs.ANALOG3)) \
            .get_entry_by_id(ActualAnalogInputs.ANALOG3)

    async def analog_4(self) -> DxsEntry:
        return (await self.fetch_props(ActualAnalogInputs.ANALOG4)) \
            .get_entry_by_id(ActualAnalogInputs.ANALOG4)

    async def battery_voltage(self) -> DxsEntry:
        return (await self.fetch_props(ActualBattery.VOLTAGE)) \
            .get_entry_by_id(ActualBattery.VOLTAGE)

    async def battery_charge(self) -> DxsEntry:
        return (await self.fetch_props(ActualBattery.CHARGE)) \
            .get_entry_by_id(ActualBattery.CHARGE)

    async def battery_current(self) -> DxsEntry:
        return (await self.fetch_props(ActualBattery.CURRENT)) \
            .get_entry_by_id(ActualBattery.CURRENT)

    async def battery_current_dir(self) -> DxsEntry:
        return (await self.fetch_props(ActualBattery.CURRENT_DIR)) \
            .get_entry_by_id(ActualBattery.CURRENT_DIR)

    async def battery_charge_cycles(self) -> DxsEntry:
        return (await self.fetch_props(ActualBattery.CHARGE_CYCLES)) \
            .get_entry_by_id(ActualBattery.CHARGE_CYCLES)

    async def battery_temp(self) -> DxsEntry:
        return (await self.fetch_props(ActualBattery.TEMPERATURE)) \
            .get_entry_by_id(ActualBattery.TEMPERATURE)

    async def grid_output_power(self) -> DxsEntry:
        return (await self.fetch_props(ActualGrid.GRID_OUTPUT_POWER)) \
            .get_entry_by_id(ActualGrid.GRID_OUTPUT_POWER)

    async def grid_frequency(self) -> DxsEntry:
        return (await self.fetch_props(ActualGrid.GRID_FREQ)) \
            .get_entry_by_id(ActualGrid.GRID_FREQ)

    async def grid_cos_phi(self) -> DxsEntry:
        return (await self.fetch_props(ActualGrid.GRID_COS_PHI)) \
            .get_entry_by_id(ActualGrid.GRID_COS_PHI)

    async def grid_limitation(self) -> DxsEntry:
        return (await self.fetch_props(ActualGrid.GRID_LIMITATION)) \
            .get_entry_by_id(ActualGrid.GRID_LIMITATION)

    async def grid_voltage_l1(self) -> DxsEntry:
        return (await self.fetch_props(ActualGrid.GRID_VOLTAGE_L1)) \
            .get_entry_by_id(ActualGrid.GRID_VOLTAGE_L1)

    async def grid_current_l1(self) -> DxsEntry:
        return (await self.fetch_props(ActualGrid.GRID_CURRENT_L1)) \
            .get_entry_by_id(ActualGrid.GRID_CURRENT_L1)

    async def grid_power_l1(self) -> DxsEntry:
        return (await self.fetch_props(ActualGrid.GRID_POWER_L1)) \
            .get_entry_by_id(ActualGrid.GRID_POWER_L1)

    async def grid_voltage_l2(self) -> DxsEntry:
        return (await self.fetch_props(ActualGrid.GRID_VOLTAGE_L2)) \
            .get_entry_by_id(ActualGrid.GRID_VOLTAGE_L2)

    async def grid_current_l2(self) -> DxsEntry:
        return (await self.fetch_props(ActualGrid.GRID_CURRENT_L2)) \
            .get_entry_by_id(ActualGrid.GRID_CURRENT_L2)

    async def grid_power_l2(self) -> DxsEntry:
        return (await self.fetch_props(ActualGrid.GRID_POWER_L2)) \
            .get_entry_by_id(ActualGrid.GRID_POWER_L2)

    async def grid_voltage_l3(self) -> DxsEntry:
        return (await self.fetch_props(ActualGrid.GRID_VOLTAGE_L3)) \
            .get_entry_by_id(ActualGrid.GRID_VOLTAGE_L3)

    async def grid_current_l3(self) -> DxsEntry:
        return (await self.fetch_props(ActualGrid.GRID_CURRENT_L3)) \
            .get_entry_by_id(ActualGrid.GRID_CURRENT_L3)

    async def grid_power_l3(self) -> DxsEntry:
        return (await self.fetch_props(ActualGrid.GRID_POWER_L3)) \
            .get_entry_by_id(ActualGrid.GRID_POWER_L3)

    async def day_yield(self) -> DxsEntry:
        return (await self.fetch_props(StatisticDay.YIELD)) \
            .get_entry_by_id(StatisticDay.YIELD)
