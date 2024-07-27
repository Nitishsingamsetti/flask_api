from flask import Flask,redirect,url_for,request,render_template
app=Flask(__name__)
accounts={'12345':{'pin':'111','balance':3000},
          '6789':{'pin':'222','balance':5000},
          }

@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        accno=request.form['acc']
        pinno=request.form['pin']
        initial_balance=request.form.get('balance',0)
        if accno in accounts:
            return 'Account already exists'
        accounts[accno]={'pin':pinno,'balance':initial_balance}
        return 'Account created successfully'
    return render_template('atm.html')

@app.route('/data')
def data():
    accounts_lists=[{'account_id':accno,'balance':details['balance']} for accno,details in accounts.items()]
    return accounts_lists

@app.route('/alreadyacc',methods=['POST','GET'])
def alreadyacc():
    if request.method=='POST':
        accno=request.form['acc']
        pinno=request.form['pin']
        if accno in accounts:
            accounts_lists=[{'account_id':accno,'pinno':details['pin']} for accno,details in accounts.items()]
            if pinno==accounts_lists[0]['pinno']:
                return redirect(url_for('panel.html'))
            else:
                return 'Invalid pin',400
    
    return render_template('login.html')
            
    

app.run(debug=True,use_reloader=True)
        