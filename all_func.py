import requests
from terminaltables import AsciiTable


def get_response(url, params=None, headers=None):
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()


def predict_rub_salary_for_superjob(vacancy):
    if vacancy['currency'] == 'rub':
        return get_avg_salary(vacancy['payment_from'], vacancy['payment_to'])


def predict_rub_salary_for_hhru(vacancy):
    if vacancy['salary'] and vacancy['salary']['currency'] == 'RUR':
        return get_avg_salary(vacancy['salary']['from'], vacancy['salary']['to'])


def get_avg_salary(salary_from, salary_to):
    if not salary_from:
        return salary_to * 0.8
    elif not salary_to:
        return salary_from * 1.2
    else:
        return (salary_from + salary_to) / 2


def get_table(title, lang_stat):
    table_data = [
        ['Язык программирования', 'Найдено вакансий', 'Обработано вакансий', 'Средняя зарплата']
    ]
    for lang in lang_stat:
        table_data.append(lang)
    table_instance = AsciiTable(table_data, title)
    return table_instance.table
