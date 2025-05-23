import aiohttp
import asyncio

urls = [
    "https://www.daraz.pk",
    "https://www.alibaba.com",
    "https://www.facebook.com/",
    "https://www.youtube.com/",
    "https://colab.google/"
]

async def fetch_async(session, url):
    async with session.get(url) as response:
        content = await response.text() 
        print(content) 
        print(f"Fetched from: {url}")

async def main():
    async with aiohttp.ClientSession() as session:
        list_of_url = [fetch_async(session, url) for url in urls]
        await asyncio.gather(*list_of_url)

asyncio.run(main())
