# Sometime you want to cancel some tasks or stop running task.
# For this we use cancel() keyword

import asyncio

async def worker():
    print("Worker: I started working...")
    await asyncio.sleep(5)
    print("Worker: I finished!") # This will never run

async def main():
    # 1. Start the task
    task = asyncio.create_task(worker())
    
    # Give the worker a split second to actually start and hit its sleep line
    await asyncio.sleep(0.1) 
    
    # 2. Cancel the task
    print("Main: Cancelling the worker now...")
    task.cancel()
    await asyncio.sleep(0.1)

    
    if task.cancelled():
        print("Main: The task was successfully cancelled without crashing!")

asyncio.run(main())