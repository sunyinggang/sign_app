from app import db


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teacher_num = db.Column(db.String(255))
    tec_account_num = db.Column(db.String(255))
    password = db.Column(db.String(255))
    teacher_name = db.Column(db.String(255))
    level = db.Column(db.String(255))
    status = db.Column(db.Integer)
    face_picture = db.Column(db.String(255))
    id_number = db.Column(db.String(255))
    gender = db.Column(db.Integer)
    school = db.Column(db.String(255))
    department = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    teacher_qualification = db.Column(db.String(255))
    teacher_qualification_picture = db.Column(db.String(255))

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
            return dict

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(255))
    classroom = db.Column(db.String(255))
    teacher_id = db.Column(db.Integer)
    ctime = db.Column(db.Integer)
    start_time = db.Column(db.String(255))
    end_time = db.Column(db.String(255))
    max_late_time = db.Column(db.Integer)

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
            return dict

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_num = db.Column(db.String(255))
    stu_account_num = db.Column(db.String(255))
    password = db.Column(db.String(255))
    student_name = db.Column(db.String(255))
    status = db.Column(db.Integer)
    face_picture = db.Column(db.String(255))
    birth_place = db.Column(db.String(255))
    id_number = db.Column(db.String(255))
    gender = db.Column(db.Integer)
    birthday = db.Column(db.Date)
    school = db.Column(db.String(255))
    department = db.Column(db.String(255))
    class_name = db.Column(db.String(255))
    phone = db.Column(db.String(255))

class StuCourse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer)
    student_id = db.Column(db.Integer)
    teacher_id = db.Column(db.Integer)
