SHELL = /bin/bash

TARGET_BIN_NAME = bakupipe
TARGET_FOLDER = Compilaciones/Bakumapu/
TARGET_CFG_DIR = pipeline
FILES = __main__.py README.md src/*.py docs/LICENSE.md
CFG_FILES = config.yaml layout_build.yaml layout_test.yaml

# =====================================================

default: zip make_exe deploy clean

cfg_files:
	@echo "Exporting yaml files..."
	@mkdir -p $(HOME)/$(TARGET_FOLDER)/$(TARGET_CFG_DIR)
	@cd $(TARGET_CFG_DIR) && cp $(CFG_FILES) $(HOME)/$(TARGET_FOLDER)/$(TARGET_CFG_DIR)/
	@echo "Done"

zip:
	@echo "Building BakuPipe..."
	@zip $(TARGET_BIN_NAME)-TEMP.zip -r $(FILES) > /dev/null 2>&1

make_exe:
	@echo "#!/usr/bin/env python" | \
		   cat - $(TARGET_BIN_NAME)-TEMP.zip > $(TARGET_BIN_NAME)
	@chmod +x $(TARGET_BIN_NAME)
	@echo "Done"

deploy:
	@mv $(TARGET_BIN_NAME) $(HOME)/$(TARGET_FOLDER)
	@echo "Deployed to $(HOME)/$(TARGET_FOLDER)"

clean:
	@rm $(TARGET_BIN_NAME)-TEMP.zip
