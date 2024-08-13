# Normalize all the line endings (Changes for Git in Windows)
```
git config core.fileMode false
```
```
git add --renormalize .
git commit -m "Normalize all the line endings"
```
```
git reset --hard HEAD
```

# Start migrations
```
python manage.py makemigrations
```
```
python manage.py migrate
```


# Start create superuser
```
python manage.py createsuperuser
```

# Databse UMb217poi81OSH7Q5lHfWDFZojvjKN7v
```
psql -h dpg-cqc6cf56l47c73cumtbg-a.frankfurt-postgres.render.com  -U accress -d accress_m1nt -f backup_postgres/accress.sql
```     