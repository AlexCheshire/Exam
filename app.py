#Kozachenko O
import datetime
from datetime import date
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    today = datetime.date.today()
    month = today.month
    quad = month//4 + 1
    return quad

if __name__ =='__main__':
    app.run(debug=True,host='0.0.0.0')
