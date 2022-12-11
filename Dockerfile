FROM python:3

WORKDIR /home

COPY . .

RUN apt update -y
RUN apt install -y /home/google-chrome-stable_current_amd64.deb
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python3", "main.py" ]