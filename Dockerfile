FROM python:3.10
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
CMD [ "python", "./plot_line.py" ]
CMD ["sh", "-c", "pytest -s test_sort.py --env=stag"]
