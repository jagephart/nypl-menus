# %%
import pandas as pd

# %%
import matplotlib.pyplot as plt
import seaborn as sns
import spacy

nlp = spacy.load("annotation_model/")
# %%
df = pd.read_csv("data/dflabeledtranslated_edited.csv")
# %%
df.head()
# %%
df.info()
# %%
test = df.sample(10)
# %%
test
# %%
ents = []
items = []
for name in test.name.values:
    doc = nlp(name)
    for ent in doc.ents:
        ents.append(ent)
        items.append(ent.label_)
# %%
ents
# %%
items
# %%
ents = []
items = []
for name in df.name.values:
    doc = nlp(name)
    for ent in doc.ents:
        ents.append(ent.text)
        items.append(ent.label_)
df_ents = pd.DataFrame({"Entity": ents, "EntityLabel": items})
# %%
df_ents.head()
# %%
sns.countplot(
    x="Entity",
    data=df_ents[df_ents["EntityLabel"] == "SEAFOOD"],
    order=df_ents[df_ents["EntityLabel"] == "SEAFOOD"]
    .Entity.value_counts()
    .iloc[:5]
    .index,
)
plt.title('Top 5 Seafood Entities')
# %%
sns.countplot(
    x="Entity",
    data=df_ents[df_ents["EntityLabel"] == "SIDE"],
    order=df_ents[df_ents["EntityLabel"] == "SIDE"].Entity.value_counts().iloc[:5].index,
)
plt.title('Top 5 Side Entities')

# %%
sns.countplot(
    x="Entity",
    data=df_ents[df_ents["EntityLabel"] == "METHOD"],
    order=df_ents[df_ents["EntityLabel"] == "METHOD"].Entity.value_counts().iloc[:5].index,
)
plt.title('Top 5 Method Entities')

# %%
sns.countplot(
    x="Entity",
    data=df_ents[df_ents["EntityLabel"] == "LOCATION"],
    order=df_ents[df_ents["EntityLabel"] == "LOCATION"].Entity.value_counts().iloc[:5].index,
)
plt.title('Top 5 Location Entities')

# %%
