import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds263710.mlab.com:63710/muadongkhonglanh-c4e18

host = "ds263710.mlab.com"
port = 63710
db_name = "muadongkhonglanh-c4e18"
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