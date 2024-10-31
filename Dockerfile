FROM python:3.12-bullseye

WORKDIR /app
COPY requirements.txt

RUN pip install --progress-bar off -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
COPY . .

CMD ["gunicorn", "-c", "/app/gunicorn.conf.py", "application.wsgi"]