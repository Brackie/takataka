# takataka_backend
A garbage collection sales backend done in Flask (https://flask.palletsprojects.com/en/2.0.x/quickstart/#)


## Installations
### Pre-requisites
- Python 3.* (https://www.python.org/downloads/)
- MySql installation (https://www.mysql.com/downloads/)

### Python installations
> cd working_directory (./takataka/takataka-be/)

> pip install -r ./requirments.txt

## Config
Copy ./config.py.example >> ./config.py

### Database config
- Edit/Create ./instance/config.py to desired database values
- Refer to ./app/schema.sql for 'db_name'

To initialize tables:
> cd working_dir (./takataka/takataka-be/)

- Login to mysql console: 

> mysql -u user_name -p db_name

- Once in the shell

>  source ./schema.sql

## Flask create app
Once all libraries are installed
- Linux

> $ export FLASK_APP='./app'

> $ export FLASK_ENV='development'

> $ flask run

> Running on http://127.0.0.1:5000/

- Windows CMD

> set FLASK_APP='./app'

> set FLASK_ENV='development'

> flask run

> Running on http://127.0.0.1:5000/

- Windows Powershel

> $env:FLASK_APP="./app"

> $env:FLASK_ENV="development"

> flask run

- Your flask app should now be running on http://127.0.0.1:5000/

## Postman Collection
- Open postman
- File > Import > Upload files
- Select collection at ./takataka/takataka-be/takataka.postman_collection.json