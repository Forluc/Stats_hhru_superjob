import os
import all_func

from dotenv import load_dotenv


def get_statistics_sj(sj_secret_key, language, page=0):
    salaries = []
    more = True
    while more:
        url = 'https://api.superjob.ru/2.0/vacancies/'
        headers = {
            'X-Api-App-Id': sj_secret_key,
        }
        params = {
            'town': 4,  # ID Москвы
            'catalogues': 48,  # Программисты
            'count': 100,  # Количество вакансий на странице
            'page': page,
            'keyword': language
        }
        response = all_func.get_response(url, headers=headers, params=params)

        vacancies = response['objects']
        vacancies_found = response['total']

        vacancies_salaries = [all_func.predict_rub_salary_for_superjob(vacancy) for vacancy in vacancies]
        salaries.extend(vacancies_salaries)

        page += 1
        more = response['more']

    data_with_salary = list(filter(lambda x: x is not None, salaries))
    vacancies_processed = len(data_with_salary)

    avg_salary = all_func.get_avg_salaries(vacancies_processed, data_with_salary)

    return [language, vacancies_found, vacancies_processed, avg_salary]


def get_statistics_hh(language, page=0):
    salaries = []
    number_pages = 1

    while page < number_pages:
        params = {
            'text': language,
            'area': 1,  # ID Москвы
            'professional_role': 96,  # Программисты
            'page': page,
            'only_with_salary': True,
            'per_page': 100  # Количество вакансий на странице
        }

        response = all_func.get_response('https://api.hh.ru/vacancies', params=params)

        number_pages = response['pages']
        language_vacancies = response['items']
        vacancies_found = response['found']

        vacancies_salaries = [all_func.predict_rub_salary_for_hhru(vacancy) for vacancy in language_vacancies]
        salaries.extend(vacancies_salaries)

        page += 1

    data_with_salary = list(filter(lambda x: x is not None, salaries))
    vacancies_processed = len(data_with_salary)

    avg_salary = all_func.get_avg_salaries(vacancies_processed, data_with_salary)

    return [language, vacancies_found, vacancies_processed, avg_salary]


def main():
    load_dotenv()
    sj_secret_key = os.environ['SUPERJOB_SECRET_KEY']

    prog_names = ['Java', 'Python', 'Javascript', 'C#', 'C++', 'PHP', 'GO']  # Можно поменять на другие языки
    hh_statistics = []
    sj_statistics = []

    for name in prog_names:
        sj_statistics.append(get_statistics_sj(sj_secret_key, name))
        hh_statistics.append(get_statistics_hh(name))

    print(all_func.get_table('HeadHunter Moscow', hh_statistics))
    print(all_func.get_table('SuperJob Moscow', sj_statistics))


if __name__ == '__main__':
    main()
