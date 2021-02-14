from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36")

URL = 'https://torgi.gov.ru/lotSearch1.html'

def get_content(url, nums_of_pages): 
    driver = webdriver.Chrome(chrome_options=opts)
    driver.get(url)
    html = driver.page_source
    all_lots = []
    
    for i in range(nums_of_pages):
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


        try:
            next_page = driver.find_element_by_id('id38')
        except:
            print("Все существующие страницы уже были распарсены")
            break

        next_page.click()
        time.sleep(5)
        html = driver.page_source
        
        persent = int((i+1)*(100/nums_of_pages))
        persent = str(persent)+'%'
        print("Завершено:",persent)


    for it in all_lots:
            for key, value in it.items():
                print("{0}: {1}".format(key,value))
            print('\n\n')


def parse():

    print('Введите ссылку раздела, с которого будет скопированна информация (по умолчанию раздел Аренда)')
    url = str(input())
    if url == '':
        url = URL


    print('Введите количество страниц для парсинга (по умолчанию одна)')
    nums_of_pages = str(input())
    if nums_of_pages == '':
        nums_of_pages = '1'
    if nums_of_pages.isdigit():
        print('Производится парсинг')
        get_content(url, int(nums_of_pages))    


parse()
