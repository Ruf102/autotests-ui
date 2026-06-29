import allure
from playwright.sync_api import expect

from elements.base_element import BaseElement

from tools.logger import get_logger

logger = get_logger('BUTTON')


class Button(BaseElement):
    @property
    def type_of(self) -> str:
        return "button"


    def check_disable(self, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" is disable'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_disabled()

    def check_enable(self, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" is disable'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_enabled()

