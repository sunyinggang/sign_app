FROM python:3.6
WORKDIR /usr/src/python/service

COPY requirements.txt ./
RUN pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

COPY . .

#前一个app是python启动的文件名，即app.py;后一个是flask项目里预启动的应用名
CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]
