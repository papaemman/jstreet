
## Check Development environment and modules version 
import sys
print("The python version is:", sys.version)

try:
    import janestreet
except:
    print("janestreet module isn't available")


import numpy as np
import pandas as pd
import xgboost as xgb

assert np.__version__ == '1.18.5'
assert pd.__version__ == '1.1.4'
assert xgb.__version__ == '1.2.1'