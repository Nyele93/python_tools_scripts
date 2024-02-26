The `generate_dt.py` is a python script, for generating N-number of random datetime values, that will be written in SQL format as `UPDATE` statetements, for populating a table.
The randomly generated datetime values are generated such that the time part can be repeated, but not more than 3 times.
>It requires that the target table has an `id` column, that is *auto_incremental* (This is needed for *sorted UPDATES*).

To see the helper function of the script, call the script with the `-h` flag. **(see below snippet)**
```
root@michael-VirtualBox:/home/michael# python3 generate_dt.py -h
usage: generate_dt.py [-h] [--sample_size SAMPLE_SIZE] --table_name TABLE_NAME --dt_column_name DT_COLUMN_NAME
Command-line argument parser
options:
  -h, --help            show this help message and exit
  --sample_size SAMPLE_SIZE
                        Sample size (default: 100)
  --table_name TABLE_NAME
                        Target table name
  --dt_column_name DT_COLUMN_NAME
                        Target datetime column name
```
The script also comes with predefined `assertions`, to avoid wrong input entry, via *prompted warnings*
```
root@michael-VirtualBox:/home/michael# python3 generate_dt.py --table_name t --dt_column_name date_created --sample_size 10 --fake_arg yes
ERROR: Too many arguments. USAGE: python3 generate_dt.py --table_name tbl_name --dt_column_name dt_col_name --sample_size N		

root@michael-VirtualBox:/home/michael# python3 generate_dt.py --table_name t --dt_column_name --sample_size 10
usage: generate_dt.py [-h] [--sample_size SAMPLE_SIZE] --table_name TABLE_NAME --dt_column_name DT_COLUMN_NAME
generate_dt.py: error: argument --dt_column_name: expected one argument
```

When script is executed successfully, the output file is also listed as well as status. **See sample run below**
```
root@michael-VirtualBox:/home/michael# python3 generate_dt.py --table_name t --dt_column_name date_created --sample_size 10
output file generated: t_date_created_2024-02-26_22-46-55.sql
file generated successfully...
root@michael-VirtualBox:/home/michael# cat t_date_created_2024-02-26_22-46-55.sql
--Update statements generated for table t below:
UPDATE t SET (date_created) = '2023-05-19 07:57:27' WHERE id = 1;
UPDATE t SET (date_created) = '2023-07-20 05:56:22' WHERE id = 2;
UPDATE t SET (date_created) = '2023-08-19 08:57:47' WHERE id = 3;
UPDATE t SET (date_created) = '2023-08-21 09:17:59' WHERE id = 4;
UPDATE t SET (date_created) = '2023-09-09 07:24:54' WHERE id = 5;
UPDATE t SET (date_created) = '2023-11-16 16:09:14' WHERE id = 6;
UPDATE t SET (date_created) = '2023-11-20 16:03:47' WHERE id = 7;
UPDATE t SET (date_created) = '2023-12-15 02:07:10' WHERE id = 8;
UPDATE t SET (date_created) = '2024-01-19 07:45:33' WHERE id = 9;
UPDATE t SET (date_created) = '2024-01-31 07:24:39' WHERE id = 10;
```

The generated file can be passed into a running DB engine to execute the commands.

