from pages.main_page import MainPage


def test_tensor_navigation(driver):
    # Открыть главную страницу
    main_page = MainPage(driver)
    main_page.open()

    # Перейти в контакты
    contacts_page = main_page.go_to_contacts()

    # Кликнуть на баннер "Тензор" и переключиться на новое окно
    tensor_page = contacts_page.click_tensor_banner()

    # Проверить наличие блока "Сила в людях"
    assert tensor_page.is_news_block_present(), "Блок 'Сила в людях' отсутствует!"

    # Перейти по кнопке "Подробнее"
    tensor_page.click_more_details()

    # Проверить, что открылась страница "О компании"
    assert tensor_page.is_about_page_opened(), "Не удалось открыть страницу 'О компании'!"
