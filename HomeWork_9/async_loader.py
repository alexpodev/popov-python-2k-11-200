import os
import asyncio
from urllib.parse import urlparse, urlunparse

import aiohttp
from bs4 import BeautifulSoup

from url_normalaizer import normalize_image_url


def normalize_image_url(image_url, current_domain):
    parsed_url = urlparse(image_url)

    if not parsed_url.scheme:
        parsed_url = parsed_url._replace(scheme='http')

    if not parsed_url.netloc:
        parsed_url = parsed_url._replace(netloc=current_domain)

    return urlunparse(parsed_url)


async def download_image(session, image_url, save_path):
    try:
        async with session.get(image_url) as response:
            if response.status == 200:
                image_data = await response.read()
                with open(save_path, 'wb') as f:
                    f.write(image_data)
    except Exception as e:
        print(f"Ошибка при скачивании изображения {image_url}: {str(e)}")


async def download_images_from_page(page_url, save_folder):
    async with aiohttp.ClientSession() as session:
        async with session.get(page_url) as response:
            if response.status == 200:
                soup = BeautifulSoup(await response.text(), 'html.parser')
                current_domain = urlparse(page_url).scheme + "://" + urlparse(page_url).netloc

                img_tags = soup.find_all('img')
                tasks = []

                for img_tag in img_tags:
                    img_url = img_tag.get('src')
                    if img_url:
                        img_url = normalize_image_url(img_url, current_domain)
                        img_filename = os.path.basename(urlparse(img_url).path)
                        save_path = os.path.join(save_folder, img_filename)

                        task = download_image(session, img_url, save_path)
                        tasks.append(task)

                await asyncio.gather(*tasks)


async def main():
    page_url = input("Введите адрес страницы: ")
    save_folder = input("Введите папку для сохранения изображений: ")

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    await download_images_from_page(page_url, save_folder)

if __name__ == '__main__':
    asyncio.run(main())
