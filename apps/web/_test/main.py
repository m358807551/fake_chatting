import asyncio
from pyppeteer import launch


async def main():
    browser = await launch({'headless': False})
    page = await browser.newPage()
    await page.goto('http://127.0.0.1:5000')
    main_div = await page.querySelector('#main')
    quality = 100
    await page.screenshot({'path': 'example{}.jpeg'.format(quality), 'type': 'jpeg', 'quality': quality, 'fullPage': True})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
