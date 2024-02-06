from flask import request, jsonify
from app import app, db
from models import Background, BasicData, Hand, AccuracyData, PlayerData, ProgramData#, TwoPlayer, TwoPlayerFinal
import logging



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
    data = request.get_json()
    if not data or 'dynamic_column' not in data:
        return jsonify({"error": "Missing required data"}), 400

    dynamic_column = data.get("dynamic_column")

    # 해당 컬럼이 BasicData 모델에 존재하는지 확인
    if not hasattr(BasicData, dynamic_column):
        return jsonify({"error": "Invalid dynamic_column"}), 400
    
    logging.debug(f"Received PUT request data: {data}")  # 요청 받은 데이터 로그
    basic_data = BasicData.query.filter_by(znickname=nickname).order_by(BasicData.row_number.desc()).first_or_404()

    logging.debug(f"Received request to update {dynamic_column} rating for {nickname}")

    if dynamic_column:
        dynamic_value = getattr(basic_data, dynamic_column, None)
        logging.debug(f"Dynamic Value for {dynamic_column}: {dynamic_value}")

        all_values = [getattr(record, dynamic_column) for record in BasicData.query.filter(getattr(BasicData, dynamic_column) > 0).all()]
        logging.debug(f"All Values for {dynamic_column}: {all_values}")

        if dynamic_value == 0 or dynamic_value == 0.0:
            basic_data.basic_rating = 0
        else:
            all_values_sorted = sorted(all_values, reverse=True)
            rank = all_values_sorted.index(dynamic_value) + 1
            percentile_rank = (len(all_values) - rank + 1) / len(all_values) * 100
            logging.debug(f"Percentile Rank for {dynamic_column}: {percentile_rank}")

            basic_data.basic_rating = round(percentile_rank)
            db.session.commit()
            logging.debug(f"Updated basic_rating to {basic_data.basic_rating} for {nickname}")

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
