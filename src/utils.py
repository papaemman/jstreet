# !pip install datatable
import datatable as dt
df = dt.fread('../input/jane-street-market-prediction/train.csv').to_pandas()


# package resources
import pkg_resources
dists = [d for d in pkg_resources.working_set]
dists