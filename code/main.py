import os
import flask
import functions_framework
import psycopg2

#this is a test comment
@functions_framework.http
def initialize_db(request: flask.Request) -> flask.Response:
    db = connect()
    
    if db:
        return flask.Response(response="Connection successfully tested v2......")
    
    return flask.Response(
        response="Request Failed",
        status=400,
    )

def config():
    params = {}
    params['host'] = os.environ['DB_HOST']
    params['user'] = os.environ['DB_IAM_USER']
    params['database'] = os.environ['DB_NAME']
    params['port'] = os.environ['DB_PORT']
    return params



def connect():
    """ Connect to the PostgreSQL database server """
    try:
        # Read connection parameters
        params = config()
        connection = psycopg2.connect(database=params['database'], user=params['user'], host=params['host'], port=params['port'])
        cursor = connection.cursor()
        # Connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        query = "select * from pg_catalog.pg_tables;"
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        print('Connected.')
        cursor.close()
        return result
    except Exception as error:
        print(f"Error occurred : {error}")
        return False
