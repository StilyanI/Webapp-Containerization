FROM python:3.12-slim

RUN pip install flask

COPY . . 

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]