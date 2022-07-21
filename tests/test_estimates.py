"""
Test of the `estimates` subpackage in `epispot`
*Only tests logic and skips over repetitive testing for all estimates*

STRUCTURE:
├ santos
└ bentout
"""

import numpy as np
import epispot as epi


# TESTS
def test_santos():
    """SEIR Model using pre-fit parameters from a genetic algorithm"""
    
    # Load data
    paper = 'SARS-CoV-2/Santos 2022/'
    beta = epi.estimates.getters.query(paper + 'beta')
    gamma = epi.estimates.getters.query(paper + 'gamma')
    delta = epi.estimates.getters.query(paper + 'delta')

    # Create required params
    p_R_0 = epi.params.R_0()
    R_0 = lambda t: p_R_0(t, gamma=gamma(t), beta=beta(t))
    N = 109.6e6  # Philippines

    # Set up model
    Model = epi.pre.SEIR(R_0, gamma, N, delta)

    # get solutions
    Solution = Model.integrate(range(100))
    return Solution

def test_bentout():
    """SEIR Model using estimated initial parameters"""

    # Load data
    paper = 'SARS-CoV-2/Bentout et al. 2020/'
    R_0 = epi.estimates.getters.query(paper + 'R_0')
    gamma = epi.estimates.getters.query(paper + 'gamma')
    delta = epi.estimates.getters.query(paper + 'delta')

    # Create required params
    N = 43.85e6  # Algeria

    # Set up model
    Model = epi.pre.SEIR(R_0, gamma, N, delta)

    # get solutions
    Solution = Model.integrate(range(100))
    return Solution

test_santos()
test_bentout()
