import time


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_get_item_in_basket(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    time.sleep(10)
    button = browser.find_element_by_class_name('btn-add-to-basket')
    text_in_button = button.text
    assert text_in_button == 'Добавить в корзину', 'There is no button to add in basket'

