FROM python:3.10
WORKDIR /usr/src/app
COPY requirements.txt .
COPY test_sorting.py .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
CMD [ "python", "./plot_line.py" ]
CMD [ "python", "./test_sorting.py" ]
