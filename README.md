![](images/bannerProject.png)
This is the assessment of skillset as part of the interview process of Spark Network for Junior Data Engineer position. 

## Project Description:
This project is composed of an ETL challenge, combined with Python, SQL and git skills. In which we extract information from a RestAPI, make transformations so the data is PII complient and ready for further analyses, and load this information into a database.

With this project I create a database in the following format:
![](images/spark_networks_database.png)

### This project can be run on docker or in your personal machine.


## Requirements:

[Docker](https://www.docker.com/products/docker-desktop) installed or the following modules:
```
pandas==1.3.4
PyMySQL==1.0.2
requests==2.26.0
SQLAlchemy==1.4.28
```
##### A requirements.txt is available in the python folder.

## How to Use it:
- Firstly dowload the repository and unzip it, or git clone https://github.com/tiaversa/sparkNetworksChallenge.
##### By Docker:
run: 
```
cd python
docker-compose up
```
- Utilize sql_test.sql to run queries in the new database.

#### By Loading Information In Your Local Server:
WARNING: this project is not ready to commit for production, local testing only. User be ware!

- Install, initialize and activate a virtual enviroment with the following comands:
```
cd python
pip install virtualenv
virtualenv env

# Activate enviroment with Mac and Linux:
source myproject/venv/bin/activate
# Activate enviroment with Windows:
env\Scripts\activate.bat
```
- Install dependencies:
```
pip -r requirements.txt
```
- Open the file 'credentials.py' and edit with the information for you personal server.
```
mysql_db_config = {
    'host': '127.0.0.1',
    'user': 'my_user',
    'password': 'my_password',
    'port': 3306,
    'database' : 'spark_networks_test'
}
```
- Run main.py
```
python main.py
```
- Utilize sql_test.sql to run queries in the new database.

## How does it work:
![](images/spark_networks_database_2.png)
The project begins by making requests from the data sources in a RestAPI, wich returns a JSON response that is storaded into variables in the program. In the next step the program flattens the data and adds the information into DataFrames for easier manipulation. From the DataFrame, first a cleaning of personal information is performed, then the information is casted into the right datatypes. And finally a connection to the database is performed, if the database or tables don't exists yet they are created and finally the data is uploaded into the database.

##### A group of queries are provided in the file sql_test,sql in which you may performe some tests in the information uploaded into the database.

## Contributors:
Timnna Aversa < <timnaaversa@gmail.com> >

## License and Copyright
© Timna Costa Aversa

Licensed under the [MIT License](License).


![](images/thanks.png)
