FROM python:3.10
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY from mcr.microsoft.com/python/aspnet:3.1-buster-slim
CMD [ "python", "./plot_line.py" ]
