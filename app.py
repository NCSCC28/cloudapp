from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template for input form
form_html = '''
<!doctype html>
<html>
  <head><title>Add Two Numbers</title></head>
  <body>
    <h2>Add Two Numbers</h2>
    <form method="POST">
      <input type="number" name="num1" placeholder="Enter first number" required>
      <input type="number" name="num2" placeholder="Enter second number" required>
      <button type="submit">Add</button>
    </form>
    {% if result is not none %}
      <h3>Result: {{ result }}</h3>
    {% endif %}
  </body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def add_numbers():
    result = None
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        result = num1 + num2
    return render_template_string(form_html, result=result)

if __name__ == '__main__':
    app.run(debug=True)