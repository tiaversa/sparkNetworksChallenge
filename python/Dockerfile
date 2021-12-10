FROM amancevice/pandas:1.3.4

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#creating the work directory
WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt
# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "main.py"]
