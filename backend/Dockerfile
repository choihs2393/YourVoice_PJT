FROM python:3.8.5

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY ./ReMu /ReMu  
WORKDIR /ReMu  
RUN pip install -r /ReMu/requirements.txt  
RUN chmod 755 /ReMu/start  
EXPOSE 8000  

ENTRYPOINT ["/ReMu/start"] 