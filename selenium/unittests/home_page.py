import unittest

#!/usr/bin/env python
# coding: utf-8

# ### Starting Chrome Driver

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.flipbook img")))

import warnings
warnings.filterwarnings("ignore")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#driver = webdriver.Chrome("./chromedriver/chromedriver")

options = webdriver.ChromeOptions()
options.headless = False
options.add_argument('ignore-certificate-errors')
promot_text = "Claim Your 15% Off Book Now"
home_page_url = "https://new.hekayati.com/"
driver = webdriver.Chrome( "./chromedriver/chromedriver", chrome_options=options)

class home_page_test(unittest.TestCase):
    """This class will handle the test cases for the home page
    we have to try to make a function for each test case so our test cases are atomic,
    means one function only test one think only and second thing is autonomous which
    says, one test cases should be independent not depending on other test cases
    """

    def __init__(self, *args, **kwargs):
        super(home_page_test, self).__init__(*args, **kwargs)
        home_page_url = "https://new.hekayati.com/"
        driver.get(home_page_url)
        import time
        print("Waitng for 4 sec...")
        time.sleep(4)

    def test_home_page_loading(self):
        #url = home_page_url
        #driver.get(url)
        if driver.title == "Hekayati – Your Child, The Star":
            pass
        else:
            self.fail ("Home page not loading properly...")

    def test_check_top_banner(self):
        """Check weather there is top banner or not"""
        try:
            driver.find_element_by_id("hek-promo-ban")
        except:
            self.fail ("Top Banner Missing")

    def test_check_promo_in_top_banner(self):
        promo_banner = driver.find_element_by_id("hek-promo-ban")

        if promot_text in promo_banner.text:
            pass
        else:
            self.fail ("Promo is missing or not match")

    def test_coupon_button_functionality(self):
        try:
            button = driver.find_element_by_css_selector("#hek-promo-ban a")
            button.click()
            pass
        except:
            self.fail ("Coupan Button is not working...")

    def test_search_icon_assertion(self):
        try:
            search_icon = driver.find_element_by_css_selector("span.search_submit")
        except:
            self.fail ("Search icon not available in header")

    def test_hekayati_header_logo(self):
        try:
            driver.find_element_by_css_selector('#hek-logo-id img')
        except:
            self.fail ("Header logo is missing...")

    def test_home_top_cover_title(self):
        try:
            driver.find_element_by_css_selector('#hek-top-cov h2')
        except:
            self.fail ("")

    def test_choose_button_top_cover(self):
        try:
            driver.find_element_by_css_selector('#hek-top-cov a')
        except:
            self.fail ("")

    def test_book_section_home(self):
        ##hek-book-sec img should return 4
        try:
            books_elem = driver.find_elements_by_css_selector("#hek-book-sec img")
            if len(books_elem) > 4:
                self.fail ("More than 4 books are showing on home page...")
        except:
            self.fail ("problem with books section...")

    def test_check_dedication_section(self):
        try:
            driver.find_element_by_id("hek-ded-sec")
        except:
            self.fail ("")

    def test_check_testimonial_section(self):
        # .sc_testimonials_item_content there are total 7 of them.
        try:
            driver.find_element_by_css_selector(".sc_testimonials_item_content")
        except:
            self.fail ("")

    def test_check_feature_section(self):
        try:
            ##hek-fet-sec
            driver.find_element_by_id('hek-fet-sec')
            pass
        except:
            self.fail ("Feature section missing...")

    def test_check_video_section(self):
        try:
            driver.find_element_by_id('hek-vid-sec')
            pass
        except:
            self.fail ("Video section missing...")

    def test_check_footer(self):
        try:
            driver.find_element_by_id('hek-footer')
            pass
        except:
            self.fail ("Video section missing...")

    def test_check_footer_logo(self):
        try:
            driver.find_element_by_css_selector('#hek-footer img')
            pass
        except:
            self.fail ("Video section missing...")
        pass

    def test_check_footer_heading(self):
        try:
            driver.find_element_by_css_selector('#hek-footer h2')
            pass
        except:
            self.fail ("Video section missing...")

    def test_check_footer_icons(self):
        try:
            driver.find_element_by_css_selector('#hek-footer i')            
            pass
        except:
            self.fail ("Video section missing...")
        #driver.quit()

    def tearDown(self):
        pass
        driver.quit()

if __name__ == '__main__':
    unittest.main()
    #driver.quit()