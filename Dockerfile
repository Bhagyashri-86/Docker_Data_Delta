FROM python:3.10

WORKDIR /app
COPY requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
COPY ml ./m1/app/

RUN python m1/train.python
EXPOSE 8000
CMD ["sh","-c","unicorn app.main:app --host 0.0.0.0 --port ${port:-8000}"]