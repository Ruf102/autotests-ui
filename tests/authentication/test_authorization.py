import allure
import pytest
from allure_commons.types import Severity

from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag


@pytest.mark.regression
@pytest.mark.authorization
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHORIZATION)  # Используем enum
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
class TestAuthorization:

    @allure.title("Успешная авторизация")
    @allure.tag(AllureTag.USER_LOGIN)  # Тег для конкретного теста
    @allure.severity(Severity.BLOCKER)
    def test_successful_authorization(
            self, login_page: LoginPage,
            registration_page: RegistrationPage,
            dashboard_page: DashboardPage
    ):
        registration_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
        )

        registration_page.registration_form.fill(email="username@test.ru", username="username", password="Test123")
        registration_page.page.wait_for_timeout(1000)
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible(username="username")
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()

        login_page.login_form.fill(email="username@test.ru", password="Test123")
        login_page.click_login_button()

        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible(username="username")
        dashboard_page.sidebar.check_visible()

    @pytest.mark.parametrize(
        "email, password",
        [
            ("user.name@gmail.com", "password"),
            ("user.name@gmail.com", "  "),
            ("  ", "password")
        ]
    )
    @allure.title("Авторизация в систему с неверным email или паролем")
    @allure.tag(AllureTag.USER_LOGIN)  # Тег для конкретного теста
    @allure.severity(Severity.CRITICAL)
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.login_form.fill(email=email, password=password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()

    @allure.title("Переход со страницы входа на страницу регистрации")
    @allure.tag("NAVIGATION")
    @allure.severity(Severity.NORMAL)
    def test_navigate_from_authorization_to_registration(
            self,
            login_page: LoginPage,
            registration_page: RegistrationPage
    ):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.click_registration_link()

        registration_page.registration_form.check_visible(email="", username="", password="")
