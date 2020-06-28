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
@app.route('/reviews', methods=['POST'])
def write_winereview():
    사진 = request.form['vivino_사진']
    이름 = request.form['input_이름']
    생산국 = request.form['vivino_생산국']
    점수 = request.form['vivino_점수']
    스타일 = request.form['vivino_스타일']
    품종 = request.form['vivino_품종']
    맛 = request.form['vivino_맛']
    느낌 = request.form['input_느깜']
    평점 = request.form['input_평점']
    가격 = request.form['input_가격']
    날짜 = request.form['input_날짜']

    wine = {
       '사진': 사진,
       '이름': 이름,
       '생산국': 생산국,
       '점수': 점수,
       '스타일': 스타일,
       '품종' : 품종,
       '맛' : 맛,
       '느낌' : 느낌,
       '평점' : 평점,
       '가격' : 가격,
       '날짜' : 날짜
    }
    # reviews에 review 저장하기
    db.wines.insert_one(wine)
    # 성공 여부 & 성공 메시지 반환
    return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 작성되었습니다.'})


@app.route('/reviews', methods=['GET'])
def wine_reviews():
    wines = list(db.wines.find({},{'_id':0}))
    return jsonify({'result': 'success', 'wines': wines})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)