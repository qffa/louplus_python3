from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, TextAreaField, IntegerField
from wtforms.validators import Length, Email, EqualTo, Required, URL, NumberRange
from simpledu.models import db, User, Course
import re
from flask import flash




class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[Required(), Length(3,24)])
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6,24)])
    repeat_password = PasswordField('重复密码', validators=[Required(), EqualTo('password')])
    submit = SubmitField('提交')


    def create_user(self):
        user = User()
        user.username = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        db.session.add(user)
        db.session.commit()


    def update_user(self, user):
        self.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        return user


    def validate_username(self, field):
        if not re.match('^\w*$', field.data):
            flash('用户名只能包含字母和数字！', 'danger')

        if User.query.filter_by(username = field.data).first():
            raise ValidationError('用户名已存在')


    def validate_email(self, field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError('邮箱已存在')





class LoginForm(FlaskForm):
#    email = StringField('邮箱', validators=[Required(), Email()])
    username = StringField('Username', validators=[Required(), Length(3, 24)])
    password = PasswordField('密码', validators=[Required(), Length(6,24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')



    def validate_username(self, field):
        if field.data and not User.query.filter_by(username = field.data).first():
            raise ValidationError('用户未注册')


    def validate_password(self, field):
        user = User.query.filter_by(username = self.username.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('密码错误')





class CourseForm(FlaskForm):
    name = StringField('课程名称', validators=[Required(), Length(5, 32)])
    description = TextAreaField('课程简介', validators=[Required(), Length(20, 256)])
    image_url = StringField('封面图片', validators=[Required(), URL()])
    author_id = IntegerField('作者ID', validators=[Required(), NumberRange(min=1, message='无效用户ID')])
    submit = SubmitField('提交')


    def validate_author_id(self, field):
        if not User.query.get(self.author_id.data):
            raise ValidationError('用户不存在')


    def create_course(self):
        course = Course()
        #使用课程表单数据填充course对象
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()

        return course


    def update_course(self, course):
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()

        return course






class UserForm(RegisterForm):
    role = IntegerField('role')
    submit = SubmitField('提交')


    def validate_rol(self, field):
        if field.data != 10 or field.data !=20 or field.data != 30:
            raise ValidationError('无效role')


    def validate_email(self, field):
#        if 
        if User.query.filter_by(email = field.data).first():
            raise ValidationError('邮箱已存在')












