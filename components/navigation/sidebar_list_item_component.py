from typing import Pattern

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier):
        super().__init__(page)

        self.button = page.get_by_test_id(f'{identifier}-drawer-list-item-button')
        self.title = page.get_by_test_id(f'{identifier}-drawer-list-item-button')
        self.icon = page.get_by_test_id(f'{identifier}-drawer-list-item-button')

    def check_visible(self, title):
        expect(self.button).to_be_visible()

        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(title)

        expect(self.icon).to_be_visible()

    def navigate(self, expected_url: Pattern[str]):
        self.button.click()

        self.check_current_url(expected_url)
