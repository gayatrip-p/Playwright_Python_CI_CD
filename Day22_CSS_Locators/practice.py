from playwright.sync_api import Page, expect
import time

def test_idlocator(page:Page):
    page.goto('https://demowebshop.tricentis.com/')
    page.locator('input#small-searchterms').fill('laptop')
    page.locator('input.button-1.search-box-button[value=Search]').click()
    page.close()



    