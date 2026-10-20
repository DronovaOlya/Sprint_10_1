from selenium.webdriver.common.by import By

class MainPageLocators:
    
    LOCATOR_INPUT_FROM = By.XPATH,".//input[@id='from']"

    LOCATOR_INPUT_TO = By.XPATH,".//input[@id='to']"

    LOCATOR_POINT_A = By.XPATH, "//ymaps[contains(@class, 'route-pin__label-a')]"

    LOCATOR_POINT_B = By.XPATH, "//ymaps[contains(@class, 'route-pin__label-b')]"

    LOCATOR_BLOCK_ROUTE = By.XPATH, './/div[@class="type-picker shown"]'

    LOCATOR_BLOCK_AUTO_FREE = By.XPATH, ".//div[@class='text' and text()='Авто Бесплатно']"

    LOCATOR_BLOCK_ZERO_MINUTES = By.XPATH, ".//div[@class='duration' and text()='В пути 0 мин.']"

    LOCATOR_TYPE_OPTIMAL = By.XPATH, "//div[contains(@class, 'mode') and text()='Оптимальный']"

    LOCATOR_TYPE_FAST= By.XPATH, ".//div[@class='mode' and text()='Быстрый']"

    LOCATOR_COST = By.XPATH,".//div[@class='text']"

    LOCATOR_TIME = By.XPATH,".//div[@class='duration']"

    LOCATOR_TYPE_MINE = By.XPATH, ".//div[@class='mode' and text()='Свой']"
    
    LOCATOR_TYPES_CONTAINER = (By.CSS_SELECTOR, ".types-container")

    LOCATOR_BUTTON_ORDER_TAXI = By.XPATH, ".//button[@class='button round' and text()='Вызвать такси']"

    LOCATOR_BUTTON_DRIVE = By.XPATH,".//div[@class='type drive']"

    LOCATOR_BUTTON_TO_BOOK = By.XPATH, ".//button[@class='button round' and text()='Забронировать']"

    LOCATOR_TARIFF_CARDS = By.CSS_SELECTOR, ".tariff-cards > .tcard"

    LOCATOR_ACTIVE_TARIFF = By.XPATH, "//div[contains(@class, 'tariff-cards')]//div[contains(@class, 'tcard') and contains(@class, 'active')]"

    LOCATOR_TEXT_DESCRIPTION_TARIFF= By.XPATH, ".//div[contains(@class, 'i-dPrefix') and text()='{}']"
    
    LOCATOR_ICONS_I = By.XPATH, "//*[@data-for='tariff-card-{}']"
    
    LOCATOR_TARIFF_CARD = By.CSS_SELECTOR, ".tariff-cards > .tcard:nth-child({})"

    LOCATOR_INPUT_PHONE = By.XPATH, ".//div[@class='np-text' and text()='Телефон']"

    LOCATOR_INPUT_PAYMENT_METHOD = By.XPATH, ".//div[@class='pp-text' and text()='Способ оплаты']"

    LOCATOR_INPUT_COMMENT = By.ID, "comment"

    LOCATOR_INPUT_ORDER_REQUIREMENTS = By.XPATH, ".//div[@class='reqs-head' and text()='Требования к заказу']"

    LOCATOR_ENTER_NUMBER_AND_ORDER = By.XPATH, "//button[contains(@class, 'smart-button')][contains(., 'Ввести номер и заказать')]"

    LOCATOR_MACHINE_SEARCH = By.XPATH, ".//div[@class='order-header-title' and text()='Поиск машины']"

    LOCATOR_TIMER = By.XPATH, ".//div[@class='order-header-time']"

    LOCATOR_BUTTON_DETAILS = By.XPATH, "//div[contains(@class, 'order-btn-group')]" "[.//button[contains(@class, 'order-button')] and .//div[text()='Детали']]"
 
    LOCATOR_BUTTON_CANCEL= By.XPATH, "//div[contains(@class, 'order-btn-group')]" "[.//button[contains(@class, 'order-button')] and .//div[text()='Отменить']]"

    LOCATOR_TIME_N = By.XPATH, ".//div[@class='order-header-title' and text()=' мин. и приедет']"

    LOCATOR_NUMBER_CAR_IMAGE= By.XPATH, "//div[contains(@class, 'order-number')]" "[.//div[contains(@class, 'number')] and .//img[@alt='Car']]"

    LOCATOR_BLOCK_DRIVER= By.XPATH, "//div[contains(@class, 'order-btn-group')]" "[.//div[contains(@class, 'order-btn-rating')] " "and .//img[@alt='close'] " "and .//div[not(@class)]]"

    LOCATOR_TAXI_FARE = By.XPATH,".//div[@class='tcard-price']"

    LOCATOR_TAXI_FARE_DETAILS = By.XPATH,"//div[contains(@class, 'o-d-sh')][contains(text(), 'Стоимость')]"

    LOCATOR_ORDER_WINDOW = By.XPATH,".//div[@class='order-body']"

    