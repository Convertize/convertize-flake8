import sys

# if sys.version_info[:2] < (3, 6):
#     sys.exit("convertize-flake8 requires at least Python 3.6.")

from setuptools import setup

setup(
    name="convertize-flake8",
    version="0.4.0",
    description="Convertize custom flake8 checker plugin.",
    license="Apache 2.0",
    url="https://github.com/convertize/convertize-flake8",
    author="Convertize",
    author_email="dev@convertize.com.br",
    install_requires=["flake8>=3.8.0,<3.9.0"],
    package_dir={"": "src"},
    extras_require={
        "tests": [
            "pytest==6.2.2",
        ]
    },  # last 2.7 and 3.7 compat version
    py_modules=["shop_check"],
    entry_points={"flake8.extension": ["B = shop_check:ShopCheck"]},
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development",
    ],
)