# Database Feeder
A complement to my project [Hortifruti Scrapping](https://github.com/JohnathanBarb/hortifruti_scrapping) where this application uses the csv file to make changes to a database.

This application uses the csv output of this other project to feed the database of [another project]().

# Usage/Exemples
To run this aplication:

Is needed change the url of database and add your driver package database
```shell
python3 database.py /path/to/file.csv
```

# Instalation
This application uses Python 3.9.4
```shell
git clone https://github.com/JohnathanBarb/database_feeder.git

cd database_feeder

python3 -m venv venv

source venv/bin/activate

pip3 install -r requirements.txt
```