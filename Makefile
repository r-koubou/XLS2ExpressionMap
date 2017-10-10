.DEFAULT_GOAL := none

depend:
	pip3 install -r requirements.txt

convert_mac:
	python3 setup_convert_gui.py bdist_mac

convert_win32:
	python3 setup_convert_gui.py build

deconvert:
	python3 setup_deconvert.py build

none:
	@echo none: Nothing to do.
	@echo set a target name to argument
