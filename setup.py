from setuptools import setup, find_packages
import logging
from pathlib import Path

VERSION = '0.8.8a6'
DESCRIPTION = 'Microsoft Adaptive Cards'
LONG_DESCRIPTION = 'A package that helps you design adaptive cards in an object-oriented manner.'

current_location = Path().absolute()
logging.info(current_location)
try:
    with open("requirements.txt") as f:
        requires = f.read().split()
except Exception as e:
    print(current_location)
    raise e

setup(
    name="adaptivecard",
    version=VERSION,
    author="cabutchei (Luan Paz)",
    author_email="<luropa_paz@hotmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=requires,
    keywords=['python', 'adaptive', 'cards', 'microsoft'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License", 
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)