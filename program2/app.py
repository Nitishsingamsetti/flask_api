from flask import Flask,render_template,url_for,redirect,request
app=Flask(__name__)

@app.route('/')
def home():
    return "welcome to first page"

@app.route('/second')
def second():
    return render_template('index.html')

@app.route('/age' ,methods=['GET','POST'])
def age():
    if request.method =='POST':
        age=request.form['age'] #this *age* is from name in input tag in html
    return render_template('age.html')
app.run(debug=True)

