from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="zambia_geo",
    version="0.1.0",
    author="Peter Sangwani Zyambo",
    author_email="zyambopeter1@gmail.com",
    description="A Python package containing Zambian provinces and cities data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sangwani-coder/zambia-geo",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)