all: setup compile copy
	@echo "Building AutoBob SideKick..."

setup:
	pip install pipenv
	pipenv install

compile:
	pipenv run pyinstaller --noconsole --onefile autobob.py

copy:
	cp dist/autobob .

docker:
	docker build --tag autobob .
	docker run -it --rm autobob bash

test:
	@echo "No tests yet!"