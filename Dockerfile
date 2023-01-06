# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt
COPY entrypoint.sh ./entrypoint.sh
RUN chmod +x entrypoint.sh
#
RUN pip install jupyter google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app

ENV PORT=80

ENTRYPOINT ["sh", "entrypoint.sh"]
# 
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "${PORT}"]
#slt