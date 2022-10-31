#gets IMAGE from Docker Hube
#the image python:3.9 includes Linux + Python
FROM python:3.9  

#Points to "/app/" in the "Linux Image"
WORKDIR /app/ 

COPY requirements.txt /app/
COPY main_code.py /app/
COPY fct_utile.py /app/
COPY params.yaml /app/


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#entrypoint
CMD ["python", "main_code.py"]
