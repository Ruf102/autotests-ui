from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.courses.course_view_menu_component import CourseViewMenuComponent
from data.course_data import CheckVisibleCourseCardParams
from elements.image import Image
from elements.text import Text
import allure


class CourseViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu = CourseViewMenuComponent(page)

        self.title = Text(page, 'course-widget-title-text', 'Title')
        self.image = Image(page, 'course-preview-image', 'Image')
        self.max_score_text = Text(page, 'course-max-score-info-row-view-text', 'Max score')
        self.min_score_text = Text(page, 'course-min-score-info-row-view-text', 'Min score')
        self.estimated_time_text = Text(page, 'course-estimated-time-info-row-view-text', 'Estimated time')

    def check_visible(self, params: CheckVisibleCourseCardParams):
        with allure.step(f"Check visible course view at index '{params.index}'"):
            self.image.check_visible(nth=params.index)

            self.title.check_visible(nth=params.index)
            self.title.check_have_text(params.title, nth=params.index)

            self.max_score_text.check_visible(nth=params.index)
            self.max_score_text.check_have_text(f"Max score: {params.max_score}", nth=params.index)

            self.min_score_text.check_visible(nth=params.index)
            self.min_score_text.check_have_text(f"Min score: {params.min_score}", nth=params.index)

            self.estimated_time_text.check_visible(nth=params.index)
            self.estimated_time_text.check_have_text(f"Estimated time: {params.estimated_time}", nth=params.index)
