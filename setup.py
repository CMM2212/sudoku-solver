from setuptools import setup

setup(name='sudoku_solver',
      version='1.0',
      description='A sudoku solving algorithm with a PyQt5 GUI.',
      url='https://github.com/CMM2212/sudoku-solver',
      license='cc0',
      packages=['sudoku_solver'],
      install_requires=['PyQt5'],
      entry_points={'console_scripts': ['sudoku-solver=sudoku_solver.__main__:main']})
