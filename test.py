import pandas as pd
import matplotlib.pyplot as mp
from pyodide.http import open_url

df = pd.read_csv(open_url('https://github.com/spradier/spradier.github.io/blob/master/files/losses.csv'))
                        
df.plot.line(y=["g_losses", "d_losses"])
                        
mp.show()