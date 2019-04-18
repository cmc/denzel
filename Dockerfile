FROM python:3.6.6
LABEL authors="cmc,maus"
WORKDIR /src/
COPY requirements.txt ./
RUN apt-get update -y
RUN apt-get install -y libfuzzy-dev build-essential libffi-dev python3 python3-dev python3-pip

RUN pip3 install --no-cache-dir -r requirements.txt
COPY config ./config
COPY *.py ./
ADD  ./ .
CMD [ "python3", "comparator.py" ]
