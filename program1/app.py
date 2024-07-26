from flask import Flask,redirect,url_for
app=Flask(__name__) 
# For Flask class--app is an object that is created
@app.route('/')
def home():
    return 'hello duniya'
    #print('hello duniya')-- this raises an error

@app.route('/first')
def home1():
    return '<h1>Tell me your name<h1>'

@app.route('/result/<marks>') #marks will be in string form,should be converted to integer
def result(marks):
    print(type(marks))
    if int(marks)>=35:
        return 'pass'
    else:
        return 'fail'
#--------------------------------------------------------------------------------------------------------------------  
#dynamic routing
@app.route('/grade/<marks>')
def grade(marks):
    print(type(marks))
    
    if int(marks) in range(90,101):
        return 'A'
    elif int(marks) in range(80,90):
        return 'B'
    elif int(marks) in range(70,80):
        return 'C'
    elif int(marks) in range(60,70):
        return 'D'
    elif int(marks) in range(0,60):
        return 'F'

#-----------------------------------------------------------------------------------------------------------------
#redirecting routing
@app.route('/voter/<int:age>') #with int: the age is directly converted to integer
def voter(age):
    if age>=18:
        return redirect(url_for('valid')) #redirect()--should be imported from flask
    else:
        return redirect('http://127.0.0.1:5000/invalid')
@app.route('/valid')
def valid():
    return 'eligible for voting'
@app.route('/invalid')
def invalid():
    return 'this person is not eligible'
app.run(debug=True)