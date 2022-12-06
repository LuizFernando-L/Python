#in 1
import pandas
import pandas as pd
pandas.read_json(path_or_buf=None, orient=None, typ='frame',
                 dtype=None, convert_axes=None, convert_dates=True,
                 keep_default_dates=True, numpy=False, precise_float=False,
                 date_unit=None, encoding=None, lines=False, chunksize=None,
                 compression='infer')
#in 2
pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json").head()