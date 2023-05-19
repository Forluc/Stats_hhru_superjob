import requests
from terminaltables import AsciiTable


def get_response(url, params=None, headers=None):
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()


def predict_rub_salary_for_superJob(vacancy):
    if vacancy['currency'] == 'rub':
        if vacancy['payment_from'] and vacancy['payment_to']:
            return (vacancy['payment_from'] + vacancy['payment_to']) / 2
        elif not vacancy['payment_from']:
            return vacancy['payment_to'] * 0.8
        elif not vacancy['payment_to']:
            return vacancy['payment_from'] * 1.2


def predict_rub_salary_for_hhru(vacancy):
    if vacancy['salary'] and vacancy['salary']['currency'] == 'RUR':
        if vacancy['salary']['from'] and vacancy['salary']['to']:
            return (vacancy['salary']['from'] + vacancy['salary']['to']) / 2
        elif not vacancy['salary']['from']:
            return vacancy['salary']['to'] * 0.8
        elif not vacancy['salary']['to']:
            return vacancy['salary']['from'] * 1.2


def get_table(title, lang_stat):
    table_data = [
        ['Язык программирования', 'Найдено вакансий', 'Обработано вакансий', 'Средняя зарплата']
    ]
    for lang in lang_stat:
        table_data.append(lang)
    table_instance = AsciiTable(table_data, title)
    print(table_instance.table)
