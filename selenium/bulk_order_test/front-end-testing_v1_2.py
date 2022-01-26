#!/usr/bin/env python
# coding: utf-8

# In[336]:


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
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
driver = webdriver.Chrome( "./chromedriver/chromedriver", chrome_options=options)

class hekayati_success_scanario:
    global driver
    domain = "https://ksa.hekayati.com/"
    product_url = ""    
    order_status = ""
    
    def get_home(self):
        print("Testing Home Page")
        driver.get(self.domain)
        #elem = driver.find_element_by_id("#hekayati-header")
        #elem = driver.find_element_by_id("#hekayati-footer")
        #elem = driver.find_element_by_css_selector("#hekayati-homepage-product a")
        #product_url = elem.get_attribute('href')        
        self.product_url = [
            "https://ksa.hekayati.com/story/football-star/",
            "https://ksa.hekayati.com/story/the-falcon/",
            "https://ksa.hekayati.com/story/space-mission/"
        ]                
        pass
    
    def get_preview(self):
        print("Testing Preview...")
        driver.get(self.product_url[0])
        
        #--wait for page to load
        try:
            wait_time = 20
            WebDriverWait(driver, wait_time).until(EC.presence_of_element_located( (By.CSS_SELECTOR, "input[name='avatar'] + img") ))            
        except TimeoutException as te:
            print("Preview Page not loading on time", wait_time)
            print("Ert35:", te) 
            
        print("Filling First Name and story details...")
        driver.find_element(By.NAME, "first_name").send_keys("testing")
        driver.find_element(By.NAME, "last_name").send_keys("testing")
        driver.find_element_by_css_selector("input[name='avatar'] + img").click()       
        
        print("Generating Book...")        
        driver.find_element_by_css_selector("button#nextBtn.generatebook").click()
        driver.switch_to.frame(driver.find_element_by_name("frame2"))
        print("Waiting for preview loading...")
        try:
            wait_time  = 20
            WebDriverWait(driver, wait_time).until(EC.presence_of_element_located( (By.CSS_SELECTOR, "div.flipbook") ))
        except TimeoutException as te:
            print("Preview is not working waited for secs:=>", wait_time)
            print("Ert35:", te)    

        driver.switch_to.default_content()

        try:
            wait_time  = 10
            WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable( (By.CSS_SELECTOR, "button#nextBtn.before-add-to-cart") ))
            print("Preview Button is Ready")
        except TimeoutException as te:
            print("Next button After Preview is working=> waited for secs:", wait_time)
            print("Ert35:", te)            
        try:
            time.sleep(1)
            driver.find_element_by_css_selector("button#nextBtn.before-add-to-cart").click()
        except Exception as e:
            print("Error in Preview loading", e)
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable( (By.CSS_SELECTOR, "#acceptcheckbox + label") ))
        #---this will not working only in one time so try to click many times        
        for i in range(0, 30):
            try:
                driver.find_element_by_css_selector("#acceptcheckbox + label").click()
                print("Check box on cover page checked breaking loop")
                break
            except:
                time.sleep(2)
                pass
        if not driver.find_element_by_css_selector("#acceptcheckbox").is_selected():
            time.sleep(5)
            driver.find_element_by_css_selector("#acceptcheckbox + label").click()
            
        time.sleep(5)
        driver.find_element_by_css_selector("button.updatecartform").click()
        print("Pressing Checkout Button...")        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable( (By.CSS_SELECTOR, "a.checkout-button") ))
        driver.find_element_by_css_selector("a.checkout-button").click()
        pass

    def get_palce_order(self):
        
        driver.get( "https://ksa.hekayati.com/checkout/" )
        #WebDriverWait(driver, 10).until(EC.)
        # ### Placing Order

        driver.find_element_by_css_selector("#billing_first_name").clear().send_keys("selenium")

        driver.find_element_by_css_selector("#billing_last_name").clear().send_keys("selenium")

        elem = driver.find_element_by_css_selector("#billing_address_1")
        elem.clear()
        
        elem.send_keys("selenium python nagar, linux states")


        elem = driver.find_element_by_css_selector("input#billing_city")
        elem.clear()
        elem.send_keys("selenium")


        elem = driver.find_element_by_css_selector("input#billing_phone")
        elem.clear()
        elem.send_keys("+933321407846")

        elem = driver.find_element_by_css_selector("input#billing_email")
        elem.clear()
        elem.send_keys("shahwaiz055@gmail.com")

        #---select COD
        driver.find_element_by_css_selector("label[for='payment_method_cod']").click()
        
        time.sleep(10)
        driver.find_element_by_css_selector("#place_order").click()

        if "Thank you. Your order has been received." in driver.page_source:
            print("O.K! Order placed successfully")
            self.order_status = True
        else:
            self.order_status = False


# In[ ]:





# In[337]:


# driver.find_element_by_css_selector("#acceptcheckbox + label").click()


# In[338]:


# try:
#     hss = hekayati_success_scanario()
#     hss.get_home()
#     hss.get_preview()
#     hss.get_palce_order()
# except:
#     #driver.quit()    


# In[339]:


hss = hekayati_success_scanario()


# In[340]:


hss.get_home()


# In[341]:


try:
    hss.get_preview()
except Exception as e:
    print(e)


# In[342]:


driver.get( "https://ksa.hekayati.com/en/checkout/" )
# ### Placing Order

try:
    driver.find_element_by_css_selector("#billing_first_name").send_keys("selenium26JanFirstStress")
except Exception as e:
    print("Cart is Empty:", e)
driver.find_element_by_css_selector("#billing_last_name").send_keys("selenium")

#from selenium.webdriver.support.ui import Select
#select = Select(driver.find_element_by_css_selector('select#billing_country'))
#select.select_by_value("JO")

# for i in range(0, 20):
#     try:
#         driver.execute_script("document.getSelection('select#billing_country').selectedIndex = 1;")
#         break
#     except Exception as e:
#         print("SEelcting country error...")
#         time.sleep(2)

driver.find_element_by_id("select2-billing_country-container").click()
driver.find_element_by_css_selector(".select2-results__option").click()

elem = driver.find_element_by_css_selector("#billing_address_1")
elem.clear()

elem.send_keys("selenium python nagar, linux states")


elem = driver.find_element_by_css_selector("input#billing_city")
elem.clear()
elem.send_keys("selenium")


#driver.find_element_by_css_selector("input#billing_state").send_keys("OMAN")

time.sleep(10)
elem = driver.find_element_by_css_selector("input#billing_phone")
elem.clear()
elem.send_keys("3321407846")

elem = driver.find_element_by_css_selector("input#billing_email")
elem.clear()
elem.send_keys("shahwaiz055@gmail.com")

#---select COD
#--wait to be loaded
#WebDriverWait(driver, 15).until(EC.presence_of_element_located( (By.CSS_SELECTOR, "label[for='payment_method_cod']") ))

for i in range(0, 30):
    try:
        driver.find_element_by_css_selector("label[for='payment_method_cod']").click()
        print ("COD is selected breaking")
        break
    except:
        time.sleep(5)
        pass
    
if not driver.find_element_by_css_selector("#payment_method_cod").is_selected():
    driver.find_element_by_css_selector("label[for='payment_method_cod']").click()

time.sleep(5)
driver.find_element_by_css_selector("#place_order").click()

WebDriverWait(driver, 200).until(EC.url_contains("https://ksa.hekayati.com/en/checkout/order-received"))


# In[ ]:





# In[ ]:





# In[ ]:

#driver.quit()


