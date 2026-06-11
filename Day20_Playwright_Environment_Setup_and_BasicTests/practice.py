from xml.parsers import expat

from playwright.sync_api import Page, expect


def test_url(page:Page):
    page.goto("https://www.flipkart.com/")
    expect(page).to_have_url('https://www.flipkart.com/')
