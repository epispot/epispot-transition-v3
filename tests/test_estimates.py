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
    
    # load data
    paper = 'SARS-CoV-2/Santos 2022/'
    beta = epi.estimates.getters.query(paper + 'beta')
    gamma = epi.estimates.getters.query(paper + 'gamma')
    delta = epi.estimates.getters.query(paper + 'delta')

    # create required params
    R_0 = epi.params.R_0(gamma=gamma, beta=beta)
    N = 109.6e6  # Philippines

    # set up model
    Model = epi.pre.SEIR(R_0, gamma, N, delta)

    # get solutions
    Solution = Model.integrate(np.linspace(0, 50, 200))
    predicted = np.around(Solution[199], -2)
    assert np.allclose(
        predicted, np.array([1.09e4, 9.816e5, 3.069e6, 1.055385e8])
    )

def test_bentout():
    """SEIR Model using estimated initial parameters"""

    # load data
    paper = 'SARS-CoV-2/Bentout et al. 2020/'
    R_0 = epi.estimates.getters.query(paper + 'R_0')
    gamma = epi.estimates.getters.query(paper + 'gamma')
    delta = epi.estimates.getters.query(paper + 'delta')

    # create required params
    N = 43.85e6  # Algeria

    # set up model
    Model = epi.pre.SEIR(R_0, gamma, N, delta)

    # get solutions
    Solutions = Model.integrate(
        range(100), starting_state=np.array([N - 100, 100, 0, 0])
    )
    predicted = np.around(Solutions[99], -2)
    assert np.allclose(
        predicted, np.array([18050200, 7308800, 9223400, 9267600])
    )
