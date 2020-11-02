from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/order', methods=['POST'])
def post_article():
    name = request.form['name']
    cnt = request.form['cnt']
    ad = request.form['ad']
    ph = request.form['ph']
    doc = {
        'Name': name,
        'Count': cnt,
        'Address': ad,
        'Phone Number': ph
    }
    db.order.insert_one(doc);
    return jsonify({'result': 'success', 'msg': '주문이 완료되었습니다!'})


@app.route('/order', methods=['GET'])
def read_articles():
    orderlist = list(db.order.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'msg': 'GET 연결되었습니다!', 'orders': orderlist})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
