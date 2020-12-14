import datetime
import json
import time

from flask import request, jsonify

from app import app
from . import client
from .. import db
from ..lib.tencent_api import search_face
from ..models import Teacher, Course, StuCourse, Student


@client.after_request
def cors(environ):
    environ.headers['Access-Control-Allow-Origin']='*'
    environ.headers['Access-Control-Allow-Method']='*'
    environ.headers['Access-Control-Allow-Headers']='x-requested-with,content-type'
    return environ

@client.route("/teacher/class/list/", methods=['POST'])
def teacher_class_list():
    info = {}
    image = request.get_json()
    print(image)
    info["group_id"] = ["2"]
    info["image"] = image["image_info"]
    res = search_face(info)
    res_json = json.loads(res)
    person_info = res_json["Results"][0]["Candidates"]
    have = 0
    out = {}
    for person in person_info:
        if person["Score"] > 80:
            have = 1
            out["code"] = 200
            id = int(person["PersonId"][1:])
            list = []
            teacher = Teacher.query.filter_by(id=id).first()
            out["teacher_name"] = teacher.teacher_name
            out["teacher_num"] = teacher.teacher_num
            course_list = Course.query.filter_by(teacher_id=id).all()
            for course in course_list:
                list.append(course.to_json())
            out["course_list"] = list
            print(out)
            break
    if have == 0:
        out["code"] = 301
    return jsonify(out)

@client.route("/course/check/", methods=['POST'])
def course_check():
    info = {}
    request_data = request.get_json()
    course_id = request_data["course_id"]
    info["group_id"] = ["3"]
    info["image"] = request_data["image_info"]
    res = search_face(info)
    res_json = json.loads(res)
    person_info = res_json["Results"][0]["Candidates"]
    have = 0
    out = {}
    for person in person_info:
        if person["Score"] > 80:
            have = 1
            id = person["PersonId"][1:]
            student_list = StuCourse.query.filter_by(course_id=course_id).first()
            student_id_list = student_list.student_id
            student_id_list = student_id_list.split(",")
            if id in student_id_list:
                out["code"] = 200
                student = Student.query.filter_by(id=int(id)).first()
                out["student_name"] = student.student_name
                out["student_num"] = student.student_num
                course = Course.query.filter_by(id=course_id).first()
                late = check_time(course.start_time,course.max_late_time)
                if late == 1:
                    out["code"] = 201
            else:
                out["code"] = 302
            break
    if have == 0:
        out["code"] = 301
    print(out)
    return jsonify(out)

def check_time(start_time,max_late_time):
    # 获取当天日期
    date_p = datetime.datetime.now().date()
    str_p = str(date_p)
    # 日期加上上课时间
    s_time = str_p + " " + start_time
    # 字符串转时间
    dateTime_p = datetime.datetime.strptime(s_time, '%Y-%m-%d %H:%M')
    # 加上最大迟到时间
    new = dateTime_p + datetime.timedelta(minutes=max_late_time)
    # 时间转字符串
    new_str = new.strftime("%Y-%m-%d %H:%M:%S")
    # 获取最大迟到时间时间戳
    ts = time.mktime(time.strptime(new_str, "%Y-%m-%d %H:%M:%S"))
    # 获取当前时间时间戳
    n_ts = time.time()
    # 迟到判断
    if ts < n_ts:
        return 1
    else:
        return 0
