ENV := $(CURDIR)/env
PIP := $(ENV)/bin/pip
PIP_DEV := $(PIP) install -r requirements/dev.txt

test: $(ENV)/bin/coverage
	$(ENV)/bin/coverage run -m unittest discover
	$(ENV)/bin/coverage report
	$(ENV)/bin/coverage html

test-watch: $(ENV)/bin/sniffer
	$(ENV)/bin/sniffer

shell: $(ENV)/bin/bpython
	$(ENV)/bin/bpython

black: $(ENV)/bin/black
	$(ENV)/bin/black solutions tests

clean:
	rm -rf $(ENV) htmlcov
	find . -name __pycache__ -type d -prune -exec rm -rf {} \;

$(ENV)/bin/coverage: $(PIP)
	$(PIP) install -r requirements/base.txt

$(ENV)/bin/bpython: $(PIP)
	$(PIP_DEV)

$(ENV)/bin/sniffer: $(PIP)
	$(PIP_DEV)

$(ENV)/bin/black: $(PIP)
	$(PIP_DEV)

$(PIP):
	python -m venv $(ENV)
	$(PIP) install pip --upgrade
	$(PIP) install -r requirements/base.txt
