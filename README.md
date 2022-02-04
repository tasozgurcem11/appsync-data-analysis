##  Run graphql query on AppSync with Python

#### In order to run create credentials.py file with your AWS credentials below. 

Go to AWS AppSync -> <your-app-sync-application> -> Settings for credentials.

`APPSYNC_API_ENDPOINT_URL = '<your-api-endpoint-url>'`

`APPSYNC_API_KEY = '<your-api-key>'`

connect.py will connect to your appsync api and return the data in JSON format

simpy run `python connect.py`

#### Note: will add Google Sheets connection later.