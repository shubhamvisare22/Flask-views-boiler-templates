from flask import Flask, views, render_template

app = Flask(__name__)


class HTMLAPI(views.View):
    """
    HTMLAPI Class

    This class implements class-based views for handling various HTTP methods
    and returns rendered HTML templates for each method.
    """

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    def get(self):
        """Handles GET requests and returns a rendered HTML template."""
        return render_template('get.html', data={"message": "GET request received"})

    def post(self):
        """Handles POST requests and returns a rendered HTML template."""
        return render_template('post.html', data={"message": "POST request received"})

    def put(self,id):
        """Handles PUT requests and returns a rendered HTML template."""
        return render_template('put.html', data={"message": f"PUT request received for id {id}"})

    def patch(self,id):
        """Handles PATCH requests and returns a rendered HTML template."""
        return render_template('patch.html', data={"message": f"PATCH request received for id {id}"})

    def delete(self,id):
        """Handles DELETE requests and returns a rendered HTML template."""
        return render_template('delete.html', data={"message": f"DELETE request received for id {id}"})


# Register the view for different endpoints: HTML render
app.add_url_rule('/get', view_func=HTMLAPI.as_view('html_get'), methods=['GET'])
app.add_url_rule('/post', view_func=HTMLAPI.as_view('html_post'), methods=['POST'])
app.add_url_rule('/put/<int:id>', view_func=HTMLAPI.as_view('html_put'), methods=['PUT'])
app.add_url_rule('/patch/<int:id>', view_func=HTMLAPI.as_view('html_patch'), methods=['PATCH'])
app.add_url_rule('/delete/<int:id>', view_func=HTMLAPI.as_view('html_delete'), methods=['DELETE'])

if __name__ == '__main__':
    app.run(debug=True)
