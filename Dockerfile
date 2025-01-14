FROM python:3.9

WORKDIR /backend/src

COPY . .

CMD ["python", "./backend/src/index.py"]