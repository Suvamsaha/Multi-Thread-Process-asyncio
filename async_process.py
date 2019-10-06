import asyncio


async def loopa():
    print("LOOP A", end="  ")
    i = 0
    while True:
        print("LOOP A", i, end="  ")
        i = i + 2
        await asyncio.sleep(2)


async def loopb():
    print("LOOPB", end="  ")
    i = 0
    while True:
        print("LOOP B", i, end="  ")
        i += 3
        await asyncio.sleep(3)


async def loopc():
    print("LOOPC", end="  ")
    i = 0
    while True:
        print("LOOP C", i)
        i += 4
        await asyncio.sleep(4)


async def main():
    await asyncio.gather(loopa(), loopb(), loopc())


if __name__ == '__main__':
    asyncio.run(main())
