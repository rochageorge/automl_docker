'''
- Machine Learning Serving - 
Recebe o nome do modelo e um dataframe no formato json, para realizar a previsão, 
como resultado, recebe a previsão em um formato json.
'''
import pandas as pd

import h2o
from h2o.automl import H2OAutoML

import json
import os

class get_model:
    '''Objeto para baixar pegar o modelo e realizar a previsão.'''
    
    def __init__(self, InitName:str, InitDataFrame:str):
        
        f = open ('path.json', "r")
        j = f.read()
        jl = json.loads(j)
        load_path = jl['modeldata'] + InitName
        
        self.path = load_path
        self.name = InitName
        self.df = InitDataFrame
        self.res = ''
        self.erro = '0'
        self.load_model()
    
    def load_model(self):
        '''Função para buscar o modelo, converter o json para o formato h2o e realizar a previsão'''
     
        try:
            h2o.init()
            
            os.system('wget '+self.path)
            loaded_model = h2o.load_model(path=self.name)
            os.system('rm '+self.name)
            
            pandas_df = pd.read_json(self.df)
            h2o_df = h2o.H2OFrame(pandas_df)
            
            if h2o_df.columns[0] == 'Unnamed: 0':
                pred_df = h2o_df.drop(h2o_df.columns[0], axis=1)
            else:
                pred_df = h2o_df
                
            self.res = loaded_model.predict(pred_df).as_data_frame()
           
        except Exception as erro:
            print(erro)
            self.erro = erro

