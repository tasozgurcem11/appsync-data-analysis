import requests
from credentials import *


def run_query(query):
    # start a session
    session = requests.Session()

    response = session.request(
        url=APPSYNC_API_ENDPOINT_URL,
        method='POST',
        headers={'x-api-key': APPSYNC_API_KEY},
        json={'query': query}
    )
    print(f'Response code: {response.status_code}')
    print(response.json()['data'])
    return response.json()


# define the query
query = """
{
      listUsers{
        items{
          name
          availability
          email
          createdAt
        }
      }
    }
    """
run_query(query)
