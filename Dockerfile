FROM python:3.7
COPY . .
RUN pip install -r requirements.txt --cache-dir=.pip_cache
CMD ["uvicorn", "manager:app", "--host", "0.0.0.0", "--port", "8001"]