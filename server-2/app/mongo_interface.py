import pymongo

# Create/Access MongoClient to connect to Mongo Container
mongo_container = pymongo.MongoClient( 'mongo' , 27017 )
# mongo_container = pymongo.MongoClient( 'localhost' , 80 )

# Create/Access DB named minor-project
db_minor_project = mongo_container["minor-project"]

# Create/Access Collection named data_log
data_log = db_minor_project["data-log"]


def fetch():
    entry = data_log.find_one( {}, { '_id': False }, sort=[("timestamp", pymongo.DESCENDING)] )
    return entry