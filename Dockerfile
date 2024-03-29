FROM python:3.10

RUN useradd -ms /bin/bash user
USER user
WORKDIR /home/user

COPY requirements.txt .
RUN pip install -r requirements.txt && rm requirements.txt

COPY my_code .

EXPOSE 10000

ENTRYPOINT ["python", "main.py"]