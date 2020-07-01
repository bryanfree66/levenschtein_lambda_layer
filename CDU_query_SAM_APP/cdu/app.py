import json
from Levenshtein import distance as levenshtein_distance

def lambda_handler(event, context):
    """Get Levenshtein Distance Lambda Handler

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": levenshtein_distance(event['nombre'], event['x'])
        }),
    }
