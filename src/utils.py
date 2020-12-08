# !pip install datatable
import datatable as dt
df = dt.fread('../input/jane-street-market-prediction/train.csv').to_pandas()


# package resources
import pkg_resources
dists = [d for d in pkg_resources.working_set]
dists

# Reload a module
import importlib
from src import dispatcher
importlib.reload(dispatcher)
from src.dispatcher import MODELS