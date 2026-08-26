FROM python:3.10.2-alpine3.15
WORKDIR /app
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
COPY scrape_hint.py /app/scrape_hint.py
CMD ["python", "scrape_hint.py"]
