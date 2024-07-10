from flask import Flask, render_template
from flask.views import MethodView

app = Flask(__name__)

class TestAPI(MethodView):
    """
    TestAPI Class

    This class implements class-based views for handling various HTTP methods
    and returns rendered HTML templates for each method.
    """

    def get(self):
        """Handles GET requests and returns a rendered HTML template."""
        return render_template('get.html', data={"message": "GET request received"})

    def post(self):
        """Handles POST requests and returns a rendered HTML template."""
        return render_template('post.html', data={"message": "POST request received"})

    def put(self, id):
        """Handles PUT requests with an ID parameter and returns a rendered HTML template."""
        return render_template('put.html', data={"message": f"PUT request received for id {id}"})

    def patch(self, id):
        """Handles PATCH requests with an ID parameter and returns a rendered HTML template."""
        return render_template('patch.html', data={"message": f"PATCH request received for id {id}"})

    def delete(self, id):
        """Handles DELETE requests with an ID parameter and returns a rendered HTML template."""
        return render_template('delete.html', data={"message": f"DELETE request received for id {id}"})

# Register the view for different endpoints
view = TestAPI.as_view('html_api')

app.add_url_rule('/get', view_func=view, methods=['GET'])
app.add_url_rule('/post', view_func=view, methods=['POST'])
app.add_url_rule('/put/<int:id>', view_func=view, methods=['PUT'])
app.add_url_rule('/patch/<int:id>', view_func=view, methods=['PATCH'])
app.add_url_rule('/delete/<int:id>', view_func=view, methods=['DELETE'])

if __name__ == '__main__':
    app.run(debug=True)
