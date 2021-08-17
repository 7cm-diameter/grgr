""" Describe the procedure that must be called at initialization. """
__version__ = '0.1.0'

from rpy2.robjects import numpy2ri, pandas2ri, r

numpy2ri.activate()
pandas2ri.activate()

# All modules share this R instance, so it is a constant
_R = r
_R("library(ggplot2)")
