## Python Microservices Demo
This is from some tutorial I followed, you can check it out here:
https://realpython.com/python-microservices-grpc/

### Installation
Just make sure you got docker and docker-compose installed and running. Then run the following command on the root of the project:
```bash
docker-compose up -d 
``` 
python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/recommendations.proto
flask run --host=0.0.0.0 --debug