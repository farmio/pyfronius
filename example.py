#!/usr/bin/env python
"""Basic usage example and testing of pyfronius."""
import asyncio
import sys

import aiohttp

import pyfronius


async def main(loop, host):
    timeout = aiohttp.ClientTimeout(total=10)
    async with aiohttp.ClientSession(loop=loop, timeout=timeout) as session:
        fronius = pyfronius.Fronius(session, host)

        for info, coro in [
            ("api_version", fronius.fetch_api_version),
            ("inverter_info", fronius.inverter_info),
            ("logger_info", fronius.current_logger_info),
            ("active_device_info", fronius.current_active_device_info),
            ("power_flow", fronius.current_power_flow),
            ("system_inverter", fronius.current_system_inverter_data),
            ("system_meter", fronius.current_system_meter_data),
            ("system_storage", fronius.current_system_storage_data),
        ]:
            print("#####")
            print(info)
            res = await coro()
            print(res)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop, sys.argv[1]))
