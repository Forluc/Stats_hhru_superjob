import all_func


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
        vacancies_language = response['items']
        vacancies_found = response['found']

        salaries_vacancies = [all_func.predict_rub_salary_for_hhru(vacancy) for vacancy in vacancies_language]
        salaries.extend(salaries_vacancies)

        is_salaries = list(filter(lambda x: x is not None, salaries))

        vacancies_processed = len(is_salaries)
        if vacancies_processed:
            avg_salary = int(sum(is_salaries) // vacancies_processed)
        else:
            avg_salary = 0

        page += 1

    return [language, vacancies_found, vacancies_processed, avg_salary]


def main():
    prog_names = ['Java', 'Python', 'Javascript', 'C#', 'C++', 'PHP', 'GO']  # Можно поменять на другие языки
    statistics = []

    for name in prog_names:
        statistics.append(get_statistics_hh(language=name))

    all_func.get_table('HeadHunter Moscow', statistics)


if __name__ == '__main__':
    main()
