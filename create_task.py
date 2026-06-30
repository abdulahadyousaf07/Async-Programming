# Its is used to schedule a coroutine  to run concurrently in the background as asoon as possible
# When we create a task in program then it go to the function that is give in create_task() the if it see the await in that function then it ask it to wait in the background and execute the next statement in main and after the await timeperiod the task is executed automatically and move on.

import asyncio

async def worker():
    await asyncio.sleep(2)
    print("Done")

async def main():
    task = asyncio.create_task(worker())

    print("Doing other work...")
    await task

asyncio.run(main())