from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()  # Создание контекста
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_email = page.get_by_test_id("registration-form-email-input").locator("input")
    registration_email.fill("user.name@gmail.com")

    registration_username = page.get_by_test_id("registration-form-username-input").locator("input")
    registration_username.fill("username")

    registration_password = page.get_by_test_id("registration-form-password-input").locator("input")
    registration_password.fill("password")

    page.wait_for_timeout(5000)
    registration_button = page.get_by_test_id("registration-page-registration-button")
    registration_button.click()

    context.storage_state(path="browser-state.json")

    header_dashboard = page.get_by_test_id("dashboard-toolbar-title-text")
    expect(header_dashboard).to_be_visible()
    expect(header_dashboard).to_have_text("Dashboard")

    page.wait_for_timeout(5000)

# Остальной код регистрации нового пользователя без изменений

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json") # Указываем файл с сохраненным состоянием
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

    page.wait_for_timeout(5000)