from playwright.sync_api import sync_playwright, expect  # Импорт Playwright для синхронного режима и проверки

# Запуск Playwright в синхронном режиме
with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()  # Создаем новую страницу

    # Переходим на страницу авторизации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    #Находим поле email и заполняем его
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    #Находим поле username и заполняем его
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill("username")

    #Находи поле password и заполняем его
    password_input1 = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input1.fill("password")

    #Находим кнопку registration и нажимаем на нее
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    #Проверяем заголовок dashboard
    dashboard = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard).to_be_visible()
    expect(dashboard).to_have_text('Dashboard')

    page.wait_for_timeout(5000)