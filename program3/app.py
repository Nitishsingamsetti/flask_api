from flask import Flask,request,jsonify
app=Flask(__name__)

@app.route('/data',methods=['POST'])
def get_data():
    data=request.get_json()
    response={'received':data}
    return jsonify(response) #jsonify()--converts given data to json format
app.run(debug=True)
    