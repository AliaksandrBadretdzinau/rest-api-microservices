# rest-api-microservices

Project represents the next REST API microservices:
- User Service (detailed information is included in`./user-service`)

# Build

Once you cloned the project you may need Docker to build all services and run tests:

`docker-compose up`

As an alternative option you can go to each service's directory and run it separately:

`sh start.sh`

In both cases tests run and `uvicorn` server starts

Application is available on `http://0.0.0.0:8080/<service_name>` (e.g `http://0.0.0.0:8080/users`)

Service based API docs are available on `http://0.0.0.0:8080/<service_name>/docs` (Swagger UI)
