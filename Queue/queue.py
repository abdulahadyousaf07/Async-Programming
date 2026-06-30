import asyncio

async def main():
    # 1. Create a queue
    queue = asyncio.Queue()

    # 2. Put items into the queue
    print("Putting items in the queue...")
    await queue.put("Apple")
    await queue.put("Banana")

    # 3. Get items out of the queue (First In, First Out)
    item1 = await queue.get()
    print(f"Got: {item1}")

    item2 = await queue.get()
    print(f"Got: {item2}")

asyncio.run(main())