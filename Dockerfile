FROM python:3.7
ENV PYTHONUNBUFFERED 1

# 1. install pipenv and create an entrypoint
RUN pip install pipenv

WORKDIR /app

# 4. copy the Pipfile and install it
COPY Pipfile /app/Pipfile
RUN pipenv lock -r >> requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5. add your own code
# <--- own code here

#COPY . /app/app

CMD ./manage.py runserver 0.0.0.0:8000