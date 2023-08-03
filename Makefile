install: # создание или обновление виртуального окружения
	poetry install

install-dep: # установка зав-тей для деплоя
	poetry add Django
	poetry add psycopg2-binary

build: # выполнение сборки пакета
	poetry build

publish: # отладка публикации
	poetry publish --dry-run

package-install-f: # переустановка пакета в систему
	pip install --user --force-reinstall dist/*.whl

package-install: # установка пакета в систему
	python3 -m pip install --user dist/*.whl

run: # старт
	poetry run python manage.py runserver

PORT ?= 8000
start: #gunicorn
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app