import json

import pytest
from mock import Mock, sentinel

from CDU_query_SAM_APP.cdu import app


@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""

    return {
        "body": '{ "nombre": "EMIGDIO MENDEZ FLOREZ", "x": "EMIGDIO MENDEZ FLORES"}',
        "resource": "/{proxy+}",
        "requestContext": {
            "resourceId": "cdu-query",
            "apiId": "pbpxzw7yii",
            "resourcePath": "/{proxy+}",
            "httpMethod": "GET",
            "requestId": "ab1c9cba-cb89-4a9e-a166-5c723d7ebbe7",
            "accountId": "383957508710",
            "identity": {
                "apiKey": "",
                "userArn": "arn:aws:iam::383957508710:user/bryan",
                "cognitoAuthenticationType": "",
                "caller": "",
                "userAgent": "Custom User Agent String",
                "user": "",
                "cognitoIdentityPoolId": "",
                "cognitoIdentityId": "",
                "cognitoAuthenticationProvider": "",
                "sourceIp": "127.0.0.1",
                "accountId": "",
            },
            "stage": "prod",
        },
        "queryStringParameters": "",
        "headers": {
        },
        "pathParameters": {"proxy": "/cdu_query"},
        "httpMethod": "GET",
        "path": "/cdu_query",
    }


def test_lambda_handler(apigw_event, mocker):

    ret = app.lambda_handler(apigw_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "result" in ret["body"]
    assert data["result"] == 1

