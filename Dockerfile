FROM python:3.9

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirement.txt

CMD ["python", "app.py"]
