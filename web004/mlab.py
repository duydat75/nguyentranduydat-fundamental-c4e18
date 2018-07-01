import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds121301.mlab.com:21301/c4e

host = "ds121301.mlab.com"
port = 21301
db_name = "c4e"
user_name = "dat123"
password = "dat123"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())