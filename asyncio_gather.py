# It is python library function used to run multiple asynchronous operations concurrently and collect their results as lists.
# In return list order is match with order of function.

import asyncio

async def task1():
    print("Task 1 started...")
    await asyncio.sleep(3)
    print("Task 1 finished!")

async def task2():
    print("Task 2 started...")
    await asyncio.sleep(3)
    print("Task 2 finished!")

async def main():
    print("--- Starting Gather ---")
    await asyncio.gather(
        task1(),
        task2()
    )
    
    print("--- Gather Finished ---")
    
asyncio.run(main())