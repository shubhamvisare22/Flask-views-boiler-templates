from flask import Flask, jsonify, views

app = Flask(__name__)


class JSONAPI(views.View):
    """
    JSONAPI Class

    This class implements class-based views for handling various HTTP methods
    and returns JSON responses for each method.
    """

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

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


# Register the view for different endpoints: JSON responses
app.add_url_rule('/get', view_func=JSONAPI.as_view('json_get'), methods=['GET'])
app.add_url_rule('/post', view_func=JSONAPI.as_view('json_post'), methods=['POST'])
app.add_url_rule('/put/<int:id>', view_func=JSONAPI.as_view('json_put'), methods=['PUT'])
app.add_url_rule('/patch/<int:id>', view_func=JSONAPI.as_view('json_patch'), methods=['PATCH'])
app.add_url_rule('/delete/<int:id>', view_func=JSONAPI.as_view('json_delete'), methods=['DELETE'])

if __name__ == '__main__':
    app.run(debug=True)
