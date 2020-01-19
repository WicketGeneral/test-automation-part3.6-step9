import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_basket_button_is_present_on_the_page(browser):
    browser.get(link)
    #time.sleep(3)
    try:
        browser.find_element_by_css_selector("button.btn-add-to-basket")
        check = True
    except:
        check = False
    assert check == True , "No basket button on the page!"