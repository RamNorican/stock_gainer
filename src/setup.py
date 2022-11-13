from setuptools import setup, find_packages

with open("requirements.txt") as requirement_file:
    requirements = requirement_file.read().split()

setup(
    name="stock_scrapper",
    description="scrapes tickers from yahoo finance",
    version="1.0.0",
    author="sitaram",
    author_email="sitaram.sarma@noricangroup.com",
    install_requires=requirements,
    packages=find_packages(),
)
