FROM python

WORKDIR /app

COPY . .

RUN pip install .

EXPOSE 8000

ENTRYPOINT [ "/app/entrypoint.sh" ]
