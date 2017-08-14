.DEFAULT_GOAL := none

depend:
	pip install -r requirements.txt

convert:
	python setup_convert.py build

deconvert:
	python setup_deconvert.py build

none:
	@echo none: Nothing to do.
	@echo set a target name to argument
