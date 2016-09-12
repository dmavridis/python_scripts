import pandas as pd

dict1 = {0:[2016,'skat',5],
         1:[2016,'skat',9],
         2:[2016,'kath',3],
         3:[2016,'kath',14],
         4:[2015,'kath',5],
         5:[2015,'kath',5],
         6:[2016,'tasaras',17],
         7:[2016,'tasaras',13]
         }


dict_pd = pd.DataFrame.from_dict(dict1, orient='index')
dict_pd.columns = ['year','name','times']

grp_year = dict_pd.groupby('year')
grp_year = dict_pd.groupby(['name','year'], as_index = False).sum()

food_pd = pd.DataFrame.from_dict(dict1, orient='index')
food_pd.columns = ['year','name','food']

skata = pd.merge(grp_year,food_pd)
