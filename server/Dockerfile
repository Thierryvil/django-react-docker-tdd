FROM python:3.10-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app/

RUN apt-get update && apt-get install nginx vim -y --no-install-recommends

COPY nginx.default /etc/nginx/sites-available/default

RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log


RUN pip install --upgrade pip

COPY start-server.sh /app/
COPY ./requirements/prd.txt /app/

COPY /src/ /app/

RUN pip install -r prd.txt
RUN chown -R www-data:www-data /app

EXPOSE 8020

STOPSIGNAL SIGTERM

CMD ["/app/start-server.sh"]