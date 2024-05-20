
import pandas as pd
import os

class CreateCSVFILE:
    
    def __init__(self, file):
        self._file = file
        self._buffer = ''
    
    def create_buffer_csv(self, ):
          df = pd.read_excel( self._file,header=1)
          csv = df.to_csv(index=False)
          self._buffer = csv
    
    def create_path(self, path):
         csv_path = os.path.join(path, 'output.csv')
         
         '''
         
         if not os.path.exists(path):
                os.makedirs(path)
         '''

         
         with open(csv_path, 'w') as csv_file:
                csv_file.write(self._buffer)