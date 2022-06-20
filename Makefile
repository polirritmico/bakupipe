SHELL = /bin/bash

TARGET_BIN_NAME = bakupipe
TARGET_FOLDER = Compilaciones/Bakumapu/
TARGET_CFG_DIR = pipeline
FILES = __main__.py README.md src/*.py docs/LICENSE.md
CFG_FILES = config.yaml layout_build.yaml layout_test.yaml

# Style codes
GREEN = \033[0;32m
ORANGE = \033[0;33m
ITLC = \033[3m
NS = \033[0m
DONE = $(GREEN)Done

# =====================================================

default: zip make_exe deploy clean

zip:
	@echo -e "$(ORANGE)Building BakuPipe...$(NS)"
	@zip $(TARGET_BIN_NAME)-TEMP.zip -r $(FILES) > /dev/null 2>&1

make_exe:
	@echo "#!/usr/bin/env python" | \
		   cat - $(TARGET_BIN_NAME)-TEMP.zip > $(TARGET_BIN_NAME)
	@chmod +x $(TARGET_BIN_NAME)
	@echo -e "$(DONE)$(NS)"

deploy:
	@mv $(TARGET_BIN_NAME) $(HOME)/$(TARGET_FOLDER)
	@echo -e "$(GREEN)Deployed to $(ORANGE)$(HOME)/$(TARGET_FOLDER)$(NS)"
	@echo -e "$(ITLC)Maybe 'make cfg_files' is also needed.$(NS)"

clean:
	@rm $(TARGET_BIN_NAME)-TEMP.zip
	@echo -e "$(DONE)$(NS)"


config:
	@echo -e "$(ORANGE)Exporting yaml files...$(NS)"
	@mkdir -p $(HOME)/$(TARGET_FOLDER)/$(TARGET_CFG_DIR)
	@cd $(TARGET_CFG_DIR) && cp $(CFG_FILES) $(HOME)/$(TARGET_FOLDER)/$(TARGET_CFG_DIR)/
	@echo -e "$(DONE)$(NS)"


version:
	@echo "Updating subversion ..."
	@sed -ri 's/(__version__ = )"([0-9])\.(.*)\"/echo "\1\\"\2.$$((\3+1))\\""/ge' src/bakupipe.py
	@sed -nr 's/__version__ = "([0-9]\..*)"/Updated to version: \1/p' src/bakupipe.py
	@echo -e "$(DONE)$(NS)"

