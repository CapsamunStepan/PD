import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import requests
from urllib.parse import urlparse, urljoin, quote
from tqdm import tqdm

base_dir = "dataset"
os.makedirs(base_dir, exist_ok=True)


def download_images(query, num_images):
    query_encoded = quote(query)
    search_url = f"https://yandex.ru/images/search?text={query_encoded}"

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # не отображать хром
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(search_url)
    time.sleep(5)

    image_links = []

    while len(image_links) < num_images:
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        for img in soup.find_all("img"):
            src = img.get("src")
            if src:
                image_links.append(src)
    driver.quit()

    category_dir = os.path.join(base_dir, query)
    os.makedirs(category_dir, exist_ok=True)

    count = 0
    for img_link in image_links[:num_images]:
        try:
            if not urlparse(img_link).scheme:
                img_link = urljoin(search_url, img_link)

            img_data = requests.get(img_link, stream=True)
            img_size = int(img_data.headers.get("Content-length", 0))
            img_filename = f"{count + 1}.jpg"
            img_path = os.path.join(category_dir, img_filename)
            progress = tqdm(img_data.iter_content(1024),
                            f'Загрузка {img_filename}',
                            total=img_size,
                            unit="B",
                            unit_scale=True,
                            unit_divisor=1024)
            with open(img_path, "wb") as img_file:
                for data in progress.iterable:
                    img_file.write(data)
                    progress.update(len(data))

            count += 1
        except Exception as e:
            print(f"Ошибка при загрузке изображения: {e}")


num = 50
download_images("cat", num)
print(f"Загружено {num} изображений категории {'cat'}")
download_images("dog", num)
print(f"Загружено {num} изображений категории {'dog'}")
