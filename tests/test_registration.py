from playwright.sync_api import sync_playwright, expect, Page
import pytest

@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page):
        chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        registration_email = chromium_page.get_by_test_id("registration-form-email-input").locator("input")
        registration_email.fill("user.name@gmail.com")

        registration_username = chromium_page.get_by_test_id("registration-form-username-input").locator("input")
        registration_username.fill("username")

        registration_password = chromium_page.get_by_test_id("registration-form-password-input").locator("input")
        registration_password.fill("password")

        registration_button = chromium_page.get_by_test_id("registration-page-registration-button")
        registration_button.click()

        dashboard_title = chromium_page.get_by_test_id("dashboard-toolbar-title-text")
        expect(dashboard_title).to_be_visible()