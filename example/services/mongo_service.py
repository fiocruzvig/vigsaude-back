
import pandas as pd

class MongoService:
    
    def __init__(self):
        pass

    def insert(self, file, collection):
        excel_data_df = pd.read_excel(file)
        data = excel_data_df.to_dict(orient='records')
        collection.insert_many(data)