import clipboard 
from flask import Flask, request
from plyer import notification
from threading import Thread

app = Flask(__name__)
app.config['AUTH_HEADER_ENCODING'] = 'utf-8'
valid_users = {
    'admin': 'Password1',
    'admin2': 'Password2' 
}

@app.route('/topc', methods=['POST'])  
def post_request():
    auth = request.authorization
    if auth and auth.username in valid_users and valid_users[auth.username] == auth.password:
        data = request.get_data().decode()
        text = data
        clipboard.copy(text)   
        Thread(target=show_notification, args=(text,)).start() 
        return text
    else:
        return 'Authentication failed'

def show_notification(text):
    notification.notify(title="消息已复制!",message=text)  

if __name__ == '__main__': 
    app.run(host='127.0.0.1', port=8087)  

