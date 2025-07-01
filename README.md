# RandQuestions

Простой веб-приложение на Flask для отображения случайных вопросов и ответов из файла `questions.txt`.  
Поддерживает вывод случайного набора вопросов и полный список вопросов с ответами с удобным UI.

---

## Возможности

- Отображение случайных вопросов (по умолчанию 10)
- Вывод всех вопросов с ответами с возможностью раскрытия/скрытия ответов
- REST API для получения вопросов в формате JSON

---

## Установка и запуск

1. Клонируйте репозиторий:

```bash
git clone https://github.com/yourusername/RandQuestions.git
cd RandQuestions

2. Создайте виртуальное окружение(рекомендуется)

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. Установите зависимости

pip install -r requirements.txt

4.Запустите приложение

python Main.py

5. Откройте в браузере:

Главная страница со случайными вопросами: http://127.0.0.1:5000/

Все вопросы с ответами: http://127.0.0.1:5000/all

REST API:

Случайные вопросы (JSON): http://127.0.0.1:5000/api/questions

Все вопросы (JSON): http://127.0.0.1:5000/api/questions/all
