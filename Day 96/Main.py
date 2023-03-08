# We have made a asyncronous function.
import asyncio

import aiohttp
import time

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

# Example 2

# This is function 1 which will take 2 second then print,
def function1():
    time.sleep(2)
    print("func 1")

# This is function 2 which will take 2 second then print,
def function2():
    time.sleep(2)
    print("func 2")

# This is function 3 which will take 2 second then print,
def function3():
    time.sleep(2)
    print("func 3")  

#This will print the functions
function1()
function2()
function3()     

# Over summary of this Example 2 isfunction 1 is taking time after that function 2 and then function 3, seperately but after one another, why is can't be possible like at the same time function 2 and function 3 also start running at the same time when we run the program. in this case asyncronous function hlep us in python.

# Example 3:


# Define three async functions that each print a message after a delay
async def funX():
    await asyncio.sleep(5)
    print("This is function X")
    return "Adarsh"

async def funY():
    await asyncio.sleep(5)
    print("This is function Y")
    return 5

async def funZ():
    await asyncio.sleep(5)
    print("This is function Z")
    # as Default return none.

# Define the main async function that runs the three other functions concurrently
async def main():
    # Use asyncio.gather to run the three functions concurrently and wait for them to finish
    # The results of each function (which are None) are returned in a list
    results = await asyncio.gather(
        funX(),
        funY(),
        funZ()
    )
    # Print the results (which are [None, None, None])
    print(f"Results: {results}")

# Run the main function using asyncio.run
asyncio.run(main())

# Summary of example 3 that it will not extra time to run a command like previous=> sleep(2),Sleep(3),sleep(4) total time take by the program to run in 9 Seconds.
# but asyncio.gather will run all the command together and make it run the same program with in 4 seconds. in this case asyncio helps.