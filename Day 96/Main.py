import asyncio
import aiohttp

# Define a coroutine function to fetch data from a URL using aiohttp
async def fetch_data(url):
    # Create a ClientSession to make HTTP requests
    async with aiohttp.ClientSession() as session:
        # Make an HTTP GET request to the given URL
        async with session.get(url) as response:
            # Read the response data as text and return it
            data = await response.text()
            return data

# Define a coroutine function to fetch data from multiple URLs in parallel
async def main():
    # Create a list of URLs to fetch
    urls = [
        "https://https://github.com/adarshooo1",
        "https://replit.com/@adarshooo1",
        "https://chat.openai.com",
    ]
    # Create an asyncio.Task for each URL and store them in a list
    tasks = [asyncio.create_task(fetch_data(url)) for url in urls]
    # Wait for all the tasks to complete and collect the results
    results = await asyncio.gather(*tasks)
    # Print the results
    print(results)

# Run the main coroutine using asyncio.run
if __name__ == "__main__":
    asyncio.run(main())
