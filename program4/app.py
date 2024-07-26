from flask import Flask,request,render_template,redirect,url_for
app=Flask(__name__)

@app.route('/index')
def home():
    # name=request.args.get('username')
    # return render_template('index.html',uname=name)
    name=int(request.args.get('marks'))
    return render_template('index.html',marks=name)    

@app.route('/result/<int:marks>')
def result(marks):
    if marks>=35 and marks<=100:
        return redirect(url_for('passes',marks1=marks))
    else:
        return redirect(url_for('failed',marks2=marks))

@app.route('/passes/<marks1>')
def passes(marks1):
    return f'he passed the exam with {marks1}'
@app.route('/failed/<marks2>')
def failed(marks2):
    return f'he failed the exam with {marks2}'

app.run(debug=True,use_reloader=True)




    