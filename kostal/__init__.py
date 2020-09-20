#!/usr/bin/env python3

from typing import List

import aiohttp
import async_timeout
import asyncio
import json

from kostal import const

import logging

LOG = logging.getLogger(__name__)

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
        print(self.status.code)

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
        auth=aiohttp.BasicAuth(self.__username, self.__password)
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

    async def __fetch_dxs_entry(self, entry_id: []):
        r = await self.__fetch_data({'dxsEntries': entry_id})
        return DxsResponse(**r).get_entry_by_id(entry_id)

    async def day_yield(self):
        entry = await self.__fetch_dxs_entry(const.StatisticDay['Yield'])
        return entry.value
