from __future__ import absolute_import, division

import numpy as np
from nose.tools import raises

from .metrics import _check_comparable, nash_sutcliffe, r_squared, \
    rmsd, avg_pc_err, integ_sq_errors, integ_weighted_sq_errors

metric_names = ('nash_sutcliffe', 'r_squared', 'rmsd', 'avg_pc_err',
                'integ_sq_errors', 'integ_weighted_sq_errors')
neg_vec = np.random.rand(10) - 4
zero_vec = np.zeros(10, dtype=np.float)
ones_vec = np.ones(10, dtype=np.float)
asc_vec = np.linspace(3, 33, 10)
desc_vec = asc_vec[::-1]


def test__check_comparable_same_shape_and_1d():
    # Args have the same shape and each has one dim
    assert _check_comparable(np.ones(42), np.zeros(42.0)) is None


@raises(ValueError)
def test__check_comparable_not_both_1d_arrays():
    # One or both not ndarrays
    _check_comparable(1, np.arange(10))


@raises(ValueError)
def test__check_comparable_diff_cardinality():
    # Not the same cardinality
    _check_comparable(np.arange(8), np.arange(10))


#def test_neg_vec_and_zero_vec():
#    for m in metric_names:
#        # Currently fails on r_squared
#        assert np.isfinite(globals()[m](neg_vec, zero_vec))

def test_nash_sutcliffe():  # (obs_v, pred_v):
    # assert nash_sutcliffe(obs_v=?, pred_v=?) == ?
    pass


def test_r_squared():
    assert r_squared(vec1=asc_vec, vec2=asc_vec) == 1
    assert r_squared(vec1=asc_vec, vec2=desc_vec) == 1
    # What if one vec is partly or entirely negative?
    # What if one vec zeros?


def test_rmsd():
    # assert rmsd(vec1=?, vec2=?) == ?
    pass


def test_avg_pc_err():
    assert avg_pc_err(obs_v=asc_vec, pred_v=asc_vec) == 0.0
    assert avg_pc_err(obs_v=asc_vec, pred_v=desc_vec) < 100  # better test?
    # - pygof.avg_pc_err(zero_vec, asc_vec) gives NaN (as divide by sum of
    #   obs_v) - guard against?
    # - pygof.avg_pc_err(neg_vec, zero_vec) gives -100 -> correct?

    # assert avg_pc_err(obs_v=?, pred_v=?) == ?


def test_integ_sq_errors():
    # assert integ_sq_errors(vec1=?, vec2=?) == ?
    pass


def test_integ_weighted_sq_errors():
    # assert integ_weighted_sq_errors(obs_v=?, pred_v=?) == ?
    pass

#######################
# Tests for all metrics
#######################
# What if one arg all zeros or all ones?  What if both?
# Do get upper bound to output?
# Do get lower bound to output?
# Try hypotheses?
