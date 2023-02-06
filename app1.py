# Jinja-2 : web templatng system
# WSGI : Web Server Gateway Interface..
from flask import Flask,request,jsonify,render_template
# to retrive the request information

app = Flask(__name__)

#Route
# the default method type is get..
@app.route("/")
def hello_world():
    return render_template("index.html")

# we can write multiple routes
@app.route("/about_me")
def about_me():
    return "I am data scientist"

# Methods
@app.route("/math",methods=['POST'])
def math_operation():
    if (request.method == 'POST'):
        operation = request.form['operation']
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])
        
    if operation == "multiply":
        result = num1*num2
    elif operation == "add":
        result = num1+num2
    elif operation == "subtract":
        result = num1-num2
    else:
        result = num1/num2
    
    return "The Operation is {} and the result is {}.".format(operation,result)

@app.route("/multiply",methods=['POST'])
def multiply():
    if (request.method == 'POST'):
        operation = request.json['operation']
        num1 = request.json["num1"]
        num2 = request.json["num2"]
        result = num1*num2
    
    return jsonify("The Operation is {} and the result is {}.".format(operation,result))

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5001)