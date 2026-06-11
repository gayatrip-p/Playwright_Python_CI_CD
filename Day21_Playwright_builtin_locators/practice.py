# import time
#
# from playwright.sync_api import Page, expect
#
# def test_pagelogo(page:Page):
#     page.goto("https://demo.nopcommerce.com/")
#     time.sleep(5000)
#     logo=page.get_by_alt_text("nopCommerce demo store")
#     expect(logo).to_be_visible()


from playwright.sync_api import Page, expect


def test_demo(page:Page):
    page.goto('https://rahulshettyacademy.com/AutomationPractice/')
    expect(page.get_by_text("Practice Page")).to_be_visible()