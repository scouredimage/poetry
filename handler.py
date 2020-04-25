import requests

def fortune(event, callback):
    r = requests.get('https://api.ef.gy/fortune')
    body = {
        "message": r.text,
        "input": event
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response
