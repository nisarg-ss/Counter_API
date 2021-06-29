from flask import Flask,request,jsonify

app=Flask(__name__)

dictionary={}

@app.route('/<id>',methods=['GET'])
def get_counter(id):
    try:
        res=dictionary.get(id,None)
        if res==None:
            return {"Message":"Not present in System"}
        print(dictionary)
        return {"Counter":res}
    except Exception as e:
        return {'error':str(e)}

@app.route('/add/<id>',methods=["POST"])
def add_Counter(id):
    try:
        dictionary[id]=0
        print(dictionary)
        return {"Message":"Data added to dictionary"}
    except Exception as e:
        return {'error':str(e)}

@app.route('/<id>/increment',methods=["POST"])
def increment_Counter(id):
    try:
        res=dictionary.get(id,None)
        if res==None:
            print(dictionary)
            return {"Message":"Not present in System"}
        dictionary[id]=res+1
        print(dictionary)
        return {"Message":"Increment successfully !"}
    except Exception as e:
        return {'error':str(e)}

@app.route('/<id>/decrement',methods=['POST'])
def decrement_count(id):
    try:
        res=dictionary.get(id,None)
        if res==None:
            return {"Message":"Not present in System"}
        dictionary[id]=res-1
        print(dictionary)
        return {"Message":"decrement successfully !"}
    except Exception as e:
        return {'error':str(e)}

@app.route('/<id>/delete',methods=['DELETE'])
def del_Counter(id):
    try:
        res=dictionary.get(id,None)
        if res==None:
            return {"Message":"Not present in System"}
        del dictionary[id]
        print(dictionary)
        return {"Message":"counter deleted successfully !"}
    except Exception as e:
        return {'error':str(e)}

if __name__=="__main__":
    app.run(debug=True)
