# 
FROM python:3.9

# 
WORKDIR /back

# 
COPY ./requirements.txt /back/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /back/requirements.txt

# 
COPY ./backend /back/backend

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]