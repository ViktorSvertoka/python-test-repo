## Prerequisites:
- Java JDK version 17+ should be installed in the system

Check it here https://www.oracle.com/java/technologies/downloads/#java17
or here https://adoptium.net/temurin/releases/

## How to Build:
To build the application execute the following commands in the project folder (where pom.xml and mvnw are located). Before building, set permissions on the ./mvnw file in the cloned project directory:
```
chmod 755 ./mvnw
```{{exec}}

```bash
./mvnw clean package # this will build the project
```
For the first time it will download and install Maven version configured in the project settings (`v.3.8.6`)
Next time the cached version will be used without redownloading.

After the build is completed, the folder `/target` will be created with a compiled `.jar` ready to be launched.

## How to Run:
Now you can launch the server for example at port `8080`
(if the option `--server.port=8080` is not provided the default port is `8080`):
```bash
java -jar ./target/*.jar --server.port=8080
```
It may take up to around 15 sec for the server to start

## How to check the server is available
execute
```bash
curl -s 'http://localhost:8080/actuator/health'
```
It should yield the following response:
```
{"status":"UP"}
```

## The DataBase

The database is managed by an embedded H2 engine (v.2.1.214),
it is stored in a file `./productsDB.mv.db`

The credentials to access the DB are:
  - JDBC URL = jdbc:h2:file:./productsDB,
  - user name = sa,
  - password = \<empty string\>

The initial content of the DB is created by the sql script `./resources/sql/data/sql`,
it ensures the five products are inserted/updated with the original prices
(the ids may differ if the products were once deleted).
```JSON
[
  {"id":"1", "name":"Sugar", "price":32.00},
  {"id":"2", "name":"Salt", "price":19.00},
  {"id":"3", "name":"Bread", "price":20.00},
  {"id":"4", "name":"Butter", "price":62.00},
  {"id":"5", "name":"Milk", "price":32.00}
]
```

When the server is running you can access the DB with web browser at http://localhost:8080/h2
Use the credentials given above to connect.

## The available endpoints

Example of application functionality is provided in the file with requests: `./simplecrud-endpoints.http`

Some basic information about the available endpoints is provided by Swagger at: http://localhost:8080/swagger-ui/index.html

## The logs

The logs are created in the `./logs` subfolder. They can be accessed via the endpoint:
http://localhost:8080/actuator/logfile
