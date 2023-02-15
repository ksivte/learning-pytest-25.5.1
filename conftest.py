from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('./chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')
    yield
    pytest.driver.quit()

@pytest.fixture()
def test_show_my_pets():  # переход на главную страницу пользователя
    # Вводим email
    pytest.driver.find_element(By.ID, 'email').send_keys('здесь указать корректный email')  # здесь указать корректный email
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'pass').send_keys('здесь указать корректный пароль')  # здесь указать корректный пароль
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()  # нажимаем на кнопку входа в аккаунт
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"  # проверяем, что мы оказались на главной странице пользователя
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы")))
    element.click()  # нажимаем на ссылку "Мои питомцы"
    assert pytest.driver.find_element(By.TAG_NAME, 'h2').text == "здесь указать имя текущего пользоваля в системе"  # проверка, что имя пользователя на странице соответствует текущему
