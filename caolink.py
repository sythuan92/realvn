# Import libraries and packages for the project 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from time import sleep
from openpyxl import load_workbook
import openpyxl
import time
import random

print('- Finish importing packages')
proxy = "27.79.137.213:45360"
# setup selenium webdriver
opt = webdriver.ChromeOptions()
# opt.add_extension("Block-image_v1.1.crx")
prefs = {"profile.managed_default_content_settings.images": 2}
opt.add_experimental_option("prefs", prefs)
opt.add_argument('--disable-gpu')
opt.add_argument("--window-size=1920,1080")
opt.add_argument("--start-maximized")
opt.add_argument('--disable-dev-shm-usage')
opt.add_argument('--no-sandbox')
opt.add_argument('--ignore-certificate-errors')
# opt.add_argument('--headless')
opt.add_argument('--proxy-server={}'.format(proxy))
opt.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36")
# driver = webdriver.Chrome(options=opt)
driver = webdriver.Chrome(options=opt)
sleep(2)
url = 'https://batdongsan.com.vn/nha-dat-cho-thue-da-nang'
driver.get(url)
sleep(2)

print('vào website')

def geturl():
    page_source = BeautifulSoup(driver.page_source,"html.parser")
    # print(page_source)
    urls_bds = page_source.find_all("a",class_="wrap-plink")
    all_URL = []
    for url_bds in urls_bds:
        url_ID = url_bds.get('href')
        url_URL = "https://batdongsan.com.vn" + url_ID
        if url_URL not in all_URL:
            all_URL.append(url_URL)
    return(all_URL)

input_page = int(input('How many pages you want to scrape: '))
URLs_all_page = []

for page in range(input_page):
    URLs_one_page = geturl()
    # print(geturl())
    sleep(2)
    a = page+2
    nexturl = url+"/p" + str(a)
    # print(nexturl)
    driver.get(nexturl)
    URLs_all_page = URLs_all_page + URLs_one_page
    sleep(2)
print('- Finish Task 3: Scrape the URLs')
print(URLs_all_page)

b =2
for linkbds in URLs_all_page:
    wa = load_workbook('ketquabds.xlsx')
    was = wa.worksheets[0]
    # print(linkbds)
    tdlink1 = "d" + str(b)
    # print(tdlink1)
    was[tdlink1] = linkbds
    b = b + 1
    wa.save('ketquabds.xlsx')
    # print("có vào lưu file")

print("lưu link rồi")

# i = 2
# for linkedin_URL in URLs_all_page:
#     driver.get(linkedin_URL)
#     print('- Accessing profile: ', linkedin_URL)
#     page_source = BeautifulSoup(driver.page_source, "html.parser")
#     info_div = page_source.find('div',{'class':'user'})
#     info_loc = info_div.find_all('div')
#     # print(info_loc)
#     try:
#         name = info_loc[1].get("title")
#     except:
#         name ="không có"
#     #HÀM THAY ĐỔI    
#     print(info_loc[2])
#     ploai = info_loc[2].get("class")
#     print(type(ploai))
#     if ploai == ["info"]:
#         sdtraw = info_loc[3].find("span")
#         try:
#             sdt= sdtraw.get("raw")
#         except:
#             sdt="không có"
#         emailraw = info_loc[4].find("a")
#         try:
#             email =emailraw.get("data-email")
#         except:
#             email="không có"
#     else:
#         sdtraw = info_loc[2].find("span")
#         try:
#             sdt= sdtraw.get("raw")
#         except:
#             sdt="không có"
#         emailraw = info_loc[3].find("a")
#         try:
#             email =emailraw.get("data-email")
#         except:
#             email="không có"
#     # print(f"thông tin khách hàng tên {name} sdt là {sdt} có email là {email}")
#     tdten = "a"+ str(i)
#     tdsdt = "b"+ str(i)
#     tdemail = "c" + str(i)
#     # tdlink = "d" + str(i)
#     wb = load_workbook('ketquabds.xlsx')
#     activesheet = wb.worksheets[0]
#     activesheet[tdten] = name
#     activesheet[tdsdt] = sdt
#     activesheet[tdemail] = email
#     # activesheet[tdlink] = linkedin_URL
#     i = i +1
#     wb.save('ketquabds.xlsx')
#     time.sleep(random.randint(1, 3))
#     print(f"Đã xử lí xong {i} khách hàng")

# print('Mission Completed!')