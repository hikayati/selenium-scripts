#!/usr/bin/env python
# coding: utf-8

# In[60]:


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
driver = webdriver.Chrome( "./chromedriver/chromedriver", chrome_options=options)


# In[61]:

def load_preview(url):
    global driver
    print("[Preview] Going for:", url)
    driver.get( url )    

    print("Waiting for preview loading....")

    start_sleep = 5
    max_sleep = 300
    sleep_for = 2
    while start_sleep < max_sleep:
        print("Waiting for:", sleep_for)
        time.sleep( sleep_for )
        try:
            driver.find_element_by_css_selector(".magazine.animated")
            print("PReview is Ready....")
            break
        except:
            start_sleep += sleep_for
            print("PReview is not ready waiting")
            continue
    print("Time Taken by Preview to load is:", start_sleep)
    if start_sleep >= 300:
        return False
    return True, start_sleep
    #driver.switch_to.default_content()    
    #driver.find_elements_by_css_selector("button#nextBtn")[-1].click()
    pass


# In[58]:


# load_preview( 'https://new.hekayati.com/product/the-magic-of-al-ain-fc/')


# In[68]:


import random
import json
import sys

products= [ 
    """https://hekayati.com/en/shop/falcon/?preview=true&bookname=falcon&fname=Selenium&lname=&language=english&gender=girl&boyavatar=4&girlavatar=4&message=Life+is+a+magical+adventure%2C+and+we+want+you+to+go+and+live+it+to+the+full.+So%2C+follow+your+heart+and+reach+for+the+sky.+At+the+same+time+respect+our+values+and+keep+your+feet+firmly+on+the+ground.Mama+%26+Baba"""
]

import sys
try:
    preview_requests = int( sys.argv[1] )
except:
    preview_requests = time.monotonic_ns()

lstatus = []
ltime_taken = []
lbook_name = []
lrequest_no = []

    
print("Sending REquest no:", preview_requests)
try:
    url = random.choice(products)
    status, time_taken = load_preview( url )
except Exception as e:
    print("ER3453:", e)
    status = False
    time_taken = 300
    driver.save_screenshot(f"./chrome_snapshots/error_request_no_{preview_requests}.png")

if status == True:
    status = "Pass"
    driver.save_screenshot(f"./chrome_snapshots/pass_request_no_{preview_requests}.png")

else:
    status = "Fail"
    driver.save_screenshot(f"./chrome_snapshots/fail_request_no_{preview_requests}.png")

lstatus.append(status)
ltime_taken.append(time_taken)
book_name = url.split("/")[-2]
lbook_name.append( book_name )
lrequest_no.append(preview_requests)

import pandas as pd

df = pd.DataFrame()
df["Status"] = lstatus
df["TimeTaken"] = ltime_taken
df["BookName"] = lbook_name
df["Request#"] = lrequest_no

json_data = json.dumps(  df.to_dict(orient='list') )
with open("./csvs/" + str(preview_requests) + ".txt", "w") as f:
    f.write( json_data )


print("Quiting Driver Chrome...")
driver.quit()
# In[ ]:





# In[ ]:




