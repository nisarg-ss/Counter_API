from flask import Flask,jsonify,request
from pymongo import MongoClient
import datetime

app = Flask(__name__)

URI='mongodb+srv://admin:1234567890@cluster0.jnepj.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(URI)

db=client.jsn
Counter=db.counter

@app.route('/<id>',methods=['GET'])
def get_counter(id):
    try:
        res=Counter.find_one({"id":id})
        if res==None:
            return {"message":"Not present in System"}
        return {"Counter":res['count'],'last updated':res['timestamp']}
    except Exception as e:
        return jsonify({'error':str(e)})

@app.route('/add/<id>',methods=["POST"])
def add_Counter(id):
    try:
        res=Counter.find_one({"id":id}) 
        if res!=None:
            return {"message":"given id already present in System"}
        data={'id':id,'count':0,'timestamp':datetime.datetime.now()}
        Counter.insert_one(data)
        return {"message":"Data added to dictionary"}
    except Exception as e:
        return {'error':str(e)}

@app.route('/<id>/increment',methods=["POST"])
def increment_Counter(id):
    try:
        res=Counter.find_one({"id":id}) 
        if res==None:
            return {"message":"Not present in System"}
        res=Counter.update({'id':id},{'$set':{'count':res['count']+1,'timestamp':datetime.datetime.now()}})
        return {"message":"Increment successfully !"}
    except Exception as e:
        return {'error':str(e)}

@app.route('/<id>/decrement',methods=['POST'])
def decrement_count(id):
    try:
        res=Counter.find_one({"id":id}) 
        if res==None:
            return {"message":"Not present in System"}
        res=Counter.update({'id':id},{'$set':{'count':res['count']-1,'timestamp':datetime.datetime.now()}})
        return {"message":"decrement successfully !"}
    except Exception as e:
        return {'error':str(e)}

@app.route('/<id>/delete',methods=['DELETE'])
def del_Counter(id):
    try:
        res=Counter.find_one({"id":id}) 
        if res==None:
            return {"message":"Not present in System"}
        res=Counter.delete_one({'id':id})
        return {"message":"counter deleted successfully !"}
    except Exception as e:
        return {'error':str(e)}
    
if __name__ == '__main__':
    app.run(debug=True)