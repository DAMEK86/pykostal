#!/usr/bin/env python3
import aiohttp
import async_timeout
import asyncio
import json
import hashlib
import base64

from kostal.DxsApi import DxsResponse
from kostal.ActualAnalogInputs import ActualAnalogInputs
from kostal.ActualBattery import ActualBattery
from kostal.ActualGrid import ActualGrid
from kostal.ActualHome import ActualHome
from kostal.ActualGenerator import ActualGenerator
from kostal.ActualGrid import ActualGrid
from kostal.ActualHome import ActualHome
from kostal.ActualSZeroIn import ActualSZeroIn
from kostal.Home import Home
from kostal.InfoVersions import InfoVersions
from kostal.SettingsGeneral import SettingsGeneral
from kostal.StatisticDay import StatisticDay
from kostal.StatisticTotal import StatisticTotal

DXS_ENDPOINT = "/api/dxs.json"
LOGIN_ENDPOINT = "/api/login.json"
LOG_DATA_ENDPOINT = "/LogDaten.dat"

DEFAULT_USERNAME = 'pvserver'
DEFAULT_PASSWORD = 'pvwr'


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
        self.__login_needed = True
        self.__session_id = None
        self.__url_login = url + LOGIN_ENDPOINT

        self.actualAnalogInputs = ActualAnalogInputs(self)
        self.actualBattery = ActualBattery(self)
        self.actualGenerator = ActualGenerator(self)
        self.actualGrid = ActualGrid(self)
        self.actualHome = ActualHome(self)
        self.actualSZeroIn = ActualSZeroIn(self)
        self.home = Home(self)
        self.infoVersions = InfoVersions(self)
        self.settingsGeneral = SettingsGeneral(self)
        self.statisticDay = StatisticDay(self)
        self.statisticTotal = StatisticTotal(self)

    async def __fetch_data(self, request_params):
        """ fetch data """
        if self.__login_needed or self.__session_id is None:
            await self.login()
        if self.__session_id is not None:
            request_params['sessionId'] = self.__session_id
        try:
            async with async_timeout.timeout(self.__timeout):
                async with self.__client.get(self.__url,
                                             params=request_params,
                                             timeout=self.__timeout) as resp:
                    assert resp.status == 200
                    dataset = await resp.json(content_type='text/plain')
                    if dataset.get('session', {}).get('roleId',0) == 0:
                        self.__login_needed = True
                        Warning("Session expired, re-login needed.")
                    return dataset
        except (asyncio.TimeoutError, aiohttp.ClientError):
            raise ConnectionError(
                "Connection to Kostal device failed at {}.".format(self.__url))
        except json.JSONDecodeError:
            raise ValueError(
                "Device returned a non-JSON reply at {}.".format(self.__url))

    async def fetch_props(self, *prop_ids):
        response = await self.__fetch_data({'dxsEntries': prop_ids})
        return DxsResponse(**response)

    async def login(self):
        """ Login to the Kostal Piko inverter """
        self.__session_id = None
        try:
            async with async_timeout.timeout(self.__timeout):
                async with self.__client.get(self.__url_login) as resp:
                    if resp.status == 200:
                        data = await resp.json(content_type=None)
                        session_id = data.get('session', {}).get('sessionId',0)
                        salt = data.get('salt')
                combined = self.__password + salt  # Reihenfolge wie im JS
                hash_value = hashlib.sha1(combined.encode("utf-8")).digest()
                pwh = base64.b64encode(hash_value).decode()
                data = {
                    'mode': 1,
                    'userId': self.__username,
                    'pwh': pwh
                }
                async with self.__client.post(f"{self.__url_login}?sessionId={session_id}",
                                              json=data) as resp:
                    if resp.status == 200:
                        data = await resp.json(content_type=None)
                        if data.get('session', {}).get('roleId', 0) > 0:
                            self.__login_needed = False
                            self.__session_id = data.get('session', {}).get('sessionId', None)
                            return True
                        else:
                            raise Warning("Login failed, invalid credentials.")
                    else:
                        raise Warning(
                            "Login request failed with status {}".format(resp.status))

        except (asyncio.TimeoutError, aiohttp.ClientError):
            raise ConnectionError(
                "Connection to Kostal device failed at {}.".format(self.__url))
        except json.JSONDecodeError:
            raise ValueError(
                "Device returned a non-JSON reply at {}.".format(self.__url))
