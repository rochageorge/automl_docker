# IFood MLE Test
The goal of the exercises below is to evaluate the candidate knowledge and problem solving expertise regarding the main development focuses for the iFood ML Platform team: MLOps and Feature Store development.

https://github.com/ifood/ifood-data-ml-engineer-test

#### Project: API for model serving with Flask, Gunicorn and Docker
#### Author: George Rocha
#### Status: In development


Project's structure:

	.
	├── AutoML
	│   ├── h2o_notebook.ipynb
	│   ├── h2o_script.py
	│   ├── param_h2o.json
	├── AWS_infra
	│   └── AWS Infrastructure.pdf
	├── IFood_API
	│   ├── docs
	│   │   ├── Document Live.txt
	│   │   └── Document Static.html
	│   ├── flask_docker
	│   │   ├── Dockerfile
	│   │   ├── exec.py
	│   │   ├── mls.py
	│   │   ├── my_app.py
	│   │   ├── path.json
	│   │   ├── requirements.txt
	│   │   ├── setup.py
	│   │   └── wsgi.py
	│   └── notebook
	│       └── example.ipynb
	└── README.md

-------------------------------------------------------------

## Installation

Dependencies, this application requires:

	Python (>= 3.7)
	Docker (= 20.10.12)

Please follow the link bellow for more information on docker:
	
	https://docs.docker.com/engine/install/ubuntu/

-------------------------------------------------------------

## URL source

To change the source and saving path, please change the path.json path:

	"modeldata": URL or path where AutoML files will be saved, such as binary models, info, test and train csv files.
	"procdata": URL or path where pre processed data will be saved to feed the models for training and testing.

Example:

	{	
	"modeldata":"https://s3model.blob.core.windows.net/modeldata/",
	"procdata":"https://s3model.blob.core.windows.net/prodata/"
	}

-------------------------------------------------------------

## Execution

Inside the folder /IFood_ML/IFood_API/flask_docker/ open a terminal and type the command bellow:
	
	python setup.py

The last line will show the docke's binding port with the host.

Example:

	CONTAINER ID   IMAGE          COMMAND             CREATED         STATUS                  PORTS                                         NAMES
	ac5bb0615e0a   flask_docker   "python3 exec.py"   2 seconds ago   Up Less than a second   0.0.0.0:49171->8000/tcp, :::49171->8000/tcp   serene_matsumoto

The binding port is 0.0.0.0:49171 in the example above.

-------------------------------------------------------------
## Documentation

	https://app.swaggerhub.com/apis-docs/george53/MLS/1.0.0

-------------------------------------------------------------

## AutoML

To use the H2O AutoML for model creation, please alter the parameters in the param_h2o.json and then execute the following command:
	
	python h2o_script.py

You can also use the notebook to create the models, it also uses the param_h2o.json file.

Example (param_h2o.json):
	
	{
	"sourcePath" : "https://s3model.blob.core.windows.net/prodata/merged_proc_data.csv", <- Local onde estão os dados pre processados.
	"savingPath" : "https://s3model.blob.core.windows.net/modeldata/", <- Local onde salvar os arquivos gerados.
	"target" : "average_ticket", <- Coluna desejada para previsão
	"algos": ["DRF", "GLM", "XGBoost", "GBM", "DeepLearning", "StackedEnsemble"], <- Algoritmos disponíveis.
	"maxModels" : "10", <- Máximo de modelos para comparaçao.
	"seed" : "4", <- Seed para reprodutividade.
	"maxTrainingTime" : "45", <- Tempo máximo de treinamento em segundos.
	}

-------------------------------------------------------------

## Example:

Execute the exemplo.ipynb notebook on the IFood_ML/IFood_API/notebooks to send and receive data. 

Get: 
      
      pd.read_json(requests.get('http://0.0.0.0:49171/').content)

Post: 
      
      r = requests.post('http://0.0.0.0:49171/', data=data).content
      
      prediction = pd.read_json(r)

--------------------------------------------------------------

