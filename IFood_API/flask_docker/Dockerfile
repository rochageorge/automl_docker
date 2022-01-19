# start by pulling the python image
FROM ubuntu:20.04

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

#RUN apt-get update && apt-get upgrade -y

RUN apt update 

RUN apt install openjdk-8-jre-headless -y

RUN apt clean

RUN apt install wget -y

RUN apt install python3-pip -y 

RUN pip install --upgrade pip 

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

EXPOSE 8000

# configure the container to run in an executed manner
ENTRYPOINT [ "python3" ]

CMD ["exec.py" ]
