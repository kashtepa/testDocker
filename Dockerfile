FROM python:3.11
LABEL authors="kristinashtepa"
WORKDIR /app

COPY requirements.txt ./

RUN pip config --user set global.progress_bar off
RUN pip install --no-cache-dir --progress-bar off -r requirements.txt
COPY . .
CMD [ "python3", "-m", "flask","run", "--host=0.0.0.0" ]