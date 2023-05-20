# Статистика вакансий программистов в Москве(SuperJob и HH.ru)
Скрипт, показывающий статистику по языкам программирования в виде таблицы.

Статистика по: 'Java', 'Python', 'Javascript', 'C#', 'C++', 'PHP', 'GO'

## Окружение

- Создайте файл ```.env``` в основном каталоге

### Требования к установке

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

```bash
pip install -r requirements.txt
``` 

### Получение Secret key для доступа ко всем методам [API SuperJob](https://api.superjob.ru/)

1. [Зарегистрировать](https://api.superjob.ru/register) приложение(ссылку на сайт можно указать любую)
2. Прописать в файле переменную SUPERJOB_SECRET_KEY со значением полученного ключа на сайте [SuperJob](https://api.superjob.ru/register)
3. .env содержит данные без кавычек

## Запуск скрипта для просмотра статистики

#### Запуск на Linux(Python 3) или Windows:

Пример для отображения общей статистики:

```bash
$ python app_hh_and_sj.py
```

![img_3](https://github.com/Forluc/Stats_hhru_superjob/assets/75582238/a1fd39b9-027b-495f-9c0e-6ecc4876f602)

## Цель проекта
Код был написан для удобства просмотра статистики вакансий [HH.ru](https://hh.ru/) и [SuperJob.ru](https://www.superjob.ru/)
