SHELL = /bin/bash
APP_DIR = dayliopy
export PYTHONPATH


default: install install-dev

all: install install-dev fmt-check lint typecheck


h help:
	@grep '^[a-z]' Makefile


install:
	pip install pip --upgrade
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

upgrade:
	pip install pip --upgrade
	pip install -r requirements.txt --upgrade
	pip install -r requirements-dev.txt --upgrade


fmt:
	black .
	isort .

fmt-check:
	black . --diff --check
	isort . --diff --check-only

pylint:
	pylint $(APP_DIR) || pylint-exit $$?

flake8:
	flake8 . --select=E9,F63,F7,F82 --show-source
	flake8 . --exit-zero

lint: pylint flake8

fix: fmt lint

t typecheck:
	mypy $(APP_DIR)


csv:
	python -m $(APP_DIR).clean_csv

mood:
	python -m $(APP_DIR).mood_report

fit:
	python -m $(APP_DIR).fit_model

process: csv mood fit


db:
	cd $(APP_DIR) \
		&& sqlite3 var/data_out/db.sqlite < ../tools/setup_db.sql

schema:
	cd $(APP_DIR) \
		&& sqlite3 var/data_out/db.sqlite '.schema'

interactive:
	cd $(APP_DIR) \
		&& sqlite3 var/data_out/db.sqlite


container:
	docker build -t dayliopy .
	docker run --rm \
		-v "$(PWD)/dayliopy/var:/usr/src/app/dayliopy/var/" \
		dayliopy
