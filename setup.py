from setuptools import setup,find_packages

setup(name="census_income",
        version="0.0.1",
        author="Vasanth",
        author_email="vrajuap@gmail.com",
        packages=find_packages(),
        install_requirements=["numpy","pandas","flask"]
        )