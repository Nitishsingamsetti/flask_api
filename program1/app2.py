from flask import Flask,redirect

app2=Flask(__name__)

@app2.route('/charecter/<letter>')
def charecter(letter):
    if letter in ['a','e','i','o','u']:
        return redirect('http://127.0.0.1:5000/vowels')
    else:
        return redirect('http://127.0.0.1:5000/consonants')
@app2.route('/vowels')  
def vowels():
    return 'given charc is vowel'
@app2.route('/consonants')
def consonants():
    return 'given char is consonants'

app2.run(debug=True)