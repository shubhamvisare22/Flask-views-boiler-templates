from flask_restx import Resource, Api
from flask import jsonify, Flask

app = Flask(__name__)
api = Api(app)

class TestAPI(Resource):
    """
    TestAPI Resource

    This resource implements class-based views for handling various HTTP methods
    and returns JSON responses for each method.
    """

    def get(self):
        """Handles GET requests and returns a JSON response."""
        return jsonify({"message": "GET request received"})

    def post(self):
        """Handles POST requests and returns a JSON response."""
        return jsonify({"message": "POST request received"})

    def put(self, id):
        """Handles PUT requests with an ID parameter and returns a JSON response."""
        return jsonify({"message": f"PUT request received for id {id}"})

    def patch(self, id):
        """Handles PATCH requests with an ID parameter and returns a JSON response."""
        return jsonify({"message": f"PATCH request received for id {id}"})

    def delete(self, id):
        """Handles DELETE requests with an ID parameter and returns a JSON response."""
        return jsonify({"message": f"DELETE request received for id {id}"})

# Register the view for different endpoints
api.add_resource(TestAPI, "/get", methods=["GET"])
api.add_resource(TestAPI, "/post", methods=["POST"])
api.add_resource(TestAPI, "/put/<int:id>", methods=["PUT"])
api.add_resource(TestAPI, "/patch/<int:id>", methods=["PATCH"])
api.add_resource(TestAPI, "/delete/<int:id>", methods=["DELETE"])

if __name__ == "__main__":
    app.run(debug=True)

