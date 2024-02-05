from flask import request, jsonify
from app import app, db
from models import Background, BasicData, Hand, AccuracyData, PlayerData, ProgramData#, TwoPlayer, TwoPlayerFinal


# BackgroundData Routes
@app.route('/api/BackgroundData', methods=['GET'])
def get_background_data():
    nickname = request.args.get('nickname')
    if nickname:
        latest_data = Background.query.filter_by(znickname=nickname).order_by(Background.row_number.desc()).first()
    else:
        return jsonify({"message": "No nickname provided"}), 400    # 닉네임 없을 경우

    if latest_data:
        return jsonify(latest_data.to_dict()), 200
    else:
        return jsonify({"message": "No data available"}), 404   # Data 없을 경우

@app.route('/api/BackgroundData', methods=['POST'])
def add_background_data():
    data = request.json
    new_data = Background(**data)
    db.session.add(new_data)
    db.session.commit()
    return jsonify(new_data.to_dict()), 201


# BasicData Routes
@app.route('/api/BasicData', methods=['GET'])
def get_basic_data():
    nickname = request.args.get('nickname')
    if nickname:
        latest_data = BasicData.query.filter_by(znickname=nickname).order_by(BasicData.row_number.desc()).first()
    else:
        return jsonify({"message": "No nickname provided"}), 400

    if latest_data:
        return jsonify(latest_data.to_dict()), 200
    else:
        return jsonify({"message": "No data available"}), 404

@app.route('/api/BasicData', methods=['POST'])
def add_basic_data():
    data = request.json
    new_data = BasicData(**data)
    db.session.add(new_data)
    db.session.commit()
    return jsonify(new_data.to_dict()), 201

# 기초체력 상위 퍼센테이지 산출 및 컬럼 update
@app.route('/api/BasicData/<string:nickname>/update_rating', methods=['PUT'])
def update_basic_rating(nickname):
    basic_data = BasicData.query.filter_by(znickname=nickname).order_by(BasicData.row_number.desc()).first_or_404()

    columns = ['reaction_time', 'on_air', 'squat_jump', 'knee_punch', 'balance_test']
    for column in columns:
        value = getattr(basic_data, column)
        if value is not None:
            if value == 0:
                # value가 0일 경우 상위 0%로 처리
                basic_data.basic_rating = 0
            else:
                # 모든 유효한 값(0이 아닌 값) 가져오기
                all_values = [getattr(record, column) for record in BasicData.query.filter(
                    getattr(BasicData, column) > 0).all()]

                if len(all_values) == 1:
                    # 유효한 값이 하나만 있는 경우 상위 1%로 처리
                    percentile_rank = 1
                else:
                    # 값이 주어진 값보다 작거나 같은 경우의 개수 계산
                    count_less_than_or_equal = sum(1 for val in all_values if val <= value)
                    # 퍼센트 순위 계산
                    percentile_rank = ((count_less_than_or_equal - 1) / len(all_values)) * 100

                basic_data.basic_rating = round(percentile_rank)
            break

    db.session.commit()
    return jsonify(basic_data.to_dict()), 200




# HandData Routes
@app.route('/api/HandData', methods=['GET'])
def get_hand_data():
    nickname = request.args.get('nickname')
    if nickname:
        latest_data = Hand.query.filter_by(znickname=nickname).order_by(Hand.row_number.desc()).first()
    else:
        return jsonify({"message": "No nickname provided"}), 400

    if latest_data:
        return jsonify(latest_data.to_dict()), 200
    else:
        return jsonify({"message": "No data available"}), 404

@app.route('/api/HandData', methods=['POST'])
def add_hand_data():
    data = request.json
    new_data = Hand(**data)
    db.session.add(new_data)
    db.session.commit()
    return jsonify(new_data.to_dict()), 201

@app.route('/api/HandData/<string:nickname>', methods=['PUT'])
def update_hand_data(nickname):
    data = request.json
    hand_data = Hand.query.filter_by(znickname=nickname).order_by(Hand.row_number.desc()).first_or_404()
    hand_data.rx = data.get('rx', hand_data.rx)
    hand_data.ry = data.get('ry', hand_data.ry)
    hand_data.lx = data.get('lx', hand_data.lx)
    hand_data.ly = data.get('ly', hand_data.ly)
    db.session.commit()
    return jsonify(hand_data.to_dict()), 200


# AccuracyData Routes
@app.route('/api/AccuracyData', methods=['GET'])
def get_accuracy_data():
    nickname = request.args.get('nickname')
    if nickname:
        latest_data = AccuracyData.query.filter_by(znickname=nickname).order_by(AccuracyData.row_number.desc()).first()
    else:
        return jsonify({"message": "No nickname provided"}), 400

    if latest_data:
        return jsonify(latest_data.to_dict()), 200
    else:
        return jsonify({"message": "No data available"}), 404

@app.route('/api/AccuracyData', methods=['POST'])
def add_accuracy_data():
    data = request.json
    new_data = AccuracyData(**data)
    db.session.add(new_data)
    db.session.commit()
    return jsonify(new_data.to_dict()), 201


# PlayerData Routes
@app.route('/api/PlayerData', methods=['GET'])
def get_player_data():
    nickname = request.args.get('nickname')
    if nickname:
        latest_data = PlayerData.query.filter_by(znickname=nickname).order_by(PlayerData.row_number.desc()).first()
    else:
        return jsonify({"message": "No nickname provided"}), 400

    if latest_data:
        return jsonify(latest_data.to_dict()), 200
    else:
        return jsonify({"message": "No data available"}), 404

@app.route('/api/PlayerData', methods=['POST'])
def add_player_data():
    data = request.json
    new_data = PlayerData(**data)
    db.session.add(new_data)
    db.session.commit()
    return jsonify(new_data.to_dict()), 201


# ProgramData Routes
@app.route('/api/ProgramData', methods=['GET'])
def get_program_data():
    nickname = request.args.get('nickname')
    if nickname:
        latest_data = ProgramData.query.filter_by(znickname=nickname).order_by(ProgramData.row_number.desc()).first()
    else:
        return jsonify({"message": "No nickname provided"}), 400

    if latest_data:
        return jsonify(latest_data.to_dict()), 200
    else:
        return jsonify({"message": "No data available"}), 404

@app.route('/api/ProgramData', methods=['POST'])
def add_program_data():
    data = request.json
    new_data = ProgramData(**data)
    db.session.add(new_data)
    db.session.commit()
    return jsonify(new_data.to_dict()), 201

@app.route('/api/ProgramData', methods=['DELETE'])
def delete_all_program_data():
    ProgramData.query.delete()
    db.session.commit()
    return '', 204


# TwoPlayerData Routes
# @app.route('/api/TwoPlayerData', methods=['GET'])
# def get_two_player_data():
#     nickname = request.args.get('nickname')
#     if nickname:
#         latest_data = TwoPlayer.query.filter_by(znickname=nickname).order_by(TwoPlayer.row_number.desc()).first()
#     else:
#         return jsonify({"message": "No nickname provided"}), 400

#     if latest_data:
#         return jsonify(latest_data.to_dict()), 200
#     else:
#         return jsonify({"message": "No data available"}), 404

# @app.route('/api/TwoPlayerData', methods=['POST'])
# def add_two_player_data():
#     data = request.json
#     new_data = TwoPlayer(**data)
#     db.session.add(new_data)
#     db.session.commit()
#     return jsonify(new_data.to_dict()), 201


# # TwoPlayerFinalData Routes
# @app.route('/api/TwoPlayerFinalData', methods=['GET'])
# def get_two_player_final_data():
#     nickname = request.args.get('nickname')
#     if nickname:
#         latest_data = TwoPlayerFinal.query.filter_by(znickname=nickname).order_by(TwoPlayerFinal.row_number.desc()).first()
#     else:
#         return jsonify({"message": "No nickname provided"}), 400

#     if latest_data:
#         return jsonify(latest_data.to_dict()), 200
#     else:
#         return jsonify({"message": "No data available"}), 404

# @app.route('/api/TwoPlayerFinalData', methods=['POST'])
# def add_two_player_final_data():
#     data = request.json
#     new_data = TwoPlayerFinal(**data)
#     db.session.add(new_data)
#     db.session.commit()
#     return jsonify(new_data.to_dict()), 201
