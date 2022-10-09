# Firefly iii

Various pieces of config for [Firefly III](https://www.firefly-iii.org/).

## Export

<https://docs.firefly-iii.org/firefly-iii/exporting-data/>

- Export config:

  ```sh
  docker exec -it <container> php artisan firefly-iii:export-data --export-accounts --export-budgets --export-categories --export-tags --export-recurring --export-rules --export-bills --export-piggies --export_directory=./storage/export/ --force --token=<cli-token> && docker cp
  fireflyiii-app-1:/var/www/html/storage/export .
  ```

- Transactions: use `--export-transactions`

## Manual Backup

<https://docs.firefly-iii.org/firefly-iii/advanced-installation/backup/>

- Create a backup:

  ```sh
  docker run --rm -v "firefly_iii_db:/tmp" -v "$HOME/backups/firefly:/backup" ubuntu tar -czvf /backup/firefly_db.tar /tmp
  ```

- Restore:

  ```sh
  docker run --rm -v "firefly_iii_db:/recover" -v "$HOME/backups/firefly:/backup" ubuntu tar -xvf /backup/firefly_db.tar -C /recover --strip 1
  ```
