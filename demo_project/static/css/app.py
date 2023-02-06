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
    
    return render_template("results.html",result = result)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5001)




### Assignment
# item cost
# 5-6 items
# 15% discount
# value after the discount

# 1000 = 10%
# 1000,2000 = 20%
# 2000,3000 = 30%

# print the price...