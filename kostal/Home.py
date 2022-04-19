#!/usr/bin/env python3
from kostal.DxsApi import DxsEntry


class Home:
    DC_POWER_PV = 33556736
    AC_POWER = 67109120
    OWN_CONSUMPTION = 83888128
    BATTERY_STATE_OF_CHARGE = 33556229
    OPERATING_STATUS = 16780032
    # TODO: statusCodes

    def __init__(self, inverter) -> None:
        self.__inverter = inverter

    async def home_dc_power_pv(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.DC_POWER_PV)) \
            .get_entry_by_id(self.DC_POWER_PV)

    async def home_ac_power(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.AC_POWER)) \
            .get_entry_by_id(self.AC_POWER)

    async def home_own_consumption(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.OWN_CONSUMPTION)) \
            .get_entry_by_id(self.OWN_CONSUMPTION)

    async def home_battery_state_of_charge(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.BATTERY_STATE_OF_CHARGE)) \
            .get_entry_by_id(self.BATTERY_STATE_OF_CHARGE)

    async def inverter_operating_status(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.OPERATING_STATUS)) \
            .get_entry_by_id(self.OPERATING_STATUS)
