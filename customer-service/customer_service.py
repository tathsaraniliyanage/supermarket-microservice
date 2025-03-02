# from flask import Flask, jsonify 

# app= Flask(__name__)
# CONTEXT_PATH = "/customer-server"
# SERVICE_PORT = 5000

# @app.route(f'{CONTEXT_PATH}/customers', methods=["GET"])
# def get_customer():
#     customers = [
#         {"id":1,"name":"john doe"},
#         {"id":2,"name":"ama"},
#     ]
#     return jsonify(customers)

# app.run(port= SERVICE_PORT)


from flask import Flask, jsonify
import py_eureka_client.eureka_client as eureka_client

# pip install flask py_eureka_client

# create flask application
app = Flask(__name__)

CONTEXT_PATH = '/customer-service'
SERVICE_PORT = 5000
EUREKA_SERVICE = "http://localhost:8761/eureka/"

eureka_client.init(
    eureka_server=EUREKA_SERVICE,
    app_name="CUSTOMER_SERVICE",
    instance_port=SERVICE_PORT
)

@app.route(f'{CONTEXT_PATH}/customers', methods=['GET'])
def get_customers():
    customers = [
        {'id': 1, 'name': 'John Doe'},
        {'id': 2, 'name': 'Nethmi Umaya'}
    ]
    return jsonify(customers)

if __name__ == '__main__':
    app.run(port=SERVICE_PORT)