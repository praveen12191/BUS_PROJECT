FROM python:3
WORKDIR /bus 
COPY requirements.txt .
RUN pip3 install --upgrade pip 
RUN pip3 install -r requirements.txt
COPY . /bus
#copying the project 