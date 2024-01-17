from flask import request, jsonify
from app import app, db
from models import Background, BasicData, Hand, AccuracyData, PlayerData, ProgramData, TwoPlayer, TwoPlayerFinal

# BackgroundData Routes
@app.route('/api/BackgroundData', methods=['GET'])
def get_background_data():
    latest_data = Background.query.order_by(Background.user_id.desc()).first()
    if latest_data:
        return jsonify(latest_data.to_dict()), 200
    else:
        return jsonify({"message": "No data available"}), 404

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
    latest_data = BasicData.query.order_by(BasicData.play_id.desc()).first()
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

# HandData Routes
@app.route('/api/HandData', methods=['GET'])
def get_hand_data():
    latest_data = Hand.query.order_by(Hand.hand_id.desc()).first()
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

@app.route('/api/HandData/<int:hand_id>', methods=['PUT'])
def update_hand_data(hand_id):
    data = request.json
    hand_data = Hand.query.get_or_404(hand_id)
    hand_data.rx = data.get('rx', hand_data.rx)
    hand_data.ry = data.get('ry', hand_data.ry)
    hand_data.lx = data.get('lx', hand_data.lx)
    hand_data.ly = data.get('ly', hand_data.ly)
    db.session.commit()
    return jsonify(hand_data.to_dict()), 200

# AccuracyData Routes
@app.route('/api/AccuracyData', methods=['GET'])
def get_accuracy_data():
    latest_data = AccuracyData.query.order_by(AccuracyData.play_id.desc()).first()
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
    latest_data = PlayerData.query.order_by(PlayerData.play_id.desc()).first()
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
    latest_data = ProgramData.query.order_by(ProgramData.program_id.desc()).first()
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
@app.route('/api/TwoPlayerData', methods=['GET'])
def get_two_player_data():
    latest_data = TwoPlayer.query.order_by(TwoPlayer.play_id.desc()).first()
    if latest_data:
        return jsonify(latest_data.to_dict()), 200
    else:
        return jsonify({"message": "No data available"}), 404


@app.route('/api/TwoPlayerData', methods=['POST'])
def add_two_player_data():
    data = request.json
    new_data = TwoPlayer(**data)
    db.session.add(new_data)
    db.session.commit()
    return jsonify(new_data.to_dict()), 201

# TwoPlayerFinalData Routes
@app.route('/api/TwoPlayerFinalData', methods=['GET'])
def get_two_player_final_data():
    latest_data = TwoPlayerFinal.query.order_by(TwoPlayerFinal.play_id.desc()).first()
    if latest_data:
        return jsonify(latest_data.to_dict()), 200
    else:
        return jsonify({"message": "No data available"}), 404


@app.route('/api/TwoPlayerFinalData', methods=['POST'])
def add_two_player_final_data():
    data = request.json
    new_data = TwoPlayerFinal(**data)
    db.session.add(new_data)
    db.session.commit()
    return jsonify(new_data.to_dict()), 201
