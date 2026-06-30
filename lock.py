# An asyncio.Lock is used to make sure that only one task can access a specific piece of code or resource at a time. It protect the task so that they cannot overwrite each other's work

import asyncio

# A shared variable that tasks will modify
shared_counter = 0

# 1. Create the Lock
lock = asyncio.Lock()

async def worker(worker_id):
    global shared_counter
    
    print(f"Worker {worker_id} is waiting for the lock...")
    
    # 2. Acquire the lock (Only ONE worker can enter this 'with' block at a time)
    async with lock:
        print(f" Worker {worker_id} secured the lock!")
        
        # Simulate doing some work inside the critical section
        current_value = shared_counter
        await asyncio.sleep(1) 
        shared_counter = current_value + 1
        
        print(f" Worker {worker_id} updated counter to {shared_counter} and released lock.")

async def main():
    # Run 3 workers concurrently
    await asyncio.gather(
        worker(1),
        worker(2),
        worker(3)
    )

asyncio.run(main())