from vercel_app import dev
from pymongo.mongo_client import MongoClient

class MongoPool:

    def __init__(self, ):
        self.driver = dev.MONGO_DATABASE["DRIVER"]
        self.user = dev.MONGO_DATABASE["USER"]
        self.pwd = dev.MONGO_DATABASE["PASSWORD"]
        self.host = dev.MONGO_DATABASE["HOST"]
        self.port = dev.MONGO_DATABASE["PORT"]
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
        #db.createColletion("teste")
        return db['teste']
          
     