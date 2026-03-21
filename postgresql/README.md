 # Introdution
Insert data to PostgreSQL.

To connect to database:
```
psql -h 194.233.93.255 -p 22641 -U admin -d DB_POOL 
```

To quit:
```
\q
```

To run a specific `.sql` file, after connect:
```
\i <file_path>
```

For instance:
```
\i postgresql/view_table.sql
```