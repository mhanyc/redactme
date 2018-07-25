
VE ?= ./ve
FLAKE8 ?= $(VE)/bin/flake8
REQUIREMENTS ?= requirements/requirements.txt
SYS_PYTHON ?= python3
PIP ?= $(VE)/bin/pip
WHEEL_VERSION ?= 0.31.1
SUPPORT_DIR ?= requirements/virtualenv_support/
MAX_COMPLEXITY ?= 9
PY_DIRS ?= *.py tests 

create: $(REQUIREMENTS) $(SUPPORT_DIR)*
	rm -rf $(VE)
	python3 -m venv $(VE)
	$(PIP) install wheel==$(WHEEL_VERSION)
	$(PIP) install --use-wheel --requirement $(REQUIREMENTS)
	touch $@

flake8: 
	$(FLAKE8) $(PY_DIRS) 

test: 
	$(VE)/bin/python -m tests.test_entity_extraction

clean:
	rm -rf ve
