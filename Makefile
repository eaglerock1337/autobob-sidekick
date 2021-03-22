all: setup compile copy
	@echo "Building AutoBob SideKick..."

setup:
	@echo "Setting up environment..."
	pip install pipenv
	pipenv install

compile:
	@echo "Compiling application with pyinstaller..."
	pipenv run pyinstaller --noconsole --onefile autobob.py

copy:
	cp dist/autobob .
	@echo "autobob executable copied to current directory!"

docker:
	docker build --tag autobob .
	docker run -it --rm autobob bash

test:
	@echo "No tests yet!"
