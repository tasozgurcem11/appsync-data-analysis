import requests
from credentials import *


def run_query(query):
    """
    This function runs APPSYNC query and returns the results as JSON.
    :param query:
    :return:
    """
    # start a session
    session = requests.Session()

    response = session.request(
        url=APPSYNC_API_ENDPOINT_URL,
        method='POST',
        headers={'x-api-key': APPSYNC_API_KEY},
        json={'query': query}
    )
    print(f'Response code: {response.status_code}')
    return response.json()