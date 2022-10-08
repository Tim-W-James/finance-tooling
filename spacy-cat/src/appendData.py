import os

import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# push new categorised data into a historical table to refine the model
historicalCsvPath = os.environ.get("HISTORICAL_CSV_PATH")
categorisedCsvPath = os.environ.get("CATEGORISED_CSV_PATH")

data = pd.read_csv(categorisedCsvPath)

if os.path.exists(historicalCsvPath):  
  data.to_csv(historicalCsvPath, mode="a", index=False, header=False)
else:
  data.to_csv(historicalCsvPath, index=False)
