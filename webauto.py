from selenium import webdriver
import time

# Use Chrome and input URL of Google Form to automate
web = webdriver.Chrome()
web.get("https://docs.google.com/forms/d/1PN6x5cqFzg3DqUGe9jA-AP11ky0yz3HE4HE9DCCFKUc/edit")

# Waits .5 seconds for website to render before performing code below
time.sleep(.5)

# Find the element you want to be edited by xpath in HTML source code, and then inputs variable to element or clicks radio button
lastName = "Kim"
last = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
last.send_keys(lastName) #

firstName = "Billy"
first = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
first.send_keys(firstName)

likeCats = web.find_element_by_xpath('//*[@id="i16"]/div[3]/div')
likeCats.click()

howManyCats = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div/span/div/div[2]/label')
howManyCats.click()

howMuchLikeCats = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/span/div/label[10]/div[2]/div/div/div[3]/div')
howMuchLikeCats.click()

whichBreed = web.find_element_by_xpath('//*[@id="i58"]/div[3]/div')
whichBreed.click()


time.sleep(1)
submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
submit.click()

get_confirmation_div_text = web.find_element_by_css_selector('.freebirdFormviewerViewResponseConfirmationMessage')
if get_confirmation_div_text.text == "Your response has been recorded.":
    print("Test successful :)")
else:
    print("Test failed :(")
