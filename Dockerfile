FROM python:3.6.6
LABEL authors="cmc,maus"
WORKDIR /src/
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update -y
RUN apt-get install -y python3-ssdeep ssdeep python-ssdeep libfuzzy-dev
#COPY config ./config
COPY *.py ./
ADD  ./ .
CMD [ "python", "comparator.py" ]
