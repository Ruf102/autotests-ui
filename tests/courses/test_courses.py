import allure
import pytest

from config import settings
from data.course_data import CheckVisibleCourseCardParams
from pages.courses.course_create_page import CreateCoursePage
from pages.courses.courses_list_page import CoursesListPage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity

from tools.routes import AppRoute


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES) # Используем enum
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.suite(AllureFeature.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    @allure.title("Создание курса")
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, courses_list_page: CoursesListPage, course_create_page: CreateCoursePage):
        course_create_page.visit(AppRoute.COURSES_CREATE)

        course_create_page.create_course_toolbar_view.check_visible()
        course_create_page.image_upload_widget.check_visible(is_image_uploaded=False)

        course_create_page.create_course_form.check_visible(
            title='',
            estimated_time='',
            description='',
            max_score='0',
            min_score='0'
        )

        course_create_page.create_course_exercises_toolbar_view.check_visible()
        course_create_page.check_visible_exercises_empty_view()

        course_create_page.image_upload_widget.upload_preview_image(file=settings.test_data.image_png_file)
        course_create_page.image_upload_widget.check_visible(is_image_uploaded=True)
        course_create_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        course_create_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(CheckVisibleCourseCardParams(
            index=0,
            title="Playwright",
            estimated_time="2 weeks",
            max_score="100",
            min_score="10"
        ))

    @allure.title("Отображение пустого представления списка курсов")
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit(AppRoute.COURSES)

        courses_list_page.navbar.check_visible(settings.test_user.username)
        courses_list_page.sidebar.check_visible()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    @allure.title("Редактирование курса")
    @allure.severity(Severity.NORMAL)
    def test_edit_course(self, courses_list_page: CoursesListPage, course_create_page: CreateCoursePage):
        courses_list_page.visit(AppRoute.COURSES_CREATE)
        course_create_page.image_upload_widget.upload_preview_image(file=settings.test_data.image_png_file)
        course_create_page.image_upload_widget.check_visible(is_image_uploaded=True)
        course_create_page.create_course_form.fill(
            title="Python",
            estimated_time="10h",
            description="Описание курса",
            min_score="100",
            max_score="50"
        )
        course_create_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(CheckVisibleCourseCardParams(
            index=0,
            title="Python",
            estimated_time="10h",
            min_score="100",
            max_score="50"
        ))
        courses_list_page.course_view.menu.click_edit(index=0)

        course_create_page.create_course_form.fill(
            title="Python+playwright",
            estimated_time="20h",
            description="Новое описание курса",
            min_score="200",
            max_score="100"
        )
        course_create_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(CheckVisibleCourseCardParams(
            index=0,
            title="Python+playwright",
            estimated_time="20h",
            min_score="200",
            max_score="100"
        ))
