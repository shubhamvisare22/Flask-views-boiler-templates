from flask import Flask, jsonify, request
from flask.views import MethodView

app = Flask(__name__)

class TestAPI(MethodView):
    """
    TestAPI Class

    This class implements class-based views for handling various HTTP methods
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
view = TestAPI.as_view('json_api')

app.add_url_rule('/get', view_func=view, methods=['GET'])
app.add_url_rule('/post', view_func=view, methods=['POST'])
app.add_url_rule('/put/<int:id>', view_func=view, methods=['PUT'])
app.add_url_rule('/patch/<int:id>', view_func=view, methods=['PATCH'])
app.add_url_rule('/delete/<int:id>', view_func=view, methods=['DELETE'])

if __name__ == '__main__':
    app.run(debug=True)
