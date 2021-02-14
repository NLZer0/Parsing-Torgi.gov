import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time

URL = 'https://torgi.gov.ru/lotSearch1.html'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 YaBrowser/20.12.3.140 Yowser/2.5 Safari/537.36',
    'accept': '*/*',
}


def get_content(url): 
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source
    all_lots = []
    
    for i in range(10):
        soup = BeautifulSoup(html,'html.parser')
        main_information = soup.find_all(class_ = 'datarow')
            
        for it in main_information:

            organisator = it.find(class_ = 'datacell left').find_next()
            notification_numbers = organisator.find_next().find_next().find_next()
            lots_numbers = notification_numbers.find_next().find_next()
            type_of_property = lots_numbers.find_next().find_next()
            square = type_of_property.find_next().find_next()
            specifications = square.find_next().find_next()
            location = specifications.find_parent().find_next_sibling().find_next()
            initial_price = location.find_next().find_next()
            validity_period = initial_price.find_next().find_next().find_next()
            type_of_contract = validity_period.next_element.next_element.next_element
            monthly_payment = validity_period.find_next().find_next().find_next()

            all_lots.append({
                'Organisator': organisator.text,
                'Notification numbers': notification_numbers.text,
                'Lots numbers' : lots_numbers.text,
                'Type of property' : type_of_property.text,
                'Square' : square.text,
                'Specifications' : specifications.text,
                'Location' : location.text,
                'Initial price' : initial_price.text,
                'Validity period' : validity_period.text,
                'Type_of contract' : type_of_contract,
                'Monthly payment' : monthly_payment.text,
            })

        next_page = driver.find_element_by_id('id38')
        next_page.click()
        time.sleep(5)
        html = driver.page_source



    for it in all_lots:
            for key, value in it.items():
                print("{0}: {1}".format(key,value))
            print('\n\n')


def parse():
    get_content(URL)



# write_to_file() - Записываем сайт в файл
parse()
