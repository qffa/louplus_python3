import os
import json
from random import randint
from faker import Faker
from simpledu.models import db, User, Course, Chapter






fake = Faker()


def iter_users():
    yield User(
            username = 'JackLee',
            email = 'jacklee@simpledu.com',
            password = '1234567890',
            job = '研发工程师'
            )




def iter_courses():
    author = User.query.filter_by(username='JackLee').first()

    with open(os.path.join(os.path.dirname(__file__), '..', 'datas', 'courses.json')) as f:
        courses = json.load(f)


    for course in courses:
        yield Course(
                name = course['name'],
                description = course['description'],
                image_url=course['image_url'],
                author = author
                )





def iter_chapters():
    for course in Course.query:
        #每个课程生成3～10个章节
        for i in range(randint(3,10)):
            yield Chapter(
                #使用fake生成一个句子作为章节名称
                name = fake.sentence(),
                course = course,
                vedio_url = 'https://labfile.oss.aliyuncs.com/courses/923/week2_mp4/2-1-1-mac.mp4',
                vedio_duration = '{}:{}'.format(randint(10,30), randint(10, 59))
                )





def run():
    for user in iter_users():
        db.session.add(user)


    for course in iter_courses():
        db.session.add(course)



    for chapter in iter_chapters():
        db.session.add(chapter)



    try:
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rooback()








