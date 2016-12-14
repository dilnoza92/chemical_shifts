===============================
final_project
===============================


.. image:: https://img.shields.io/pypi/v/final_project.svg
        :target: https://pypi.python.org/pypi/final_project

.. image:: https://img.shields.io/travis/dilnoza92/final_project.svg
        :target: https://travis-ci.org/dilnoza92/final_project

.. image:: https://readthedocs.org/projects/final-project/badge/?version=latest
        :target: https://final-project.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/dilnoza92/final_project/shield.svg
     :target: https://pyup.io/repos/github/dilnoza92/final_project/
     :alt: Updates
.. image:: https://coveralls.io/repos/github/dilnoza92/chemical_shifts/badge.svg?branch=master
:target: https://coveralls.io/github/dilnoza92/schrodinger?branch=master



How to run the code with inputs given in the terminal
--------
This package genereates a 2d NOESY spectrum of plumed chemical shifts. In this example cs-cs-100.dat in final_project folder has the plumed outputs. The package computes NOEs and makes a plot of it and save it as final_project.png. Another file that is needed is called COLVARN_outputs has the labels of atoms from which the NOEs are computed. The package is parallelized for faster calculations.
The scatter plot of 2D NOESY spectrum for N atoms of Villin protein is given below:

.. image:: https://github.com/dilnoza92/chemical_shifts/blob/master/final_project_scatter_plot.png

The plot with gaussian added to the NOESY peaks is shown below:

.. image:: https://github.com/dilnoza92/chemical_shifts/blob/master/final_project_gaussian.png



.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

