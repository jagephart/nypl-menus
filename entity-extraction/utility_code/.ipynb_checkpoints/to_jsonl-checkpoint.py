# %%
import pandas as pd
# %%
df = pd.read_csv('data/r_seafood.csv', index_col=0)
# %%
df.head()
# %%
titles = df.title.values
# %%
titles
# %%
import json
# %%
dict_list = []
# %%
for title in titles:
    dict_list.append({"text": title})
# %%
dict_list
# %%
with open('data/r_seafood.jsonl', 'w') as outfile:
    for entry in dict_list:
        json.dump(entry, outfile)
        outfile.write('\n')
# %%
def to_jsonl(file_path: str):
    df = pd.read_csv(file_path, index_col=0)
    titles = df.title.values
    dict_list = [{"text":title} for title in titles]
    path = file_path.split('.')[0]
    with open(f'{path}.jsonl', 'w') as outfile:
        for entry in dict_list:
            json.dump(entry, outfile)
            outfile.write('\n')
# %%
paths = ['data/r_seafood.csv', 'data/r_seafoodrecipes.csv', 'data/r_cooking.csv', 'data/r_travel.csv']
# %%
for path in paths:
    to_jsonl(path)
# %%
