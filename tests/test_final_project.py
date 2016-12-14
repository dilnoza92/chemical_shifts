#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_final_project
----------------------------------

Tests for `final_project` module.
"""


import sys
import unittest
from contextlib import contextmanager
from final_project import final_project

class TestFinal_project(unittest.TestCase):


    def test_empty_arrays(self):
        self.assertEqual(len(final_project.empty_arrays(3)), 3)
        pass

    def test_number_arrays(self):
        self.assertNotEqual(len(final_project.noe_results),0)
        pass
    def test_variables(self):
        string=final_project.variables(final_project.colvar_file)
        self.assertTrue(isinstance(string[0],str))
        
    def test_chemical_shifts(self):
        self.assertTrue(isinstance(float(final_project.shiftss[3]),float))
        pass
    def test_total_atom(self):
        self.assertTrue(isinstance(final_project.new_variables[0],str))
        self.assertEqual(len(final_project.variable_averagenoe[0]),3)
        pass
    def atoms_distances(self):
        self.assertEqual(len(final_project.x_H),len(final_project.intense))
        pass
    def test_gaus(self):
        self.assertEqual(len(final_project.ZZ[0]),final_project.N_atoms)

        pass
