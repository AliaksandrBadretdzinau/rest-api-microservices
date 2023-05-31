# rest-api-microservices

Project represents the next REST API microservices:
- User Service (detailed information is included in`./user-service`)

## Build

### Using Docker Compose

Once you cloned the project you may need Docker to build all services and run tests

To start the project just simply run the next command

`docker-compose up`

### Building specific service as an alternative (without Docker)

As an alternative option you can go to each service's directory and run it separately

Lets run `User Service` which is located in `./user-service` directory

#### Steps to run

Go to `User Service` directory:

`cd ./user-service`

Active virtual environment:

`python -m venv venv`

Install dependencies:

`pip install -r requirements.txt`

Run tests and start server:

`sh start.sh`

In both cases tests run and `uvicorn` server starts

Application is available on `http://0.0.0.0:8080/<service_name>` (e.g `http://0.0.0.0:8080/users`)

Service based API docs are available on `http://0.0.0.0:8080/<service_name>/docs` (Swagger UI)
