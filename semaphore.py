# A Semaphore is very similar to a Lock, but with one major difference: while a Lock only allows one task to access a resource at a time, a Semaphore allows a specific, limited number of tasks to access a resource simultaneously.

import asyncio

# Create a Semaphore that allows a maximum of 2 tasks at once
semaphore = asyncio.Semaphore(2)

async def download_file(worker_id):
    print(f"Worker {worker_id} is waiting in line...")
    
    # Acquire a spot in the semaphore
    async with semaphore:
        print(f"[ACTIVE] Worker {worker_id} started downloading.")
        
        # Simulate downloading a file (takes 2 seconds)
        await asyncio.sleep(2)
        
        print(f"[FINISHED] Worker {worker_id} is done and left.")
    # The spot is automatically released when exiting the 'async with' block

async def main():
    # Run 5 workers concurrently
    await asyncio.gather(
        download_file(1),
        download_file(2),
        download_file(3),
        download_file(4),
        download_file(5)
    )

asyncio.run(main())