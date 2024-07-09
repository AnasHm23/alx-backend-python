#!/usr/bin/python3

import asyncio

async def my_coroutine():
    print("Hello")
    await asyncio.sleep(2)
    print("World")
    
async def main():
    print("Start")
    await my_coroutine()
    print("end")

asyncio.run(main())