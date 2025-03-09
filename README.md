# 🌟 Supermarket Microservice Project

This project is a microservice-based implementation of a supermarket system. It consists of multiple services built using different technologies and programming languages. The services are registered and discovered using a Eureka server.

## 📚  Project Structure

The project is composed of the following services:

1. **Eureka Server (Spring Boot, Maven)**
   - Service discovery server that allows other microservices to register themselves and discover other services.

2. **API Gateway (Spring Boot, Maven)**
   - Acts as a single entry point for all client requests and routes them to the appropriate microservices.

3. **Customer Service (Python)**
   - Manages customer-related operations such as customer registration, profile management, etc.

4. **Inventory Service (Spring Boot, Maven, Gradle)**
   - Handles inventory management, including product stock levels, updates, and queries.

5. **Order Service (Spring Boot, Maven, Gradle)**
   - Manages order processing, including order creation, status updates, and order history.

6. **Product Service (Spring Boot, Maven)**
   - Manages product-related operations such as product catalog, product details, etc.

## 📚 Prerequisites

Before running the project, ensure you have the following installed:

- Java JDK (for Spring Boot services)
- Python (for Customer Service)
- Maven (for building Java-based services)
- Gradle (optional, for services that support Gradle)
- Docker (optional, for containerization)

## 🚀 Setup and Running the Project

### 1. Eureka Server

1. Navigate to the `eureka-server-springboot` directory.
2. Build the project using Maven:
   ```
   mvn clean install
3. Run the Eureka Server
   ```
   mvn spring-boot:run
   ```
4. The Eureka server will be available at http://localhost:8761.


---

### 2. API Gateway

1. Navigate to the api-gateway-springboot directory.
2. Build the project using Maven:
   ```
   mvn clean install
3. Run the API Gateway
   ```
   mvn spring-boot:run
   ```
4. The API Gateway will be available at http://localhost:8080
    

---

   ### 3. Customer Service

1. Navigate to the customer-service-python directory
2. Install the required Python dependencies
   ```
   pip install -r requirements.txt
3. Run the Customer Service
   ```
   python app.py
   ```
4. The Customer Service will be available at http://localhost:5000.


---   

   ### 4. Customer Service

1. Navigate to the inventory-service-springboot directory.
2. Build the project using Maven or Gradle:
   ```
   mvn clean install
   ```
   or
   ```
   gradle build
   ```
4. Run the Inventory Service
   ```
   mvn spring-boot:run
   ```
   or
   ```
   gradle bootRun
   ```
5. The Inventory Service will be available at http://localhost:8081.

---


### 5. Order Service

1. Navigate to the order-service-springboot directory.
2. Build the project using Maven or Gradle:
   ```
   mvn clean install
   ```
   or
   ```
   gradle build
   ```
3. Run the Order Service
   ```
   mvn spring-boot:run
   ```
   or
   ```
   gradle bootRun
   ```
5. The Order Service will be available at http://localhost:8082.
    


---

### 6. Product Service

1. Navigate to the product-service-springboot directory.
2. Build the project using Maven 
   ```
   mvn clean install
   ```
3. Run the Product Service
   ```
   mvn spring-boot:run
   ```
5. The Product Service will be available at http://localhost:8083.
    

---

  ## 📚 License

This project is licensed under the [MIT License](LICENSE).

---
