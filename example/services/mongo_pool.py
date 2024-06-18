from vercel_app import dev, test, prod
from pymongo.mongo_client import MongoClient
from django.conf import settings
import os

class MongoPool:

    def __init__(self, ):

        #vercel_app.test
        if  os.environ["DJANGO_SETTINGS_MODULE"] == 'vercel_app.dev':
            self.driver = dev.MONGO_DATABASE["DRIVER"]
            self.user = dev.MONGO_DATABASE["USER"]
            self.pwd = dev.MONGO_DATABASE["PASSWORD"]
            self.host = dev.MONGO_DATABASE["HOST"]
            self.port = dev.MONGO_DATABASE["PORT"]
            self.client = None
        else: 
            self.driver = test.MONGO_DATABASE["DRIVER"]
            self.user = test.MONGO_DATABASE["USER"]
            self.pwd = test.MONGO_DATABASE["PASSWORD"]
            self.host = test.MONGO_DATABASE["HOST"]
            self.port = None
            self.client = None 
       
      
    def connect(self, ):
        uri = "{0}://{1}:{2}@{3}:{4}/".format(self.driver, self.user , self.pwd,  self.host, self.port)
        if  self.port is None:
            uri = "{0}://{1}:{2}@{3}/".format(self.driver, self.user , self.pwd,  self.host)

        client = MongoClient(uri)
        try:
            client.admin.command('ping')
            self.client = client
            return True
        except Exception as e:
            return False
    
    def get_client(self,):
        return self.client
    
    def get_db(self):
        return self.client["fiocruz"]
    
    def get_collection(self, db):
        #db.createColletion("x")
        return db['teste']
          
     