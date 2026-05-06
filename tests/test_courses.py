import pytest
from playwright.sync_api import Page, expect

from data.course_data import CheckVisibleCourseCardParams
from pages.course_create_page import CourseCreatePage
from pages.courses_list_page import CoursesListPage

@pytest.mark.courses
@pytest.mark.regression
def test_create_course(courses_list_page: CoursesListPage, course_create_page: CourseCreatePage):
        course_create_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

        course_create_page.check_visible_create_course_title()
        course_create_page.check_disabled_create_course_button()
        course_create_page.check_visible_image_preview_empty_view()
        course_create_page.check_visible_image_upload_view(is_image_uploaded=False)

        course_create_page.check_visible_create_course_form(
            title='',
            estimated_time='',
            description='',
            max_score='0',
            min_score='0'
        )

        course_create_page.check_visible_exercises_title()
        course_create_page.check_visible_create_exercise_button()
        course_create_page.check_visible_exercises_empty_view()

        course_create_page.upload_preview_image(file='./testdata/files/image.png')
        course_create_page.check_visible_image_upload_view(is_image_uploaded=True)

        course_create_page.fill_create_course_form(
            title = "Playwright",
            estimated_time = "2 weeks",
            description = "Playwright",
            max_score = "100",
            min_score = "10"
        )

        course_create_page.click_create_course_button()

        courses_list_page.check_visible_courses_title()
        courses_list_page.check_visible_create_course_button()
        courses_list_page.check_visible_course_card(CheckVisibleCourseCardParams(
            index=0,
            title="Playwright",
            estimated_time="2 weeks",
            max_score="100",
            min_score="10"
        ))

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_list_page.navbar.check_visible('username')
    courses_list_page.sidebar.check_visible()

    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_empty_view()

