# takataka_backend
A garbage collection sales backend done in Flask (https://flask.palletsprojects.com/en/2.0.x/quickstart/#)


## Installations
### Pre-requisites
- Python 3.* (https://www.python.org/downloads/)
- MySql installation (https://www.mysql.com/downloads/)

### Python installations
> cd current_directory (./ -> takataka)

> pip install -r ./requirments.txt

## Config
Copy ./config.py.example >> ./config.py

### Database config
- Edit/Create ./instance/config.py to desired database values
- Refer to ./app/schema.sql for 'db_name'

To initialize tables:
- Login to mysql console
> cd current_dir (./ -> takataka)

> mysql -u user_name -p db_name

- Once in the shell
>  source ./app/schema.sql

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

> Running on http://127.0.0.1:5000/

## Postman Collection
- Open postman
- File > Import > Upload files
- Select collection at ./takataka.postman_collection.json