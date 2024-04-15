from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the simple web server!"

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name', 'World')
    # Potential security risk: Reflected Cross-Site Scripting (XSS)
    return render_template_string(f'Hello, {name}!')

if __name__ == '__main__':
    app.run(debug=True)
