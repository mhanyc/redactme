
VE ?= ./ve
FLAKE8 ?= $(VE)/bin/flake8
REQUIREMENTS ?= requirements/requirements.txt
SYS_PYTHON ?= python3
PIP ?= $(VE)/bin/pip
PY_SENTINAL ?= $(VE)/sentinal
WHEEL_VERSION ?= 0.29.0
SUPPORT_DIR ?= requirements/virtualenv_support/
MAX_COMPLEXITY ?= 9
PY_DIRS ?= *.py tests 

$(PY_SENTINAL): $(REQUIREMENTS) $(SUPPORT_DIR)*
	rm -rf $(VE)
	virtualenv --python=$(SYS_PYTHON) $(VE)
	$(PIP) install -f file://$(SUPPORT_DIR) wheel==$(WHEEL_VERSION)
	$(PIP) install -f file://$(SUPPORT_DIR) --use-wheel --no-deps --requirement $(REQUIREMENTS)
	touch $@

flake8: $(PY_SENTINAL)
	$(FLAKE8) $(PY_DIRS) 

test: 
	$(VE)/bin/python -m tests.test_entity_extraction

clean:
	rm -rf ve
