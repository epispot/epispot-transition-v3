"""
The `epispot.getters` module contains various scripts for listing, 
querying, and loading data from the literature. Alternatively, the data
can be loaded directly from `epispot.estimates.data`.

"""

# imports
from . import storage


# querying
def query(match):
    """
    Query the literature for estimates.
    
    ## **Parameters**
    
    `match`: Query as tuple of IDs or slash-separated string.
             Use IDs for all queries except papers 
             (use in-text citations).
             Ex: `('SARS-CoV-2', 'Ganyani et al. 2020')` or
             `'SARS-CoV-2/Lauer et al. 2020/gamma'`
    
    ## **Example**
    
    ```python
    >>> from epispot.getters import query
    >>> query('SARS-CoV-2')
    <epispot.utils.Disease object at 0x...>

    ## **Error Handling**

    If the query returns no results, a `ValueError` will be raised.
    No errors are raised related to query format, however.
    ```
    
    """
    # convert to list if not already
    if isinstance(match, str): match = match.split('/')

    # helper functions
    def query_params(data):
        for param in data:
            if param.id == match[2]:
                return param

    def query_papers(data):
        for paper in data:
            if paper.in_text == match[1]:
                if len(match) == 2:
                    return paper
                else:
                    return query_params(paper.params)

    def query_diseases(data):
        for disease in storage.bulk:
            if disease.id == match[0]:
                if len(match) == 1:
                    return disease
                else:
                    return query_papers(disease.papers)  

    # search for match
    queried = query_diseases(storage.bulk)
    if queried is None:
        raise ValueError(
            f'No match found for {match}; try a different query or '
            + 'manually load the data (see `epi.estimates.utils`).'
        )

    return queried
