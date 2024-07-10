## Distributed Application - Final Project - Team 02 - TicPick
Member's informations:
- 20120133: Phạm Lê Hoài Minh
- 20120257: Đinh Hoàng Bảo Châu
- 20120341: Phan Thiện Nhân (leader)
- 20120344: Vương Tấn Phát

### Running
Create database connection and Authentication service
```bash
docker compose up
``` 

Run API Gateway:
```bash
cd .\api_gateway
python app.py
``` 

Run Event service:
```bash
cd .\event_management_service
python app.py
``` 

Run Ticket service:
```bash
cd .\ticket_management_service
python app.py
``` 

Run Frontend:
```bash
cd .\frontend
yarn install
yarn dev
``` 

### Notes:
Run the following command to generate protofile:
```bash
python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/recommendations.proto
``` 
