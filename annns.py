import aiohttp
import asyncio
import time

urls = ["https://ru.wikipedia.org/wiki/%D0%92%D0%B8%D0%BA%D0%B8"] * 100


async def fetch(session, url):
    async with session.get(url) as response:
        text = await response.text()
        print(len(text))


async def load_urls_async():
    async with aiohttp.ClientSession() as session:
        tasks = []

        for url in urls:
            tasks.append(fetch(session, url))

        await asyncio.gather(*tasks)


start = time.time()

asyncio.run(load_urls_async())

end = time.time()

print("Асинхронное время:", end - start)