import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno

from XtraNetflixGraphUtility import  *
from XtraNetflixHelperFunction import *


df = pd.read_csv("netflix_titles.csv")
#df.head()
#df.info()
#df.isnull().sum()
#msno.matrix(df)
#df.describe()



df_cleaned = CleanedData(df)
#print('Data CLeaned')


#PlotDistribution(df_cleaned,plt,sns)
#print('Protting Distribution')


Top10CoutryProducer(df_cleaned,plt,sns)
print('Producing Country')



ContentRating(df_cleaned,plt,sns)
print('Protting Rating')


CleanYear(df_cleaned,pd,np)
#print('Year Cleanned')


TitlePerYear(df_cleaned,plt,sns)
print('Protting Per Year')


Top10Director(df_cleaned,plt,sns)
print('Protting Director')


Top10Actor(df_cleaned,plt,sns,pd)
print('Protting Actor')


DurationForMovie(df_cleaned,plt,sns)
print('Protting Duration')



