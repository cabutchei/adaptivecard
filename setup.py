from setuptools import setup, find_packages

VERSION = '0.8.5-alpha'
DESCRIPTION = 'Microsoft Adaptive Cards'
LONG_DESCRIPTION = 'A package that helps you design adaptive cards in an object-oriented manner.'

setup(
    name="adaptivecard",
    version=VERSION,
    author="cabutchei (Luan Paz)",
    author_email="<luropa_paz@hotmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        'tabulate'
    ],
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