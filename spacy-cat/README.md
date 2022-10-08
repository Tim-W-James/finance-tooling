# Transaction Categoriser

Uses natural language processing to categorise a bank transaction from on a
description. For example, the description "Purchase Burger" could be categorised
as "FOOD".

General purpose enough to classify any text into discrete categories if need be.

## Getting Started

### Prerequisites

- pyenv: <https://github.com/pyenv/pyenv>
- pipenv: <https://pipenv.pypa.io/en/latest/>

### Install dependencies

```sh
make install
```

### Setup

- You'll need some training data to start with. Create a CSV with at least the
  column `Description` and `Category`
- Create a `.env` file with the following config:

  ```sh
  # path training data csv that has a `Category` column prefilled
  HISTORICAL_CSV_PATH="../data/historical.csv"
  # path for new data csv to categorise, using the `Description` field for classification
  UNCATEGORISED_CSV_PATH="../data/uncategorised.csv"
  # path to write categorised data 
  CATEGORISED_CSV_PATH="../data/categorised.csv"
  # if the model has low confidence for a given classification, prompt for user input via the CLI
  MANUALLY_RESOLVE_AMBIGUOUS="true"
  ```

### Train

Train the model with historical data:

```sh
make train
```

### Categorise

Use you new model to categorise your csv:

```sh
make run
```

### Retrain

Incorporate new data into the model:

```sh
make retrain
```
