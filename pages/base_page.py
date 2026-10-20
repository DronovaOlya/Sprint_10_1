import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver, timeout=15): 
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)

    @allure.step('Открыть главную страницу')
    def go_to_page(self, url):
        self.driver.get(url)

    @allure.step('Найти элемент')
    def wait_and_find_element(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Найти элементы')
    def wait_and_find_elements(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step('Нажать на элемент')
    def click_to_element(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def wait_text(self, locator, text):
        self.wait.until_not(expected_conditions.text_to_be_present_in_element_value(locator, text))
        return self.driver.find_element(*locator).text

    @allure.step('Заполнить поле ввода')
    def add_text_to_element(self, locator, text):
        self.wait_and_find_element(locator).send_keys(text)

    def get_text_to_element(self, locator):
        return self.wait_and_find_element(locator).text

    @allure.step('Найти кликабельный элемент')
    def wait_and_find_clickable_element(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return method, locator

    @allure.step('Навести курсор на элемент')
    def hover_element(self, locator):
        element = self.wait_and_find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    @allure.step('Дождаться окончания таймера через setTimeout')
    def wait_for_timer_via_settimeout(self, seconds: int = 30):
        self.driver.set_script_timeout(seconds + 10)
        self.driver.execute_async_script("""
            const done = arguments[arguments.length - 1];
            setTimeout(done, arguments[0] * 1000);
        """, seconds)
    
    @allure.step('Дождаться исчезновения элемента')
    def wait_element_invisible(self, locator):
        return self.wait.until(expected_conditions.invisibility_of_element_located(locator))

    
    