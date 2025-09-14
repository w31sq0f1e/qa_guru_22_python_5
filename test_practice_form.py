import pytest
from selene import browser, be, have
import os

def test_fill_forms(browser_config):
    browser.open("/automation-practice-form")

    #Фамилия, имя. маил, номер телефона
    browser.element("#firstName").type("Test")
    browser.element("#lastName").type("Testoviy")
    browser.element("#userEmail").type("testoviytest9990@mail.ru")
    browser.element("#userNumber").type("9990001122")

    # Гендер
    browser.element('label[for="gender-radio-1"]').click() #Male

    # Хобби
    browser.element('label[for="hobbies-checkbox-1"]').click() # Спорт
    browser.element('label[for="hobbies-checkbox-3"]').click() # Музыка

    #Дата рождения
    browser.element('#dateOfBirthInput').click()

    browser.element('.react-datepicker__month-select').click() #Месяц
    browser.element('.react-datepicker__month-select [value = "6"]').click()

    browser.element('.react-datepicker__year-select').click() #Год
    browser.element('.react-datepicker__year-select [value = "2002"]').click()

    browser.element('.react-datepicker__day--011:not(.react-datepicker__day--outside-month)').click() #День

    #Subject
    browser.element('#subjectsInput').type("Eng").press_enter() # Проверка выбора значения через enter

    browser.element('#subjectsInput').type("C") # Проверка выбора значения при клике из выпадающего списка
    browser.element('.subjects-auto-complete__menu').should(be.visible)
    browser.all('.subjects-auto-complete__option').element_by(have.exact_text('Computer Science')).click()
    browser.all('.subjects-auto-complete__multi-value__label').element_by(have.exact_text('Computer Science')).should(be.visible)

    #Загрузка фото
    browser.element('#uploadPicture').type(os.path.abspath('IMG_8683.PNG'))

    #Адрес
    browser.element("#currentAddress").type("Тестовый")

    #StateCyty
    browser.element('#state').click()
    browser.element('#react-select-3-input').type('NCR').press_enter()

    #City
    browser.element('#city').click()
    browser.element('#react-select-4-input').type('Noida').press_enter()

    #Submit
    browser.element('#submit').click()

    #Плашка
    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))

    #Данные в таблице
    browser.element('.table-responsive').all('td').should(have.texts(
            'Student Name', 'Test Testoviy',
            'Student Email', 'testoviytest9990@mail.ru',
            'Gender', 'Male',
            'Mobile', '9990001122',
            'Date of Birth', "11 July,2002",
            'Subjects', 'English, Computer Science',
            'Hobbies', 'Sports, Music',
            'Picture', 'IMG_8683.PNG',
            'Address', 'Тестовый',
            'State and City', 'NCR Noida'))

    browser.element('#closeLargeModal').click()








