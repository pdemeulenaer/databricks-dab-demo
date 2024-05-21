"""
setup.py configuration script describing how to build and package this project.

This file is primarily used by the setuptools library and typically should not
be executed directly. See README.md for how to deploy, test, and run
the dab_default_python_test project.
"""
from setuptools import setup, find_packages

import sys
sys.path.append('./src')

import datetime
import databricks_dab_demo

setup(
    name="databricks_dab_demo",
    # We use timestamp as Local version identifier (https://peps.python.org/pep-0440/#local-version-identifiers.)
    # to ensure that changes to wheel package are picked up when used on all-purpose clusters
    version=databricks_dab_demo.__version__ + "+" + datetime.datetime.utcnow().strftime("%Y%m%d.%H%M%S"),
    url="https://databricks.com",
    author="Northell",
    author_email="pdemeulenaer@gmail.com",
    description="wheel file based on databricks-dab-demo/src",
    packages=find_packages(where='./src'),
    package_dir={'': 'src'},
    entry_points={
        "packages": [
            "data_pipeline=databricks_dab_demo.data_pipeline.data_pipeline:main",
            "train=databricks_dab_demo.scripts.train:main"            
        ]
    },
    install_requires=[
        # Dependencies in case the output wheel file is used as a library dependency.
        # For defining dependencies, when this package is used in Databricks, see:
        # https://docs.databricks.com/dev-tools/bundles/library-dependencies.html
        "setuptools"
    ],
    # package_data={'global_toolkit': ['**/*.yaml']},
    package_data={'': ['*.yaml', '*.csv', '*.pkl']},  # Include all YAML files in the package
    include_package_data=True,       # Include package data specified by package_data
)
