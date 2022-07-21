"""
Basic packaging checks

STRUCTURE: 
├ base
    ├ dependency (x2)
    └ sanity
└ integrity
"""


def test_base():
    """Triggers automatic import checks from within epispot"""
    import epispot
    epispot.dependency_check()
    epispot.plots.dependency_check()
    epispot.sanity_check()


def test_integrity():
    """Tests epispot's integrity (ensures no module is missing)"""
    from epispot import comps
    from epispot import models
    from epispot import params
    from epispot import pre

    from epispot.plots import web
    from epispot.plots import native
    
    from epispot.estimates import data
    from epispot.estimates import getters
    from epispot.estimates import storage
    from epispot.estimates import utils
