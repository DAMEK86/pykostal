#!/usr/bin/env python
"""Basic usage example and testing of kostal."""
import asyncio
import logging
import aiohttp

import kostal
from kostal import ActualBattery


async def main(loop, host):
    async with aiohttp.ClientSession(loop=loop) as session:
        inverter = kostal.Piko(session, host)

        # Fetch single values
        res = await inverter.statisticDay.day_yield()
        print(f'day yield: {res.value}')

        # Or multiple values at once
        res = await inverter.fetch_props(ActualBattery.CHARGE, ActualBattery.TEMPERATURE)
        battery_charge = res.get_entry_by_id(ActualBattery.CHARGE).value
        battery_temp = res.get_entry_by_id(ActualBattery.TEMPERATURE).value
        print(f'battery charge {battery_charge}, temperature {battery_temp}')


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop, 'http://192.168.0.xyz'))
