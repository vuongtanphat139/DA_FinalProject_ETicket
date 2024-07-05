FROM python

RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY event_management_service/ /service/event_management_service/
WORKDIR /service/event_management_service
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=./ --grpc_python_out=./ ../protobufs/event_management.proto

EXPOSE 5002
# ENV FLASK_APP=app.py
ENTRYPOINT [ "python", "app.py"]