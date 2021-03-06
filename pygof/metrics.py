from __future__ import absolute_import
from __future__ import division

import numpy as np
import scipy.stats as sp_stats


def _check_comparable(vec1, vec2):
    are_ndarrays = all((isinstance(v, np.ndarray) for v in (vec1, vec2)))
    are_comparable = are_ndarrays and \
        (vec1.shape == vec2.shape and vec1.ndim == vec2.ndim == 1)

    if not are_comparable:
        raise ValueError("Arguments must be 1D numpy.ndarrays " +
                         "of the same shape")


def nash_sutcliffe(obs_v, pred_v):
    """
    Nash Sutcliffe Efficiency Index correlation metric

    Nash, J. E. and Sutcliffe, J. V. (1970).  River flow forecasting through
    conceptual models part I - A discussion of principles, J. Hydrology, 10(3),
    pp. 282-290, ISSN 0022-1694, DOI 10.1016/0022-1694(70)90255-6
    """
    _check_comparable(obs_v, pred_v)
    obs_v_mean = obs_v.mean()
    return 1. - (np.sum(np.power(obs_v - pred_v, 2.)) /
                 np.sum(np.power(obs_v - obs_v_mean, 2.)))


def r_squared(vec1, vec2):
    """Aka coefficient of determination (?).

    Is square of Pearson product-moment correlation coefficient.

    See http://www.statsoft.com/Textbook/Statistics-Glossary/P/button/p#Pearson%20Correlation

    """
    _check_comparable(vec1, vec2)
    return (sp_stats.pearsonr(vec1, vec2)[0]) ** 2.


def rmsd(vec1, vec2):
    """Root Mean Square Deviation correlation metric

    See:
    Anderson, M. P. and Woessner, W. W. (1992).  Applied Groundwater Modeling:
    Simulation of Flow and Advective Transport, Academic Press, London, UK.
    """
    _check_comparable(vec1, vec2)
    return np.sqrt(np.sum(np.power(vec1 - vec2, 2.)) / vec1.size)


def avg_pc_err(obs_v, pred_v):
    """Average Percent Error correlation metric.

    See:
    Kashefipour, S. M. and Falconer, R. A. (2002). Longitudinal dispersion
    coefficients in natural channels, Water Research, 36(6), pp 1596-1608,
    ISSN 0043-1354, DOI: 10.1016/S0043-1354(01)00351-7
    """
    _check_comparable(obs_v, pred_v)
    return 100 * np.sum(np.abs(obs_v - pred_v)) / np.sum(obs_v)


def integ_sq_errors(vec1, vec2):
    """Integral of squared errors."""
    _check_comparable(vec1, vec2)
    return np.sum(np.power(vec1 - vec2, 2.0))


def integ_weighted_sq_errors(obs_v, pred_v):
    """Integral of squared errors, weighted by the observation magnitude"""
    _check_comparable(obs_v, pred_v)
    return np.sum(obs_v * np.power(obs_v - pred_v, 2.0))
