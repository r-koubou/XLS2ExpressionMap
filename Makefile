.DEFAULT_GOAL := none

PREFIX=XLS2ExpressionMap
WORKDIR=build
DMG_DISKID=disk4

depend:
	pip install -r requirements.txt

convert:
	python setup_convert_gui.py bdist_mac

dmg: convert
	$(eval APP := $(shell ls ./build/ | grep app))
	$(eval VOL := $(shell basename $(APP)))
	@echo -----------------------------------------------
	@echo Create a dmg file
	@echo -----------------------------------------------
	hdiutil create -size 50m -type UDIF -fs HFS+ -volname "$(VOL)" -layout NONE $(WORKDIR)/src.dmg
	hdid $(WORKDIR)/src.dmg
	ditto -rsrcFork $(WORKDIR)/$(APP)          	"/Volumes/$(VOL)/$(PREFIX).app"
	ditto -rsrcFork LICENSE						"/Volumes/$(VOL)/"
	ditto -rsrcFork NOTICE						"/Volumes/$(VOL)/"
	ditto -rsrcFork $(WORKDIR)/Applications 	"/Volumes/$(VOL)/"

	hdiutil eject $(DMG_DISKID)
	hdiutil convert -format UDZO -o $(WORKDIR)/$(VOL).dmg $(WORKDIR)/src.dmg

deconvert:
	python setup_deconvert.py build

none:
	@echo none: Nothing to do.
	@echo set a target name to argument
