from flask import Flask
import redis

app=Flask(__name__)
redis_server=redis.Redis('localhost',decode_responses=True)


@app.route('/<id>',methods=['GET'])
def get_counter(id):
    res=(redis_server.hget('counters',id))
    if res==None:
        return {"Message":"Not present in System"}
    return {"Counter":int(res)}

@app.route('/add/<id>',methods=["POST"])
def add_Counter(id):
    res=(redis_server.hget('counters',id))
    if res!=None:
        return {"Message":"the data with this id is already there !"}
    redis_server.hset('counters',id,0)
    return {"Message":"Data added to dictionary"}

@app.route('/<id>/increment',methods=["POST"])
def increment_Counter(id):
    res=redis_server.hget('counters',id)
    if res==None:
        return {"Message":"Not present in System"}
    redis_server.hset('counters',id,int(res)+1)
    return {"Message":"Increment successfully !"}

@app.route('/<id>/decrement',methods=['POST'])
def decrement_count(id):
    res=int(redis_server.hget('counters',id))
    if res==None:
        return {"Message":"Not present in System"}
    redis_server.hset('counters',id,res-1)
    return {"Message":"decrement successfully !"}

@app.route('/<id>/delete',methods=['DELETE'])
def del_Counter(id):
    res=int(redis_server.hget('counters',id))
    if res==None:
        return {"Message":"Not present in System"}
    redis_server.hdel('counters',id)
    return {"Message":"counter deleted successfully !"}

if __name__=="__main__":
    app.run(debug=True)
