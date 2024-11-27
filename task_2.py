# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Авторизация
    driver.get("https://fix-online.sbis.ru/")
    login_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='﻿'][@type='text']"))
    )
    login_field.clear()
    login_field.send_keys("арагорн")

    # Нажать на кнопку типа входа
    sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-qa='auth-AdaptiveLoginForm__checkSignInTypeButton']"))
    )
    sign_in_button.click()

    # Ввод пароля
    password_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='﻿'][@type='password']"))
    )
    password_field.clear()
    password_field.send_keys("123арагорн123")

    # Клик по кнопке входа
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'auth-AdaptiveLoginForm__loginButtonImage')]"))
    )
    login_button.click()

    # Ожидаем загрузки страницы
    WebDriverWait(driver, 10).until(EC.url_contains("https://fix-online.sbis.ru/"))

    # Переходим в реестр "Контакты"
    contacts_menu = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[@data-qa='NavigationPanels-Accordion__title' and text()='Контакты']"))
    )
    contacts_menu.click()

    # Ждём, пока откроется подменю "Контакты" и выполняем клик
    contacts_submenu = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'NavigationPanels-SubMenu__headTitle')]"))
    )
    contacts_submenu.click()

    # Ожидаем перехода на страницу диалогов
    WebDriverWait(driver, 10).until(EC.url_contains("https://fix-online.sbis.ru/page/dialogs"))

    # Нажимаем кнопку для добавления нового сообщения
    add_message_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@data-qa='informers_informerContent_Messages_icon']"))
    )
    add_message_button.click()

    # Дождаться исчезновения блокирующего элемента
    blocker = WebDriverWait(driver, 10).until(
        EC.invisibility_of_element(
            (By.XPATH, "//div[contains(@class, 'helpBase-routesRunCommon-RouteClickTargetBlocker')]"))
    )

    # Проверка видимости поля "Сотрудники"
    employees_tab = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH,
             "//div[@data-qa='TabsItemSelected' and contains(@class, 'ws-flexbox') and contains(@class, 'controls-Tabs__item_view_selected_style_unaccented')]//div[text()='Сотрудники']"))
    )

    # Убедиться, что поле ввода кликабельно
    message_input_field = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class, 'controls-Render__placeholder_overflow') and text()='Найти']/ancestor::div[contains(@class, 'controls-Render__field')]//input)[1]"))
    )

    # Проверить, что элемент отображается, перед взаимодействием
    if message_input_field.is_displayed():
        # Клик и ввод текста
        message_input_field.click()
        message_input_field.send_keys("Петряев")
    else:
        raise Exception("Поле ввода недоступно для взаимодействия")

    # Ожидание появления результата поиска и клик по имени "Петряев Даниил"
    result_name = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-qa='person-Information__fio' and text()='Петряев Даниил']"))
    )
    result_name.click()

    # Ожидание появления окна для ввода сообщения
    message_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@role='textbox'][@data-qa='textEditor_slate_Field']"))
    )
    message_field.click()
    message_field.send_keys("Тестовое сообщение для автотеста")

    # Ожидание кнопки "Отправить" и клик по ней
    send_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@data-qa='msg-send-editor__send-button' and contains(@class, 'controls-BaseButton') and contains(@title, 'Отправить')]"))
        )
    send_button.click()

    # Ожидание кнопки закрытия окна и клик по ней
    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "//span[@data-qa='controls-stack-Button__close' and contains(@class, 'controls-stack-Button__rightPanel__close')]"))
    )
    close_button.click()

    # Проверка наличия сообщения в реестре
    sent_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'msg-entity-text') and contains(@class, 'msg-dialogs-item__message-text') and @tabindex='0']//p[text()='Тестовое сообщение для автотеста']"))
    )
    assert sent_message is not None, "Отправленное сообщение не найдено!"

    # Удаление сообщения
    toggle_operations_panel = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH,
             "//div[@data-name='toggleOperationsPanel' and @data-qa='toggleOperationsPanel' and contains(@class, 'controls-Toolbar__item')]"))
    )

    # Клик по найденному элементу
    toggle_operations_panel.click()

    # Поиск чекбокса на созданном ранее сообщении
    checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='msg-dialogs-item__content-inner msg-entity-content__inner ws-flex-shrink-1 ws-flex-grow-1' and .//p[text()='Тестовое сообщение для автотеста']]/ancestor::div[contains(@class, 'controls-ListView__item')]//div[@data-qa='controls-CheckboxMarker']"))
    )

    # Клик по чекбоксу
    checkbox.click()

    # Поиск кнопки "Удалить"
    delete_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH,
             "//span[@class='controls-BaseButton__text controls-button__text_captionPosition_end controls-Button__text_viewMode-link controls_text-style_default' and text()='Удалить']")
        )
    )

    # Клик по кнопке "Удалить"
    delete_button.click()

    # Проверка отсутствия сообщения
    message_absent = WebDriverWait(driver, 5).until_not(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class, 'msg-entity-text') and text()='Тестовое сообщение для автотеста']"))
    )

    assert message_absent, "Сообщение не удалено!"
    print("Сообщение успешно удалено.")

finally:
    driver.quit()
