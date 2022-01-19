# IFood MLE Test
The goal of the exercises below is to evaluate the candidate knowledge and problem solving expertise regarding the main development focuses for the iFood ML Platform team: MLOps and Feature Store development.

https://github.com/ifood/ifood-data-ml-engineer-test

#### Projeto: API para servir modelos com Flask, Gunicorn e Docker
#### Autor: George Rocha

Estrutura do projeto:

	.
	├── AutoML
	│   └── AutoML_h2o.ipynb
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
	└── READ.me

-------------------------------------------------------------

## Installation

Dependencies, this application requires:

	Python (>= 3.7)
	Docker (= 20.10.12)

Please follow the link bellow for more information on docker:
	
	https://docs.docker.com/engine/install/ubuntu/

-------------------------------------------------------------

## Alteração da url de origem dos dados

Para alterar as origens e destinos dos arquivos salvos, favor alterar o arquivo path.json onde:

	"modeldata": dados como informações salvas pelo AutoML, info, modelos, arquivos de teste,
	"procdata": dados como dados pre processados que serão utilizados para treinar e validar o modelo

Abaixo segue um exemplo:

	{	
	"modeldata":"https://s3model.blob.core.windows.net/modeldata/",
	"procdata":"https://s3model.blob.core.windows.net/prodata/"
	}

-------------------------------------------------------------

## Execução

No diretório /IFood_ML/IFood_API/flask_docker/ digite no terminal o seguinte comando:
	
	python setup.py

A última linha mostrará a porta que o docker fez o bind com o host.
Exemplo:

	CONTAINER ID   IMAGE          COMMAND             CREATED         STATUS                  PORTS                                         NAMES
	ac5bb0615e0a   flask_docker   "python3 exec.py"   2 seconds ago   Up Less than a second   0.0.0.0:49171->8000/tcp, :::49171->8000/tcp   serene_matsumoto


-------------------------------------------------------------
## Documentation

	https://app.swaggerhub.com/apis-docs/george53/MLS/1.0.0

-------------------------------------------------------------

## AutoML

Executar o notebook IFood_AutoML_h2o no diretório AutoML para criar um modelo, tempo para criação de um minuto na configuração atual.

-------------------------------------------------------------

## Exemplo:
Executar o notebook exemplo.ipynb IFood_ML/IFood_API/notebooks para enviar e receber os dados. 

Get: 
      
      pd.read_json(requests.get('http://0.0.0.0:49171/').content)

Post: 
      
      r = requests.post('http://0.0.0.0:49171/', data=data).content
      
      prediction = pd.read_json(r)

--------------------------------------------------------------

