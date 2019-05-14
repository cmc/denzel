FROM python:3.7.3
LABEL authors="cmc,maus"
WORKDIR /src/
COPY requirements.txt ./
RUN apt-get update -y
RUN apt-get install -y libfuzzy-dev build-essential libffi-dev python3 python3-dev python3-pip 
RUN pip3 install --no-cache-dir -r requirements.txt
COPY config ./config
COPY workers ./workers
COPY lib ./lib
COPY api ./api
COPY *.py ./
COPY *.sh ./
CMD [ "/bin/sh", "/src/entrypoint.sh" ]
