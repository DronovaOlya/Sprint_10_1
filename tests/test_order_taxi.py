import allure
import pytest
from page_object.locators.main_page_locators import MainPageLocators
from page_object.urls import URL_MAIN_PAGE
from page_object.data import adress_one, adress_two, tariff_description_data

@allure.epic('Заказ тарифа такси')
class TestOrderTaxi:
    @allure.title('Проверка формы со всеми тарифами')
    def test_form_tariffst(self, main_page):
        main_page.go_to_page(URL_MAIN_PAGE)
        main_page.add_input_from(adress_one)
        main_page.add_input_to(adress_two)
        main_page.click_button_order_taxi()

        all_tariffs = main_page.get_all_tariffs()
        assert len(all_tariffs) == 6

        active_tariffs = main_page.get_active_tariffs()
        assert len(active_tariffs) == 1

    @pytest.mark.parametrize(
        'num',
        [0, 1, 2, 3, 4, 5]
    )   
    @allure.title('Проверка описания тарифов')
    def test_icons_i(self, num, main_page):
        if num in (1, 3):
            pytest.xfail("Баг AAA-001: описания Сонного и Разговорчивого перепутаны")
        main_page.go_to_page(URL_MAIN_PAGE)
        main_page.add_input_from(adress_one)
        main_page.add_input_to(adress_two)
        main_page.click_button_order_taxi()
        main_page.click_tariff_card(num)
        main_page.find_the_icon_i(num)

        assert main_page.check_tariff(num, tariff_description_data[num])

    @allure.title('Проверка отображения под тарифами блока с полями')
    def test_block_fields_taxi(self, main_page):
        main_page.go_to_page(URL_MAIN_PAGE)
        main_page.add_input_from(adress_one)
        main_page.add_input_to(adress_two)
        main_page.click_button_order_taxi() 

        check_phone = main_page.wait_and_find_element(MainPageLocators.LOCATOR_INPUT_PHONE)
        assert check_phone.is_displayed()

        check_payment_method = main_page.wait_and_find_element(MainPageLocators.LOCATOR_INPUT_PAYMENT_METHOD)
        assert check_payment_method.is_displayed()

        check_comment = main_page.wait_and_find_element(MainPageLocators.LOCATOR_INPUT_COMMENT)
        assert check_comment.is_displayed()

        check_comment = main_page.wait_and_find_element(MainPageLocators.LOCATOR_INPUT_ORDER_REQUIREMENTS)
        assert check_comment.is_displayed()

        

    




    