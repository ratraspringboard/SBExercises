# Loading routine libraries
import pandas as pd
import json
from pandas.io.json import json_normalize


# load json as string
data = json.load((open('data/world_bank_projects.json')))

# normalise the dataset, countries with highest number of projects
data_normalise = json_normalize(data)
data_normalise.countryname.value_counts().head(10)

# Table from nested elements, top 10 proejct themes
data_normalise = json_normalize(data,'mjtheme_namecode')
data_normalise.name.value_counts().head(10)

# Taking care of the empty project name- creating a dataframe to replace empty cell with 'Missing project name'  
data_normalise.name =data_normalise.name.replace('','Missing Project Name')
data_normalise






