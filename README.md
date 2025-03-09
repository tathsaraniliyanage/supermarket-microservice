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

## Prerequisites

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
   ```bash
   mvn clean install


  ## 📚 License

This project is licensed under the [MIT License](LICENSE).

---
