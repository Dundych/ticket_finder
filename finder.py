# -*- coding: utf-8 -*-

from selenium import webdriver
import os, time

browser = webdriver.Firefox()
browser.implicitly_wait(10) # seconds

browser.get('http://booking.uz.gov.ua/ru/')

def get_result(city_from, city_to, date):
  field_from = browser.find_element_by_css_selector('div#station_from input')
  field_from.send_keys(city_from)
  autosuggest_from = browser.find_element_by_css_selector('div#stations_from > div:nth-child(1)')
  autosuggest_from.click()

  field_till = browser.find_element_by_css_selector('div#station_till input')
  field_till.send_keys(city_to)
  autosuggest_till = browser.find_element_by_css_selector('div#stations_till > div:nth-child(1)')
  autosuggest_till.click()

  field_date = browser.find_element_by_css_selector('input#date_dep')
  field_date.clear()
  field_date.send_keys(date)

  button_search = browser.find_element_by_css_selector("button[name='search']")
  button_search.click()

  if browser.find_element_by_css_selector("#ts_res_not_found").is_displayed():
    return None
  else:
    result = browser.find_element_by_css_selector("#ts_res_tbl")
    return result

res_table = get_result("Киев", "Херсон", "01.9.2015")

if res_table != None:
  # Save the table to result
  imageFile = open('result.html', 'w')
  imageFile.write(res_table.get_attribute('innerHTML'))
  imageFile.close()
  print(res_table.get_attribute('innerHTML'))

browser.quit()
