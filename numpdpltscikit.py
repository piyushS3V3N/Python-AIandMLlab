#implementation of numpy, Pandas, matplotlib and Scikit

import numpy as np
import pandas as pd
from matplotlib import pyplot as pt


ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))


ts = ts.cumsum()

ts.plot()

pt.show()
