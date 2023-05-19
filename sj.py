import os
import all_func

from dotenv import load_dotenv


def get_statistics_sj(sj_secret_key, language, page=0):
    salaries = []
    more = True
    while more:
        url = '	https://api.superjob.ru/2.0/vacancies/'
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

        salaries_vacancies = [all_func.predict_rub_salary_for_superJob(vacancy) for vacancy in vacancies]
        salaries.extend(salaries_vacancies)

        is_salaries = list(filter(lambda x: x is not None, salaries))
        vacancies_processed = len(is_salaries)

        if vacancies_processed:
            avg_salary = sum(is_salaries) // vacancies_processed
        else:
            avg_salary = 0

        page += 1
        more = response['more']

    return [language, vacancies_found, vacancies_processed, avg_salary]


def main():
    load_dotenv()
    sj_secret_key = os.environ['SUPERJOB_SECRET_KEY']

    prog_names = ['Java', 'Python', 'Javascript', 'C#', 'C++', 'PHP', 'GO']  # Можно поменять на другие языки
    statistics = []

    for name in prog_names:
        statistics.append(get_statistics_sj(sj_secret_key, name))

    all_func.get_table('SuperJob Moscow', statistics)


if __name__ == '__main__':
    main()
