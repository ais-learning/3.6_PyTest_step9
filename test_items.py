# import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_backet_btn_is_present(browser):
    browser.get(link)
    # time.sleep(15) 
    btn = browser.find_element_by_class_name("btn-add-to-basket")
    assert btn.is_displayed()
