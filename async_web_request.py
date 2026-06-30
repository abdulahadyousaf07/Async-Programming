# [ Client ]  --- (Request: "Give me this page") --->  [ Server ]
# [ Client ]  <--- (Response: "Here is your data") ---  [ Server ]

import aiohttp
import asyncio

# 1. Fetch function now accepts the shared session
async def fetch(session, url):
    try:
        async with session.get(url) as response:
            # Returns the HTML or text content of the page
            return await response.text()
    except Exception as e:
        return f"Error fetching {url}: {e}"

# 2. Main coordinator function
async def main():
    # Dummy URLs for demonstration
    url1 = "https://httpbin.org/delay/1"
    url2 = "https://httpbin.org/delay/2"
    url3 = "https://httpbin.org/delay/1"
    
    # Create ONE session to handle all requests efficiently
    async with aiohttp.ClientSession() as session:
        # Schedule all fetch tasks to run concurrently
        results = await asyncio.gather(
            fetch(session, url1),
            fetch(session, url2),
            fetch(session, url3)
        )
        
        # Print a snippet of the results to verify
        for i, html in enumerate(results, start=1):
            print(f"URL {i} fetched successfully! (Length: {len(html)} characters)")

# 3. Code execution entry point
if __name__ == "__main__":
    asyncio.run(main())