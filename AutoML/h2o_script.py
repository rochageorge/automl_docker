import pandas as pd
import json
import os
import re

from datetime import datetime

os.system('pip install h2o')

import h2o
from h2o.automl import H2OAutoML

j = open('param_h2o.json', 'r').read()
param = json.loads(j)

source_path = param['sourcePath']
saving_path = param['savingPath']
target = param['target']
exclude_algos = [param['excludeAlgos']]
max_models = int(param['maxModels'])
seed = int(param['seed'])
max_training_time = int(param['maxTrainingTime'])
classification = param['classification']

h2o.init()

df = h2o.import_file(path=source_path)
train, test = df.split_frame(ratios=[0.8], seed = seed)

aml = H2OAutoML(
    max_models = max_models, 
    max_runtime_secs = max_training_time, 
    exclude_algos = exclude_algos, 
    balance_classes=True, 
    seed = seed
)

aml.train(training_frame = train, y = target)

best_model = aml.get_best_model()

model_info = best_model.model_performance(test)

local_path = os.getcwd()+'/'

model_path_1 = h2o.save_model(model=best_model,path=local_path, force=True)

best_model = model_path_1.split('/')[int(len(model_path_1.split('/'))-1)]

model_id = best_model.split('_')[-2]+best_model.split('_')[-1]
model_name = best_model.split('_')[0]+'_'+model_id
model_date = best_model.split('_')[-2]

test_name = 'test_' + model_id
train_name = 'train_' + model_id

test.as_data_frame().convert_dtypes().to_pickle(test_name + '.csv')
train.as_data_frame().convert_dtypes().to_pickle(train_name + '.csv')

model_path = saving_path + model_name

try:
    aic = model_info.aic()
except:
    aic = str(0)
    
info1 = {
        'id': str(model_id),
        'name': str(model_name),
        'date': datetime. strptime(model_date, '%Y%m%d'),
        "h2o_version": str(h2o.__version__),
        "seed": str(seed),
        "target": str(target),
        "train_path": str(saving_path + test_name+ '.csv'),
        "test_path": str(saving_path + train_name+ '.csv'),
        'model_path':str(saving_path + model_name),
        'max_runtime': str(aml.max_runtime_secs),
        'classification':str(classification),
        'columns':str(list(aml.varimp().index)),
        'varimp':str(aml.varimp().to_json())
}


if classification == 'False':
    info2 = {
        'metrics':{
            'mse':str(model_info.mse()),
            'rmse':str(model_info.rmse()),
            'mae':str(model_info.mae()),
            'rmsle':str(model_info.rmsle()),
            'r2':str(model_info.r2()),
            'mean_resid_deviance':str(model_info.mean_residual_deviance()),
            'null_degrees_of_freedom':str(model_info.null_degrees_of_freedom()),
            'resid_degrees_of_freedom':str(model_info.residual_degrees_of_freedom()),
            'null_deviance':str(model_info.null_deviance()),
            'residual_deviance':str(model_info.residual_deviance()),
            'aic':aic,
        }
    }
    
info = info1.copy()
info.update(info2)

info_new = pd.DataFrame([info])

info_path = local_path + 'info.csv'

try:
    info_old = pd.read_csv(info_path)
    if info_old.columns[0] == 'Unnamed: 0':
        info_old = info_old.drop(info_old.columns[0], axis=1)
    
    info_save = pd.concat([info_old, info_new])
    info_save.to_csv(info_path, index = False)
except:
    info_new.to_csv(info_path, index = False)
    
os.rename(model_path_1, local_path + model_name)