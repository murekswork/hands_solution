Для клонирования репозитория и установки venv ввести команды:
```
git clone https://github.com/murekswork/hands_solution
cd hands_solution
python3 -m venv _venv && source _venv/bin/activate && pip install -r requirements.txt 
```

Для использования api парсинга номеров ввести команду в корневой директории (на уровне main.py):

```
uvicorn --factory main:create_app --reload
```

Далее в браузере перейти по адресу http://127.0.0.1:8000/docs/ 
Список сайтов вставлять в формате
```
[
  "https://hands.ru/company/about",
  "https://hands.ru/company/about",
  "https://krasnodar.hh.ru/"
]
```

