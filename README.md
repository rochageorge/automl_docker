# IFood MLE Test
The goal of the exercises below is to evaluate the candidate knowledge and problem solving expertise regarding the main development focuses for the iFood ML Platform team: MLOps and Feature Store development.

https://github.com/ifood/ifood-data-ml-engineer-test

# Projeto: API para servir modelos 
# Autor: George Rocha
# Data: 19/01/2022

** Alteração da url de origem dos dados----------------------

Para alterar as origens e destinos dos arquivos salvos, favor alterar o arquivo path.json onde:

	"modeldata": dados como informações salvas pelo AutoML, info, modelos, arquivos de teste,
	"procdata": dados como dados pre processados que serão utilizados para treinar e validar o modelo

Abaixo segue um exemplo:
{
"modeldata":"https://s3model.blob.core.windows.net/modeldata/",
"procdata":"https://s3model.blob.core.windows.net/prodata/"
}

** Estas informações são as informações de para dados de treinamentos e para armazenamento dos dados dos modelos.

** Execução----------------------------------------

No diretório /IFood_ML/IFood_API/flask_docker/ digite no terminal o seguinte comando:
	
python setup.py

A última linha mostrará a porta que o docker fez o bind com o host.
Exemplo:

CONTAINER ID   IMAGE          COMMAND             CREATED         STATUS                  PORTS                                         NAMES
ac5bb0615e0a   flask_docker   "python3 exec.py"   2 seconds ago   Up Less than a second   0.0.0.0:49171->8000/tcp, :::49171->8000/tcp   serene_matsumoto


-------------------------------------------------------------

AutoMl-------------------------------------------------------

Executar o notebook IFood_AutoML_h2o no diretório AutoML para criar um modelo, 
tempo para criação de um minuto na configuração atual.

-------------------------------------------------------------

Exemplo:
Executar o notebook exemplo.ipynb IFood_ML/IFood_API/notebooks para enviar e receber os dados. 

Get: 
      pd.read_json(requests.get('http://0.0.0.0:49171/').content)

Post: 
      r = requests.post('http://0.0.0.0:49171/', data=data).content
      prediction = pd.read_json(r)

--------------------------------------------------------------
