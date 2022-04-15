import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


CHROMEDRIVER_PATH = r"C:\Users\****\AppData\Local\Programs\Python\Python37-32\chromedriver.exe"
options = Options()
options.headless = True
#options.add_argument('--disable-gpu')  # Last I checked this was necessary.
driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)

url = 'https://www.google.com/maps/place/7900+Shelbyville+Rd,+Louisville,+KY+40222'
print(url)
#driver = webdriver.Chrome(r"C:\Users\***\AppData\Local\Programs\Python\Python37-32\chromedriver.exe")

driver.get(url)

time.sleep(4)

cur_url = driver.current_url

#print(cur_url)

cur_splt_url = cur_url.split('/')

location = cur_splt_url[6]
characters_to_remove = '@,'

for characters in characters_to_remove:
    location = location.replace(characters,'')

#print(location)

lat_long = location.split('-')

latitude = lat_long[0]
longitude = lat_long[1]

print(latitude)
print(longitude)






# quard = cur_url.replace(url, '')
#
# print(quard)
#
# quadrant = quard.split("/",7)[1]
#
# print(quadrant)
#
# lat = quadrant.split(",")[0]
# longg = quadrant.split(",")[1]
# print(lat,longg)

