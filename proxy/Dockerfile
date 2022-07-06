FROM python:3.9.1
RUN apt-get update && apt-get -y install cron vim
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY crontab /etc/cron.d/crontab
COPY . .
RUN chmod 0644 /etc/cron.d/crontab
RUN /usr/bin/crontab /etc/cron.d/crontab

# run crond as main process of container
CMD ["cron", "-f"]