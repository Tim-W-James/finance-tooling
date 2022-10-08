import os
import shutil

import pandas as pd
import spacy
from dotenv import load_dotenv
from sklearn.model_selection import train_test_split
from spacy.tokens import DocBin

from utils import prepareDescription

load_dotenv()

historicalCsvPath = os.environ.get("ISTORICAL_CSV_PATH")

# prepare data for training from a csv with the header:
# ,Date,Description,Debits and credits,Balance
def prepareData(inFile="data.csv"):
  data = pd.read_csv(inFile)
  data = data[["Description", "Category"]]
  data = data.dropna()
  for index, description in enumerate(data["Description"]):
    preparedDescription = prepareDescription(description)

    if (preparedDescription == ""):
      data.drop(index, inplace=True)
    else:
      data.loc[index,"Description"] = preparedDescription
  return data

# convert a data frame into a spacy DocBin object for classification
def convert(data, categories, outfile="data.spacy"):
  nlp = spacy.blank("en")
  db = DocBin()

  for desc, cat in zip(data["Description"], data["Category"]):
    doc = nlp.make_doc(desc)
    doc.cats = {category: 0 for category in categories}
    doc.cats[cat] = 1
    db.add(doc)
  db.to_disk(outfile)

data = prepareData(historicalCsvPath)
categories = data["Category"].unique()
print("CATEGORIES")
print(categories)

train, dev = train_test_split(data, test_size=0.33, random_state=42)
print("\nTRAINING DATA")
print(train)
print("\nTEST DATA")
print(dev)

if os.path.isdir("model"):
  shutil.rmtree("model")

os.mkdir("model")
convert(train, categories, "model/train.spacy")
convert(dev, categories, "model/dev.spacy")
