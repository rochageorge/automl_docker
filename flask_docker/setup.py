import os

os.system('docker image build -t flask_docker .')
os.system('docker container run -P -d flask_docker')
os.system('docker container ps')
