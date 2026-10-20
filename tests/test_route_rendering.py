import allure
from page_object.locators.main_page_locators import MainPageLocators
from page_object.data import adress_one, adress_two
from page_object.urls import URL_MAIN_PAGE

@allure.epic('Отрисовка маршрута')
class TestRouteRendering:
    @allure.title('Проверка отображения начала и конца маршрута')
    def test_route_rendering(self, main_page):
        main_page.go_to_page(URL_MAIN_PAGE)
        main_page.add_input_from(adress_one)
        main_page.add_input_to(adress_two)

        check_a = main_page.wait_and_find_element(MainPageLocators.LOCATOR_POINT_A)
        assert check_a.is_displayed()

        check_b = main_page.wait_and_find_element(MainPageLocators.LOCATOR_POINT_B)
        assert check_b.is_displayed()

    