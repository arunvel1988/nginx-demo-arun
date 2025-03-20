#pip install flask

#nohup python3 app.py > flask.log 2>&1 &

# sudo rm /etc/nginx/sites-enabled/default


from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is my Flask app running behind Nginx!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
