# read_csv
# read_excel
# read_hdf
# read_sql
# read_json
# read_html
# real_gdb
# read_stata_read_sas
# read_clipboard
# read_pickle
# https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html

import pandas as pd
import numpy as np

data = pd.read_csv('Students.csv')
print(data)

data.to_pickle('Students.pickle')