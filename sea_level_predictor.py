import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress 
import numpy as np

def draw_plot():
    # Read data from file
  df=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
  fig,axs=plt.subplots(figsize=(16,8))
  plt.scatter('Year','CSIRO Adjusted Sea Level',data=df)
    # Create first line of best fit
  to2050=np.arange(1880,2051)
  result=linregress(df['Year'],df['CSIRO Adjusted Sea Level'])

  plt.plot(to2050,result.intercept + result.slope*to2050,'r')

    # Create second line of best fit
  from2000to2050=np.arange(2000,2051)
  df2=df[df['Year']>1999]
  result2=linregress(df2['Year'],df2['CSIRO Adjusted Sea Level'])
  plt.plot(from2000to2050,result2.intercept+result2.slope*from2000to2050,'b')
  
    # Add labels and title
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
