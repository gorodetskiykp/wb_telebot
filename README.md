# wb_telebot

## git
- git clone https://github.com/gorodetskiykp/wb_telebot.git
- git fetch origin - забрать всю информацию про изменения в удаленном репозитории
- git fetch --prune - дополнительно удаляет мусорные ветки 
- git pull - забрать все изменения
- git checkout 1-add-project-structure - переключится на ветку
- git checkout -b new_branch - создание локальной ветки
- git branch - посмотреть все ветки
- git rebase main
- git stash / git stash apply

## SKILLS
- SMART - задачи и цели
- CI/CD - devOps
- Аренда VDS - выделенный сервер (linux)
- SSH - защищенный канад передачи данных

## PIP
- pip freeze - список установленных пакетов
- pip install lib_name
- pip freeze > requirements.txt
- pip install -r requirements.txt 

## VENV
- python -m venv venv
- source venv/bin/activate
- venv\Scripts\activate (WIN)
- source venv/bin/deactivate

## linux
- ls -la - посмотреть файлы в текущем каталоге
- history - посмотреть историю команд
- history | grep ФИЛЬТР
- history | grep python
- !343 - выполнить 343-ю команду из истории

## Установка и запуск бота
1. python -n venv venv
2. venv\Scripts\activate или source venv/bin/activate
3. pip install -r requirements.txt 
4. Получить токен в BotFather
5. Создать в корне проекта файл creds.py
6. Создать в creds.py константу TELE_TOKEN = "наш телеграм-токен"
7. Запустить бота: python main.py
