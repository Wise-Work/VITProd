from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "CONNECTION_STRING"
client = MongoClient(uri, server_api=ServerApi('1'))
summaryColl = client["VITDemo"]["summary"]

def save_str_data(data):
    res_dict = {}
    res_dict["content"] = data
    summaryColl.insert_one(res_dict)

