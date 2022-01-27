FROM python:3.9
# ADD . /todo
RUN mkdir /home/dev/ && mkdir /home/dev/code/

WORKDIR /home/dev/code/
# COPY requirements.txt /todo/
COPY . .
# RUN bundle install --full-index
RUN pip install pipenv && pipenv install requests && pipenv run app.py
CMD ["pipenv", "run"]
# FROM python:3.8

# RUN pip install pipenv

# ENV PROJECT_DIR /usr/local/bin/scrapping_data_eng

# WORKDIR ${PROJECT_DIR}

# COPY Pipfile Pipfile.lock ${PROJECT_DIR}/

# RUN pipenv install --system --deploy