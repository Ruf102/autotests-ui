from typing import Pattern

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button
from elements.icon import Icon
from elements.text import Text


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier):
        super().__init__(page)

        self.button = Button(page, f'{identifier}-drawer-list-item-button', 'Button')
        self.title = Text(page, f'{identifier}-drawer-list-item-button', 'Title')
        self.icon = Icon(page, f'{identifier}-drawer-list-item-button', "Icon")

    def check_visible(self, title):
        self.button.check_visible()

        self.title.check_visible()
        self.title.check_have_text(title)

        self.icon.check_visible()

    def navigate(self, expected_url: Pattern[str]):
        self.button.click()
        self.check_current_url(expected_url)
