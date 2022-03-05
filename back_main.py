from flask import Flask, render_template

app = Flask(__name__)

# host : Defaults to 127.0.0.1 (localhost). Set to ‘0.0.0.0’ to have server available externally
# port : 5000 (default)

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]

server_message = {'client':'message'}

client_message = {'server':'message'}

@app.route('/')
def index():
   return render_template("index.html",message=messages)

@app.route('/server')
def server():
   return render_template("server.py",message=messages)

@app.route('/client')
def client():
   return render_template("client.py",message=messages)

if __name__ == '__main__':
    host = "0.0.0.0" 
    port = 5000
    debug = True
    app.run(host, port, debug)