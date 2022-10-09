import pandas as pd
import matplotlib.pyplot as mp

df = pd.read_csv("files/losses.csv")
                        
df.plot.line(y=["g_losses", "d_losses"])
                        
mp.show()