APP_DIR = dayliopy

default: install install-dev

all: install install-dev fmt-check lint


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
	# Exit on fatal error code.
	pylint $(APP_DIR) || pylint-exit $$?

flake8:
	# Error on syntax errors or undefined names.
	flake8 . --select=E9,F63,F7,F82 --show-source
	# Warn on everything else.
	flake8 . --exit-zero

lint: pylint flake8

fix: fmt lint


csv:
	cd $(APP_DIR) \
		&& ./clean_csv.py

mood:
	cd $(APP_DIR) \
		&& ./mood_report.py

fit:
	cd $(APP_DIR) \
		&& ./fit_model.py

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
