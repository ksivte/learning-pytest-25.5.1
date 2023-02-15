import pytest
from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_all_pets_are_displayed(test_show_my_pets):  # проверка, что все питомцы отображаются
    statistic = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))  # сохраняем в переменную statistic элементы статистики, явное ожидание
    pets = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))  # сохраняем в переменную pets элементы карточек питомцев, явное ожидание
    amount = statistic.text.split('\n')  # получаем количество питомцев из статистики
    amount = amount[1].split(' ')
    amount = int(amount[1])
    amount_of_pets = len(pets)  # получаем количество карточек питомцев
    assert amount == amount_of_pets  # проверка, что количество питомцев из статистики равно количеству карточек питомцев


def test_half_of_pets_have_photo(test_show_my_pets):  # проверка, что хотя бы у половины питомцев есть фото
    statistic = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))  # сохраняем в переменную statistic элементы статистики
    pytest.driver.implicitly_wait(10)  # неявное ожидание
    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')  # cохраняем в переменную images элементы с атрибутом img
    amount = statistic.text.split('\n')  # получаем количество питомцев из статистики
    amount = amount[1].split(' ')
    amount = int(amount[1])
    half = amount // 2  # половина от всего кол-ва питомцев
    amount_photos = 0  # находим количество питомцев с фото
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            amount_photos += 1
    assert amount_photos >= half  # проверка, что количество питомцев с фотографией больше или равно половине количества питомцев


def test_all_pets_have_info(test_show_my_pets):  # проверка, что у всех питомцев есть имя, возраст и порода
    pet_data = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))  # сохраняем в переменную pet_data элементы с данными о питомцах, явное ожидание
    wait = WebDriverWait(pytest.driver, 10)  # переменная явного ожидания
    for i in range(len(pet_data)):
        assert wait.until(EC.visibility_of(pet_data[i]))
    name_my_pets = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[1]')  # поиск в таблице данных имен, явное ожидание
    for i in range(len(name_my_pets)):
        assert wait.until(EC.visibility_of(name_my_pets[i]))
    type_my_pets = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[2]')  # поиск в таблице данных пород, явное ожидание
    for i in range(len(type_my_pets)):
        assert wait.until(EC.visibility_of(type_my_pets[i]))
    age_my_pets = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[3]')  # поиск в таблицы данных возраста, явное ожидание
    for i in range(len(age_my_pets)):
        assert wait.until(EC.visibility_of(age_my_pets[i]))


def test_all_pets_have_different_names(test_show_my_pets):  # проверка, что у всех питомцев разные имена
    names_my_pets = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))  # cохраняем в переменную pet_data элементы с данными о питомцах, явное ожидание
    list_names_my_pets = []  # проверка, что у всех питомцев разные имена
    for i in range(len(names_my_pets)):
        list_names_my_pets.append(names_my_pets[i].text)
    set_pet_data = set(list_names_my_pets)  # преобразовываем список в множество
    assert len(list_names_my_pets) == len(set_pet_data)  # сравниваем длину списка и множества


def test_all_pets_are_different(test_show_my_pets):  # проверка, что в списке питомцев нет повторяющихся
    data_my_pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')  # получаем в переменную data_my_pets элементы с данными о питомцах, явное ожидание
    list_data_my_pets = []  # проверка, что в списке нет повторяющихся питомцев:
    for i in range(len(data_my_pets)):
        list_data = data_my_pets[i].text.split("\n")
        list_data_my_pets.append(list_data[0])
    set_data_my_pets = set(list_data_my_pets)
    assert len(list_data_my_pets) == len(set_data_my_pets)  # сравниваем длину списка и множества

