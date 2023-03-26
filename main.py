import ast
import os
# import the library module
import sys
import hashlib

def join(l, sep):
    out_str = ''
    for i, el in enumerate(l):
        out_str += '{}{}'.format(el, sep)
    return out_str[:-len(sep)]
  
if sys.version_info < (3, 6):
    import sha3
 
# initialize a string
def encode(str):
 
  # encode the string
  encoded_str = str.encode()
   
  # create sha3-256 hash objects
  obj_sha3_512 = hashlib.sha3_512(encoded_str)
   
  # print in hexadecimal
  return obj_sha3_512.hexdigest()
user = ""
while True:
  users = next(os.walk('users'))[1]
  operation = input("Login or create account? (Enter 1 for login or 2 for create; no email is required, just username and password): ")
  if operation == "1":
    pws = {}
    with open('users.txt') as f:
      pws = ast.literal_eval(f.readlines()[0])
    while True:
      username = input("Username: ")
      if username not in users:
        print("Invalid username!")
      else:
        pw = input("Password: ")
        if pws[username] != encode(pw):
          print("Incorrect password!")
        else:
          user = username
          break
  else:
    pws = {}
    with open('users.txt') as f:
      pws = ast.literal_eval(f.readlines()[0])
    while True:
      username = input("Username: ")
      if username in users:
        print("Username taken!")
      else:
        pw = input("Password: ")
        pws[username] = encode(pw)
        text_file = open("users.txt", "w")
        n = text_file.write(str(pws))
        text_file.close()
        user = username
        break
  break
    
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-web-security')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument("user-data-dir=users/"+user)
chrome_options.add_argument("start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=chrome_options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
print(driver.execute_script("return navigator.userAgent;"))
driver.get("https:/google.com")

def type(data):
  actions = ActionChains(driver)
  actions.send_keys(data)
  actions.perform()

start = input("Hit enter when you're ready!")
time.sleep(5)
while True:
  type("hi")
  type(Keys.ENTER)
  time.sleep(1)