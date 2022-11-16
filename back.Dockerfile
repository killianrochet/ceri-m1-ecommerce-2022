FROM python:3

COPY requirements.txt ./

WORKDIR backend/

RUN python -m pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install -e .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
