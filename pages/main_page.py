import allure
from page_object.locators.main_page_locators import MainPageLocators
from page_object.pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Нажать на вид "Оптимальный"')
    def click_optimal(self):
        self.click_to_element(MainPageLocators.LOCATOR_TYPE_OPTIMAL)
     
    @allure.step('Нажать на вид "Свой"')
    def click_designer_button(self):
        self.click_to_element(MainPageLocators.LOCATOR_TYPE_MINE)

    @allure.step('Нажать на кнопку "Драйв"')
    def click_drive_button(self):
        self.click_to_element(MainPageLocators.LOCATOR_BUTTON_DRIVE)

    @allure.step('Нажать на кнопку "Заказать такси"')
    def click_button_order_taxi(self):
        self.click_to_element(MainPageLocators.LOCATOR_BUTTON_ORDER_TAXI)

    @allure.step('Нажать требования к заказу')
    def click_order_requirements(self):
        self.click_to_element(MainPageLocators.LOCATOR_INPUT_ORDER_REQUIREMENTS)

    @allure.step('Нажать на кнопку "Ввести номер и заказать"')
    def click_enter_number_and_order(self):
        self.click_to_element(MainPageLocators.LOCATOR_ENTER_NUMBER_AND_ORDER)

    @allure.step('Нажать на кнопку "Детали')
    def click_details(self):
        self.click_to_element(MainPageLocators.LOCATOR_BUTTON_DETAILS)

    @allure.step('Нажать на кнопку "Отменить')
    def click_cancel(self):
        self.click_to_element(MainPageLocators.LOCATOR_BUTTON_CANCEL)

    @allure.step('Дождаться таймера')
    def wait_timer_and_open_details(self, seconds: int = 30):
        self.wait_for_timer_via_settimeout(seconds)

    @allure.step('Найти элемент')
    def find_element_auth(self):
        self.wait_and_find_element(MainPageLocators.LOCATOR_COLLECT_ORDER)

    @allure.step('Взять начальное значение каунтера')
    def get_counter(self) -> int:
        return self.get_counter_value(MainPageLocators.LOCATOR_COUNTER_SAUCE)

    @allure.step('Взять текст стоимости заказа')
    def take_cost(self):
        return self.get_text_to_element(MainPageLocators.LOCATOR_COST)

    @allure.step('Взять текст времени заказа')
    def take_time(self):
        return self.get_text_to_element(MainPageLocators.LOCATOR_TIME)

    @allure.step('Заполнить поле "Откуда"')
    def add_input_from(self, data):
        self.add_text_to_element(MainPageLocators.LOCATOR_INPUT_FROM, data)

    @allure.step('Заполнить поле "Куда"')
    def add_input_to(self, data):
        self.add_text_to_element(MainPageLocators.LOCATOR_INPUT_TO, data)

    @allure.step("Проверить, что происходит смена активного таба на Оптимальный")
    def change_active_tobacco(self):
        def is_optimal_active():
            elements = self.wait_and_find_elements(MainPageLocators.LOCATOR_TYPE_OPTIMAL)
            if not elements:
                return False
            classes = elements[0].get_attribute("class") or ""
            return "mode" in classes and "active" in classes
        return True
    
    @allure.step("Проверить, что происходит смена активного таба на Свой")
    def change_active_type_mine(self):
            def is_optimal_active():
                elements = self.wait_and_find_elements(MainPageLocators.LOCATOR_TYPE_MINE)
                if not elements:
                    return False
                classes = elements[0].get_attribute("class") or ""
                return "mode" in classes and "active" in classes
            return True

    @allure.step('Проверить, что все иконки транспорта активны')
    def are_all_types_active(self):
        types = self.wait_and_find_elements(MainPageLocators.LOCATOR_TYPES_CONTAINER)
        return all(
            "disabled" not in (el.get_attribute("class") or "")
            for el in types
        )
    
    @allure.step('Получить все тарифы')
    def get_all_tariffs(self):
        return self.wait_and_find_elements(MainPageLocators.LOCATOR_TARIFF_CARDS)

    @allure.step('Получить активные тарифы')
    def get_active_tariffs(self):
        return self.wait_and_find_elements(MainPageLocators.LOCATOR_ACTIVE_TARIFF)

    @allure.step('Выбрать тариф')
    def click_to_tariff(self,num):
        locator_question_formatted = self.format_locators(MainPageLocators.LOCATOR_QUESTION, num)
        self.click_to_element(locator_question_formatted)

    @allure.step('Навести на иконку i')
    def find_the_icon_i(self,num):
        locator_icon_i_formatted = self.format_locators(MainPageLocators.LOCATOR_ICONS_I, num)
        self.hover_element(locator_icon_i_formatted)

    @allure.step('Получить описание тарифа')
    def get_text_tariff(self, num):
        locator_tariff_formatted = self.format_locators(MainPageLocators.LOCATOR_TEXT_DESCRIPTION_TARIFF, num)
        return self.get_text_to_element(locator_tariff_formatted)

    @allure.step('Проверить описание тарифа')
    def check_tariff(self, num, expected_text):
        self.find_the_icon_i(num)
        locator = self.format_locators(MainPageLocators.LOCATOR_TEXT_DESCRIPTION_TARIFF,expected_text)
        element = self.wait_and_find_element(locator)
        return element.is_displayed()

    @allure.step('Взять стоимостm заказа такси в тарифе рабочий')
    def take_taxi_fare(self):
        return self.get_text_to_element(MainPageLocators.LOCATOR_TAXI_FARE)

    @allure.step('Выбрать тариф')
    def click_tariff_card(self, num):
        locator = self.format_locators(MainPageLocators.LOCATOR_TARIFF_CARD, num + 1)
        self.click_to_element(locator)
