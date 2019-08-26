import uuid


def gen_uuid(salt):
    res = uuid.uuid3(uuid.NAMESPACE_URL, salt)
    return res.hex