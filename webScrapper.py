from selenium import webdriver

Word = input('Insert Word: ')

url = 'https://www.howmanysyllables.com/syllables/{0}'.format(Word)
browser = webdriver.Chrome()
browser.get(url)

print("Pronounced:", browser.find_element("xpath",'/html/body/div[1]/div[2]/div[1]/div[2]/p[2]/span[3]').text)