FROM python:3.7
COPY . .
RUN pip install -r requirements.txt --cache-dir=.pip_cache
CMD ["uvicorn", "manager:app"]