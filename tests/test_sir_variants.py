"""
Test of all simple SIR-related models and variants. 
Does not use any functions as parameters or otherwise special 
parameters. This test is meant for *basic* code coverage. For advanced 
coverage, use the test_advanced.py check.

STRUCTURE:
├ SIR
├ SEIR
└ SIRD
"""

import numpy as np

import epispot as epi


# TESTS
def test_SIR():
    """SIR Pre-Compiled Model Test"""
    SIR = epi.pre.SIR(2.5, 1/2, 1e6)
    Solution = SIR.integrate(range(100))
    predicted = np.around(Solution[99], -2)
    assert np.allclose(predicted, np.array([70900, 0, 929100]))

def test_SEIR():
    """SEIR Pre-Compiled Model Test"""
    SEIR = epi.pre.SEIR(2.5, 1/2, 1e6, 1/2)
    Solution = SEIR.integrate(range(100))
    predicted = np.around(Solution[99], -2)
    assert np.allclose(predicted, np.array([90300, 0, 0, 909700]))

def test_SIRD():
    """SIRD Pre-Compiled Model Test"""
    SIRD = epi.pre.SIRD(2.5, 1/2, 1e6, 1/3, rho=3/4)
    Solution = SIRD.integrate(range(100))
    predicted = np.around(Solution[99], -2)
    assert np.allclose(predicted, np.array([70900, 0, 464600, 464600]))
