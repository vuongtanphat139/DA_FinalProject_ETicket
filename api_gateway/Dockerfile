FROM python

RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY api_gateway/ /service/api_gateway/
WORKDIR /service/api_gateway
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

EXPOSE 5001
# ENV FLASK_APP=app.py
ENTRYPOINT [ "python", "app.py"]