# !pip install datatable
import datatable as dt
df = dt.fread('../input/jane-street-market-prediction/train.csv').to_pandas()