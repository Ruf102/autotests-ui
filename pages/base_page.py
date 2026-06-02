from re import Pattern
import allure
from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        with allure.step(f'Opening the url: "{url}"'):
            self.page.goto(url, wait_until='networkidle')

    def reload(self):
        with allure.step(f'Reload page with url: "{self.page.url}"'):
            self.page.reload(wait_until="networkidle")

    def check_current_url(self, expected_url: Pattern[str]):
        with allure.step(f'Checking thet current url match pattern "{expected_url.pattern}"'):
            expect(self.page).to_have_url(expected_url)
