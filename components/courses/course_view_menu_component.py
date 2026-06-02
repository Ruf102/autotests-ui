from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from elements.button import Button
from elements.text import Text
import allure


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = Button(page, 'course-view-menu-button', "Menu button")
        self.edit_menu_item = Button(page, 'course-view-edit-menu-item', "Edit button")
        self.delete_menu_item = Button(page, 'course_delete_menu_item', "Delete button")

    @allure.step("Open course menu at index '{index}' and click edit")
    def click_edit(self, index: int):
        self.menu_button.click(nth=index)

        self.edit_menu_item.check_visible(nth=index)
        self.edit_menu_item.click(nth=index)

    @allure.step("Open course menu at index '{index}' and click delete")
    def click_delete(self, index: int):
        self.menu_button.click(nth=index)

        self.delete_menu_item.check_visible(nth=index)
        self.delete_menu_item.click(nth=index)

