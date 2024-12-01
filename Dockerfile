FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt /app/

# 更新 apt 包索引并安装构建 mysqlclient 所需的依赖
RUN apt-get update && apt-get install -y \
    pkg-config \
    default-libmysqlclient-dev \
    build-essential \
    && pip install --progress-bar off -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . .

CMD ["gunicorn", "-c", "/app/gunicorn.conf.py", "puredrf.wsgi"]