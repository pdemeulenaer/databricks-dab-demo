.ONESHELL:

SHELL = /bin/bash
CONDA_ACTIVATE = source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate

conda:
	conda env create --file environment.yml --force
	$(CONDA_ACTIVATE) customer-needs-solution

install:
	pip install -r requirements.txt

pre-commit:
	pre-commit install

setup: conda install pre-commit

# run:
# 	uvicorn app.api.main:app --reload --port 8000

dev:
	pip install -e .

data_pipeline:
	python -m src.databricks_dab_demo.data_pipeline.data_pipeline	

train:
	python -m src.databricks_dab_demo.scripts.train	

black:
	black src/databricks_dab_demo

lint:
	mypy src/databricks_dab_demo
	pylint src/databricks_dab_demo

test:
	behave tests/features/

doc: 
	mkdocs build	

quality: black lint test doc

quality-ci: lint test

