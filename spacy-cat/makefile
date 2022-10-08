.PHONY: install

clean:
	rm -rf model metrics.json

install:
	pyenv install
	pipenv install --python $$(cat .python-version)

train:
	pipenv run python3 src/trainModel.py
	pipenv run python3 -m spacy train spacyConfig.cfg --paths.train ./model/train.spacy  --paths.dev ./model/dev.spacy --output model/textcat_model

run:
	pipenv run python3 src/classifyData.py

retrain:
	make clean
	pipenv run python3 src/appendData.py
	make train