from selenium.webdriver.common.by import By

class RegistrationPage:
    NAME_INPUT = (By.XPATH, '//label[text()="Имя"]/following-sibling::input') #поле ввода имени
    EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input') #поле ввода емейла
    PASSWORD_INPUT = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input') #поле ввода пароля
    REG_LINK = (By.CSS_SELECTOR, 'a[href="/register"]') #ссылка на страницу регистрации
    REG_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]') #кнопка Зарегистрироваться
    SIGNIN_PAGE = (By.XPATH, '//h2[text()="Вход"]') #страница входа
    PASSWORD_ERROR = (By.XPATH, '//p[@class="input__error text_type_main-default"]')  # ошибка пароля
class MainPage:
    LK_BUTTON = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]') #кнопка Личный кабинет
    MY_LOGIN = (By.XPATH, '//input[@name="name"]') #заполненное поле емейла в ЛК
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") #Кнопка на главной Войти в аккаунт
    HAVE_LOGIN = (By.CSS_SELECTOR, 'a[href="/login"]') #Кнопка Войти если есть аккаунт

    NAME_INPUT = (By.NAME, 'name') #поле логина
    PASSWORD_INPUT = (By.NAME, 'Пароль') #поле пароля
    BUTTON_SIGN_IN = (By.XPATH, "//button[contains(text(),'Войти')]")  # Кнопка Войти в форме логина
    BUTTON_EXIT = (By.XPATH, "//button[text()='Выход']") #Кнопка Выход в ЛК

    BURGER_LOGO = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2') #Логотип в шапке
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[contains(text(),'Конструктор')]") #Ссылка Конструктор
    TEXT_CONSTRUCTOR = (By.XPATH, '//h1[contains(text(),"Соберите бургер")]') #текст "Собери бургер" на главной

    SAUCES = (By.XPATH, '//div[contains(@class, "tab_tab__1SPyG")]/span[text()="Соусы"]/parent::div') #раздел Соусы
    FILLING = (By.XPATH, '//div[contains(@class, "tab_tab__1SPyG")]/span[text()="Начинки"]/parent::div') #раздел Начинки
    BREAD = (By.XPATH, '//div[contains(@class, "tab_tab__1SPyG")]/span[text()="Булки"]/parent::div') #раздел Булки
