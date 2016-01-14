"""Goodness of fit metrics for comparing two 1D numpy.ndarrays."""
from __future__ import absolute_import

from .metrics import nash_sutcliffe, r_squared, rmsd, avg_pc_err, \
    integ_sq_errors, integ_weighted_sq_errors

import sys
import os
import nose


def run_nose(verbose=False):
    nose_argv = sys.argv
    nose_argv += ['--detailed-errors', '--exe']
    if verbose:
        nose_argv.append('-v')
    initial_dir = os.getcwd()
    my_package_file = os.path.abspath(__file__)
    my_package_dir = os.path.dirname(my_package_file)
    os.chdir(my_package_dir)
    try:
        nose.run(argv=nose_argv)
    finally:
        os.chdir(initial_dir)
