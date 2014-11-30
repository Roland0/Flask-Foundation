.PHONY: docs test

help:
	@echo "  env         create a development environment using virtualenv"
	@echo "  deps        install dependencies using pip"
	@echo "  clean       remove unwanted files like .pyc's"
	@echo "  lint        check style with flake8"
	@echo "  test        run all your tests using py.test"

env:
	virtualenv env && \
	. env/bin/activate && \
	make deps

deps:
	pip install -r requirements.txt

clean:
	find . -name '*.pyc' -exec rm -vf {} \;
	find . -name '*.pyo' -exec rm -vf {} \;
	find . -name '*~' -exec rm -vf {} \;

lint:
	flake8 --exclude=env .

test:
	py.test tests
