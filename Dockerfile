FROM python:3.6

ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

ENTRYPOINT [ "bash", "scripts/wait-for-db.sh" ]
CMD ["python", "-u", "main.py"]
