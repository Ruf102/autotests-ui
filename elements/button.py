import allure
from playwright.sync_api import expect

from elements.base_element import BaseElement


class Button(BaseElement):
    @property
    def type_of(self) -> str:
        return "button"


    def check_disable(self, nth: int = 0, **kwargs):
        with allure.step(f'Checking that {self.type_of} "{self.name}" is disable'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_disabled()

    def check_enable(self, nth: int = 0, **kwargs):
        with allure.step(f'Checking that {self.type_of} "{self.name}" is enable'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_enabled()

