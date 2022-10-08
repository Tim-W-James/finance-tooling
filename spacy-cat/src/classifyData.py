
import os

import numpy as np
import pandas as pd
import spacy
from dotenv import load_dotenv

from utils import prepareDescription

load_dotenv()

historicalCsvPath = os.environ.get("HISTORICAL_CSV_PATH")
categorisedCsvPath = os.environ.get("CATEGORISED_CSV_PATH")
uncategorisedCsvPath = os.environ.get("UNCATEGORISED_CSV_PATH")

manuallyResolveAmbiguous = os.environ.get("MANUALLY_RESOLVE_AMBIGUOUS").lower() == "true"

nlp = spacy.load("model/textcat_model/model-best")

data = pd.read_csv(uncategorisedCsvPath, index_col=[0])

categories = []
if os.path.isfile(historicalCsvPath):
  categories = pd.read_csv(historicalCsvPath)["Category"].unique()
print("Existing categories: ", categories)

# reindex the data frame to start at 0
data.reset_index(inplace=True)

# add categorisation headers
if "Category" in data.columns:
  data["Category"].fillna("UNASSIGNED")
else:
  data["Category"] = "UNASSIGNED"

for index, description in enumerate(data['Description']):
  if data.loc[index,"Category"] != "UNASSIGNED":
    continue
  preparedDescription = prepareDescription(description)
  if (preparedDescription == ""):
    data.drop(index, inplace=True)
    continue
  doc = nlp(preparedDescription)
  categoryEstimates = doc.cats

  # determine the category with the highest confidence
  bestCategory = max(categoryEstimates, key=categoryEstimates.get)
  confidence = max(categoryEstimates.values())
  data.loc[index,"Category"] = bestCategory

  date = data.loc[index,"Date"].replace("/", "-")
  price = data.loc[index,"Debits and credits"]

  if (confidence < 0.8) and manuallyResolveAmbiguous:
    print(f"Low confidence ({confidence}) categorising: {description} ({price} - {date})")
    print(f"Top guesses: {sorted(categoryEstimates, key=categoryEstimates.get, reverse=True)[:3]}")
    print("Enter the category:")
    newCategory = input()
    if not np.isin(newCategory, categories):
      print(f"Created new category: {newCategory}")
      categories = np.append(categories, newCategory)
    data.loc[index,"Category"] = newCategory
  else:
    print(f"{bestCategory} ({confidence}) -> {description}")

  # update cvs with categories every row, so that if the program is terminated
  # before completion, data is not lost
  data.to_csv(categorisedCsvPath, index=False)


