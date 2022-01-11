import unittest

# !/usr/bin/env python
# coding: utf-8

# ### Starting Chrome Driver

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.flipbook img")))

import warnings

warnings.filterwarnings("ignore")

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
import time

# driver = webdriver.Chrome("./chromedriver/chromedriver")

options = webdriver.ChromeOptions()
options.headless = False
options.add_argument('ignore-certificate-errors')
driver = webdriver.Chrome("./chromedriver/chromedriver", chrome_options=options)
product_page_url = "https://new.hekayati.com/en/product/what-will-you-be/"
driver.get(product_page_url)
import time
print("Waitng for 4 sec...")
time.sleep(4)

def get_product_url():
    import random
    urls = [
        "https://new.hekayati.com/en/product/falcon/",
        "https://new.hekayati.com/product/the-magic-of-al-ain-fc/",
        "https://new.hekayati.com/en/product/on-a-space-mission/",
        "https://new.hekayati.com/product/what-will-you-be/",
        "https://new.hekayati.com/product/the-ocean-keeper/",
        "https://new.hekayati.com/product/the-football-star/",
        "https://new.hekayati.com/en/product/the-football-star/"
    ]
    url = random.choice(urls)
    print("Going for:", url)
    return url

class ProductPage(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(ProductPage, self).__init__(*args, **kwargs)

    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_book_title(self):
        try:
            driver.get(get_product_url())
            driver.find_element(By.CSS_SELECTOR, "#hek-bk-dtls h3")
        except:
            self.fail("Book Title is Missing")
        pass

    def test_book_description(self):
        try:
            driver.get(get_product_url())
            driver.find_element(By.ID, "hek-bk-desc")
        except:
            self.fail("Book Description is Missing")
        pass

    def test_vat_tax(self):
        try:
            driver.get(get_product_url())
            no_of_elements = len(driver.find_elements(By.ID, "#hek-tax-dlvry"))
            if no_of_elements < 2:
                self.fail("VAT OR DELIVERY SECTION IS MISSING")
        except:
            self.fail("Book VAT and Delivery Info section is Missing")
        pass

    def test_child_age_and_category(self):
        try:
            driver.get(get_product_url())
            driver.find_element(By.ID, "hek-bk-age")
        except:
            self.fail("Book Child Age or Category is Missing.")
        pass

    def test_create_book_button(self):
        try:
            driver.get(get_product_url())
            driver.find_element(By.CSS_SELECTOR, "#hek-bk-dtls .elementor-button-text")
        except:
            self.fail("Book Create Book Button is Missing")
        pass

    def test_book_gallery(self):
        try:
            driver.get(get_product_url())
            driver.find_element(By.ID, "hek-bk-glry")
        except:
            self.fail("Book Gallery is Missing")
        pass

    def test_steps_navigation_bar(self):
        try:
            driver.get(get_product_url())
            driver.find_element(By.CSS_SELECTOR, "div.stepnav")
        except:
            self.fail("Book Steps Navigation Bar is Missing")
        pass

    def test_preview_form(self):
        try:
            driver.get(get_product_url())
            driver.find_element(By.NAME, "language")
            driver.find_element(By.NAME, "gender")
            driver.find_element(By.NAME, "first_name")
            driver.find_element(By.NAME, "last_name")
            driver.find_element(By.NAME, "avatar")
        except Exception as e:
            self.fail("Book Form Issue, These Fields is Missing:" + str(e))

        pass

    def test_generate_preview(self):
        def test_steps_navigation_bar(self):
            try:
                driver.get(get_product_url())
                driver.find_element(By.CSS_SELECTOR, ".generatebook")
            except:
                self.fail("Book Generate Preview is Missing.")
            pass

    def tearDown(self):
        #driver.quit()
        pass


if __name__ == '__main__':
    unittest.main()
