"""
Test epispot's ability to load and save models:
1. Creates a custom model and saves it to a file.
2. Loads the model from the file and checks that the model is correct.

STRUCTURE:
└ main
"""

from os import mkdir, path
import numpy as np
import epispot as epi


# TESTS
def test_main():
    """SIR Model"""
    
    # params
    N = 1e6
    R_0 = lambda t: 2.0 + 0.5 * np.sin(t)
    gamma = epi.params.Gamma(R_0=R_0, beta=3)

    # compile compartments
    Susceptible = epi.comps.Susceptible(R_0, gamma, N)
    Infected = epi.comps.Infected()
    Removed = epi.comps.Removed()

    # compile parameters
    matrix = np.empty((3, 3), dtype=tuple)
    matrix.fill((1.0, 1.0))  # default probability and rate
    matrix[1][2] = (1.0, gamma)  # I => R

    # compile model
    SIR_Model = epi.models.Model(N)
    SIR_Model.add(Susceptible, [1], matrix[0])
    SIR_Model.add(Infected, [2], matrix[1])
    SIR_Model.add(Removed, [], matrix[2])
    SIR_Model.compile()

    # get solutions
    Solution = SIR_Model.integrate(np.linspace(0, 20, 100), delta=0.2)
    predicted = Solution[99]
    
    # save model
    if not path.exists('tests/artifacts'):
        mkdir('tests/artifacts')
    SIR_Model.save('tests/artifacts/SIR_Model.epi')

    # load model
    loaded = epi.models.Model.load('tests/artifacts/SIR_Model.epi')

    # check model
    re_Solution = loaded.integrate(np.linspace(0, 20, 100), delta=0.2)
    re_predicted = re_Solution[99]
    assert np.allclose(predicted, re_predicted)
