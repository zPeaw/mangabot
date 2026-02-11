import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import config


def get_new_items():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get(config.URL)
    time.sleep(6)

    results = []
    tags = driver.find_elements(By.CLASS_NAME, "c-new-tag")

    for tag in tags:
        href = tag.get_attribute("href")
        title = tag.get_attribute("title")

        if not href:
            continue

        slug = href.split("/comic/")[-1].strip("/")
        manga_name = slug.replace("-", " ").title()

        if title:
            results.append(f"📘 {manga_name}\n⏱ {title}\n{href}")
        else:
            results.append(f"📘 {manga_name}\n{href}")

    driver.quit()
    return results
