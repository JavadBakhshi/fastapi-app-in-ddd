FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN pip install -r requirements.txt

WORKDIR /src/entrypoint

EXPOSE 8000

CMD uvicorn fastapi_app:app --reload
