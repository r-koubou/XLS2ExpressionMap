.DEFAULT_GOAL := none

depend:
	pip3 install -r requirements.txt

convert:
	python3 setup_convert.py build

deconvert:
	python3 setup_deconvert.py build

none:
	@echo none: Nothing to do.
	@echo set a target name to argument
