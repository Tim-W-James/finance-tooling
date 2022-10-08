# Finance Tooling

Monorepo for all my finance/budgeting tooling.

## Firefly III

[Firefly III](https://www.firefly-iii.org/) is an open source personal finance
manager. Allows transactions management, budgeting, etc.

[fireflyiii/](fireflyiii/) has my config.

### Data Importer

[Firefly Data Importer](https://docs.firefly-iii.org/data-importer) is used to
import CSVs exported from bank transactions.

Example import config: [fireflyiii/import_config.json](fireflyiii/import_config.json)

## Spacy Categoriser

Uses natural language processing to categorise a bank transaction from on a
description.

Run via the CLI to prepare CSV files for import to Firefly. More details in [spacy-cat/README.md](spacy-cat/README.md).

## Trans Cat

Alternative to the Spacy Categoriser which can be used with a web app. Forked
from <https://github.com/Hapyr/trans-cat>.

The root [docker-compose.yml](docker-compose.yml) allows for the full stack to
be deployed with `docker compose -f docker-compose.yml up -d`.
