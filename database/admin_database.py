import pymongo, os
from config import DB_URI, DB_NAME


dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]

admin_data = database['admins']


async def full_adminbase():
    admin_docs = admin_data.find()
    admin_ids = []
    for doc in admin_docs:
        admin_ids.append(doc['_id'])
    return admin_ids

async def add_admin(admin_id, admin_level):
    admin_data.insert_one({'_id': admin_id,'level':admin_level})
    return

async def present_admin(admin_id):
    found = admin_data.find_one({'_id': admin_id})
    if found:
        return True
    else:
        return False

async def del_admin(admin_id):
    admin_data.delete_one({'_id': admin_id})
    return
