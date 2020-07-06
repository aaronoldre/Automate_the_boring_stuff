from selenium import webdriver


# check this in the book
# had error with needing path for firefox
browser = webdriver.Chrome()
browser.get('https://automatetheboringstuff.com/')
elem = browser.find_element_by_css_selector('.main > div:nth-child(1) > ul:nth-child(20) > li:nth-child(1) > a:nth-child(1)')
elem.click()
# return all elements 
elems = browser.find_elements_by_css_selector('p')
len(elems)

# type in the webpage
searchElem = browser.find_elements_by_css_selector('.search-field')
searchElem.send_keys('zophie')
# push the button
searchElem.submit()

elem_text = browser.find_element_by_css_selector('.entry-content > p:nth-child(4)')
print(elem_text)

# entire page
elem_page = browser.find_element_by_css_selector('html')

# back
browser.back()

# refresh
browser.refresh()

# close
browser.quit()