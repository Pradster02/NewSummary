from flask import Flask, jsonify, request
import Summarizer

app = Flask(__name__) 
  
  
@app.route('/', methods=['GET']) 
def helloworld(): 
    if(request.method == 'GET'): 
        return Summarizer.summary(request.args.get('p'))[0]["summary_text"]
  
  
if __name__ == '__main__': 
    app.run(debug=True) 