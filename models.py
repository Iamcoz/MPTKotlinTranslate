from app import db

class Background(db.Model):
    row_number = db.Column(db.Integer, primary_key=True)
    znickname = db.Column(db.String(255))
    # zcreated_at = db.Column(db.TIMESTAMP)
    is_vr = db.Column(db.Integer, default=False)
    bg_name = db.Column(db.String(255))
    coord_name = db.Column(db.String(255))

    def to_dict(self):
        return {
            'row_number': self.row_number,
            'znickname': self.znickname,
            # 'zcreated_at': self.zcreated_at,
            'is_vr': self.is_vr,
            'bg_name': self.bg_name,
            'coord_name': self.coord_name
        }

class BasicData(db.Model):
    row_number = db.Column(db.Integer, primary_key=True)
    znickname = db.Column(db.String(255))
    # zcreated_at = db.Column(db.TIMESTAMP)
    reaction_time = db.Column(db.Float)
    on_air = db.Column(db.Float)
    squat_jump = db.Column(db.Integer)
    knee_punch = db.Column(db.Integer)
    balance_test = db.Column(db.Integer)
    basic_rating = db.Column(db.Integer)

    def to_dict(self):
        return {
            'row_number': self.row_number,
            'znickname': self.znickname,
            # 'zcreated_at': self.zcreated_at,
            'reaction_time': self.reaction_time,
            'on_air': self.on_air,
            'squat_jump': self.squat_jump,
            'knee_punch': self.knee_punch,
            'balance_test': self.balance_test,
            'basic_rating': self.basic_rating
        }

class Hand(db.Model):
    row_number = db.Column(db.Integer, primary_key=True)
    znickname = db.Column(db.String(255))
    # zcreated_at = db.Column(db.TIMESTAMP)
    rx = db.Column(db.Integer)
    ry = db.Column(db.Integer)
    lx = db.Column(db.Integer)
    ly = db.Column(db.Integer)

    def to_dict(self):
        return {
            'row_number': self.row_number,
            'znickname': self.znickname,
            # 'zcreated_at': self.zcreated_at,
            'rx': self.rx,
            'ry': self.ry,
            'lx': self.lx,
            'ly': self.ly
        }

class AccuracyData(db.Model):
    row_number = db.Column(db.Integer, primary_key=True)
    znickname = db.Column(db.String(255))
    # zcreated_at = db.Column(db.TIMESTAMP)
    capture_time = db.Column(db.Integer)
    accuracy = db.Column(db.Integer)

    def to_dict(self):
        return {
            'row_number': self.row_number,
            'znickname': self.znickname,
            # 'zcreated_at': self.zcreated_at,
            'capture_time': self.capture_time,
            'accuracy': self.accuracy
        }

class PlayerData(db.Model):
    row_number = db.Column(db.Integer, primary_key=True)
    znickname = db.Column(db.String(255))
    # zcreated_at = db.Column(db.TIMESTAMP)
    total = db.Column(db.Integer)
    total_top = db.Column(db.Integer)
    total_bottom = db.Column(db.Integer)
    perfect_frame = db.Column(db.Integer)
    awesome_frame = db.Column(db.Integer)
    good_frame = db.Column(db.Integer)
    ok_frame = db.Column(db.Integer)
    bad_frame = db.Column(db.Integer)
    recommend_content = db.Column(db.Integer)

    def to_dict(self):
        return {
            'row_number': self.row_number,
            'znickname': self.znickname,
            # 'zcreated_at': self.zcreated_at,
            'total': self.total,
            'total_top': self.total_top,
            'total_bottom': self.total_bottom,
            'perfect_frame': self.perfect_frame,
            'awesome_frame': self.awesome_frame,
            'good_frame': self.good_frame,
            'ok_frame': self.ok_frame,
            'bad_frame': self.bad_frame,
            'recommend_content': self.recommend_content
        }

class ProgramData(db.Model):
    row_number = db.Column(db.Integer, primary_key=True)
    znickname = db.Column(db.String(255))
    # zcreated_at = db.Column(db.TIMESTAMP)
    is_running = db.Column(db.Integer)

    def to_dict(self):
        return {
            'row_number': self.row_number,
            'znickname': self.znickname,
            # 'zcreated_at': self.zcreated_at,
            'is_running': self.is_running
        }

class TwoPlayer(db.Model):
    row_number = db.Column(db.Integer, primary_key=True)
    znickname = db.Column(db.String(255))
    # zcreated_at = db.Column(db.TIMESTAMP)
    capture_time = db.Column(db.Integer)
    first_player = db.Column(db.Integer)
    second_player = db.Column(db.Integer)

    def to_dict(self):
        return {
            'row_number': self.row_number,
            'znickname': self.znickname,
            # 'zcreated_at': self.zcreated_at,
            'capture_time': self.capture_time,
            'first_player': self.first_player,
            'second_player': self.second_player
        }

class TwoPlayerFinal(db.Model):
    row_number = db.Column(db.Integer, primary_key=True)
    znickname = db.Column(db.String(255))
    # zcreated_at = db.Column(db.TIMESTAMP)
    total_first = db.Column(db.Integer)
    perfect_frame_first = db.Column(db.Integer)
    awesome_frame_first = db.Column(db.Integer)
    good_frame_first = db.Column(db.Integer)
    ok_frame_first = db.Column(db.Integer)
    bad_frame_first = db.Column(db.Integer)
    total_second = db.Column(db.Integer)
    perfect_frame_second = db.Column(db.Integer)
    awesome_frame_second = db.Column(db.Integer)
    good_frame_second = db.Column(db.Integer)
    ok_frame_second = db.Column(db.Integer)
    bad_frame_second = db.Column(db.Integer)

    def to_dict(self):
        return {
            'row_number': self.row_number,
            'znickname': self.znickname,
            # 'zcreated_at': self.zcreated_at,
            'total_first': self.total_first,
            'perfect_frame_first': self.perfect_frame_first,
            'awesome_frame_first': self.awesome_frame_first,
            'good_frame_first': self.good_frame_first,
            'ok_frame_first': self.ok_frame_first,
            'bad_frame_first': self.bad_frame_first,
            'total_second': self.total_second,
            'perfect_frame_second': self.perfect_frame_second,
            'awesome_frame_second': self.awesome_frame_second,
            'good_frame_second': self.good_frame_second,
            'ok_frame_second': self.ok_frame_second,
            'bad_frame_second': self.bad_frame_second
        }
