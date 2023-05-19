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

Пример для отображения статистики для HH.ru:

```bash
$ python hhru.py
```
![img](https://github.com/Forluc/proj-delete-/assets/75582238/d34b6ee1-adec-4937-bc47-03fb86e29954)

Пример для отображения статистики для SuperJob.ru:

```bash
$ python sj.py
```

![img_1](https://github.com/Forluc/proj-delete-/assets/75582238/6eb9ada9-44a8-4a12-a023-3e9936b98674)

Пример для отображения общей статистики:

```bash
$ python app_hh_and_sj.py
```
![img_3](https://github.com/Forluc/proj-delete-/assets/75582238/be6ed6f1-5f82-4360-a0cb-ee56a786e036)

## Цель проекта
Код был написан для удобства просмотра статистики вакансий HH.ru и SuperJob.ru
