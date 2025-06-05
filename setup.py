from setuptools import setup, find_packages

from src.candlestick_to_csv import __version__

setup(
    name='candlestick_to_csv',
    version=__version__,

    url='https://github.com/KianML/candlestick_to_csv',
    author='Kianoosh Keshavarzian',
    author_email='kshvzn@gmail.com',
    install_requires=['PIL', 'datetime', 'matplotlib', 'numpy, 'pandas', 'collections', 'pytesseract'],
)
