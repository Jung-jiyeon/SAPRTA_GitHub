from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/wines', methods=['POST'])
def write_winereview():
    이름 = request.form['이름']
    날짜 = request.form['날짜']
    가격 = request.form['가격']
    느낌 = request.form['느낌']
    평점 = request.form['평점']
    생산지 = request.form['생산지']
    종류 = request.form['종류']

    wine = {
       '이름': 이름,
       '날짜': 날짜,
       '가격': 가격,
       '느낌': 느낌,
       '평점': 평점,
       '생산지': 생산지,
       '종류': 종류,
    }
    db.wines.insert_one(wine)
    # 성공 여부 & 성공 메시지 반환
    return jsonify({'result': 'success','msg': '리뷰가 성공적으로 작성되었습니다.'})


@app.route('/wines', methods=['GET'])
def wine_reviews():
    wines = list(db.wines.find({},{'_id':0}))
    return jsonify({'result': 'success', 'wines': wines})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
