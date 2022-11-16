FROM python:3.9
WORKDIR /app/ 
COPY requirments.txt /app/
COPY main_code.py /app/
COPY fct_utile.py /app/
COPY params.yaml /app/
RUN pip install --upgrade pip
RUN pip install -r requirments.txt
#entrypoint
CMD ["python", "main_code.py"]
