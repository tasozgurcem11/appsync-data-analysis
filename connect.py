from aws_requests_auth.boto_utils import BotoAWSRequestsAuth
import requests

APPSYNC_API_KEY = 'inAppsyncSettings'
APPSYNC_API_ENDPOINT_URL = 'https://aaaaaaaaaaaavzbke.appsync-api.ap-southeast-2.amazonaws.com/graphql'

headers = {
    'Content-Type': "application/graphql",
    'x-api-key': APPSYNC_API_KEY,
    'cache-control': "no-cache",
}
query = """{
    GetUserSettingsByEmail(email: "john@washere"){
      items {name, identity_id, invite_code}
    }
}"""


def test_stuff():
    # Use the library to generate auth headers.
    auth = BotoAWSRequestsAuth(
        aws_host='aaaaaaaaaaaavzbke.appsync-api.ap-southeast-2.amazonaws.com',
        aws_region='ap-southeast-2',
        aws_service='appsync')

    # Create an http graphql request.
    response = requests.post(
        APPSYNC_API_ENDPOINT_URL,
        json={'query': query},
        auth=auth,
        headers=headers)

    print(response)

#    response = requests.post(APPSYNC_API_ENDPOINT_URL, data=json.dumps({'query': query}), auth=auth, headers=headers)