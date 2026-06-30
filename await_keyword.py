import asyncio

async def hello():
    print("Hello")
    await asyncio.sleep(2)   # Wait for 2 seconds
    print("World")
asyncio.run(hello()) 

# The above program run and print Hello and then wait 2 seconds and then print World because of await
