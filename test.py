import numpy as np
import yaml, os
from sys import path
from pathlib import Path
import matplotlib.pyplot as plt

# path.append("/home/gmraz/starships/")
# path.append("/home/gmraz/ENV_starships_J2025/starships/starships/")
# path.append("ENV_starships_Feb2025/lib/python3.10/site-packages/starships/")
            
import astropy.units as u
import astropy.constants as const

from starships.instruments import load_instrum
import pipeline.reduction as red
import pipeline.make_model as mod
import pipeline.correlations as corr
import pipeline.run_pipe as run
import pipeline.split_nights as split
from importlib import reload

import copy

reload(run)
reload(corr)
reload(mod)
reload(red)

from starships.correlation import quick_correl
from starships.correlation_class import Correlations

import warnings
warnings.simplefilter("ignore", UserWarning)
warnings.simplefilter("ignore", RuntimeWarning)