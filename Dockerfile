FROM python:3.10
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /plot_line.py
CMD [ "python", "./plot_line.py" ]
