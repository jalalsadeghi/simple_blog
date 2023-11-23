FROM python:3.11.4

ENV PYTHONUNBUFFERED 1
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

COPY ./requirements /requirements
COPY ./scripts /scripts
COPY ./src /src

WORKDIR src

EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/python -m pip install --upgrade pip

RUN /py/bin/pip install -r /requirements/development.txt

RUN chmod -R +x /scripts && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    adduser --disabled-password --no-create-home backend && \
    chown -R backend:backend /vol &&\
    chmod -R 755 /vol

ENV PATH="/scripts:/py/bin:$PATH"

USER backend

CMD ["run.sh"]
