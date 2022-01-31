FROM python:3.9
RUN mkdir /home/dev/ && mkdir /home/dev/code/
WORKDIR /home/dev/code/
COPY . .
RUN  pip install --upgrade pip &&  pip install pipenv && pipenv install --skip-lock
CMD ["pipenv", "run"]