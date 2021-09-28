import uuid
import redis

def handler(event, context):
    r = redis.Redis(host=event['hostname'], port=6379, db=0)
    set_uuid = uuid.uuid4().hex
    r.set('uuid', set_uuid)
    get_uuid = r.get('uuid')
    if get_uuid == set_uuid:
        print("Success: Got value %s from redis" % (get_uuid))
    else:
        raise Exception("Error: Exception")

    return "Got value from redis: " + get_uuid