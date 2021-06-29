from flask import Flask,request,jsonify

app=Flask(__name__)

dictionary={}

@app.route('/<id>',methods=['GET'])
def get_counter(id):
    res=dictionary.get(id,None)
    if res==None:
        return {"Message":"Not present in System"}
    print(dictionary)
    return {"Counter":res}

@app.route('/add/<id>',methods=["POST"])
def add_Counter(id):
    dictionary[id]=0
    print(dictionary)
    return {"Message":"Data added to dictionary"}

@app.route('/<id>/increment',methods=["POST"])
def increment_Counter(id):
    res=dictionary.get(id,None)
    if res==None:
        print(dictionary)
        return {"Message":"Not present in System"}
    dictionary[id]=res+1
    print(dictionary)
    return {"Message":"Increment successfully !"}

@app.route('/<id>/decrement',methods=['POST'])
def decrement_count(id):
    res=dictionary.get(id,None)
    if res==None:
        return {"Message":"Not present in System"}
    dictionary[id]=res-1
    print(dictionary)
    return {"Message":"decrement successfully !"}

@app.route('/<id>/delete',methods=['DELETE'])
def del_Counter(id):
    res=dictionary.get(id,None)
    if res==None:
        return {"Message":"Not present in System"}
    del dictionary[id]
    print(dictionary)
    return {"Message":"counter deleted successfully !"}

if __name__=="__main__":
    app.run(debug=True)
