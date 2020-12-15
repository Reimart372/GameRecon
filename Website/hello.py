from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''Hello, Country! <i>this is emphasized</i> 
    
    
    
    
    
   <p> bye''' 
