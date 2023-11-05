import os
from multiprocessing import Pool
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

from url_normalaizer import normalize_image_url


def download_image(image_url, save_path):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
    except Exception as e:
        print(f"Ошибка при скачивании изображения {image_url}: {str(e)}")


def download_images_from_page(page_url, save_folder):
    response = requests.get(page_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        current_domain = urlparse(page_url).scheme + "://" + urlparse(page_url).netloc

        img_tags = soup.find_all('img')
        links = []

        for img_tag in img_tags:
            img_url = img_tag.get('src')
            if img_url:
                img_url = normalize_image_url(img_url, current_domain)
                img_filename = os.path.basename(urlparse(img_url).path)
                save_path = os.path.join(save_folder, img_filename)
                links.append((img_url, save_path))

        with Pool() as pool:
            pool.starmap(download_image, links)


def main():
    page_url = input("Введите адрес страницы: ")
    save_folder = input("Введите папку для сохранения изображений: ")

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    download_images_from_page(page_url, save_folder)


if __name__ == '__main__':
    main()
