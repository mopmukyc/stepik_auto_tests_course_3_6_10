import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_shop_language(browser):
    
    # Открываем браузер
    browser.get(link)

    time.sleep(30)

    btn = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    btn.click()

    assert True, 'Error text'



    


