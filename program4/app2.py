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
                return redirect(url_for('panel',accno=accno,pinno=pinno))
            else:
                return 'Invalid pin',400
    
    return render_template('login.html')

@app.route('/panel/<accno>/<pinno>')
def panel(accno,pinno):
    return render_template('options.html',accno=accno,pinno=pinno)

@app.route('/deposite/<accno>/<pinno>',methods=['GET','POST'])
def deposite(accno,pinno):
    if request.method=='POST':
        amount=int(request.form['depo'])
        print(amount)
        accounts_lists=[{'account_id':accno,'balance':details['balance']} for accno,details in accounts.items()]
        if accounts_lists[0]['account_id']==accno:
            accounts_lists[0]['balance']+=amount
        print(accounts_lists)
        
        accounts[accno]['balance']=accounts_lists[0]['balance']
    return render_template('depo.html')

@app.route('/withdraw/<accno>/<pinno>',methods=['GET','POST'])
def withdraw(accno,pinno):
    if request.method=='POST':
        amount=int(request.form['withd'])
        print(amount)
        accounts_lists=[{'account_id':accno,'balance':details['balance']} for accno,details in accounts.items()]
        if accounts_lists[0]['account_id']==accno:
            oramount=accounts_lists[0]['balance']
        if amount>oramount:
            return 'given amount is out of balance'
        else:
            accounts_lists[0]['balance']-=amount
            
        print(accounts_lists)
        accounts[accno]['balance']=accounts_lists[0]['balance']
        
    return render_template('withdw.html')

#@app.route('/balance/<accno>/<pinno>')

#def balance(accno,pinno):
    


            
    

app.run(debug=True,use_reloader=True)
        