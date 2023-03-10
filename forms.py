from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[Email("Емэил введен некоректно!")])
    psw = PasswordField("Пароль", validators=[DataRequired(), Length(min=5, max=100, message="Длинa пароля от 6 до 100 символов")])
    remember = BooleanField("Не запоминать", default=True)
    submit = SubmitField("Войти")

class RegisterForm(FlaskForm):
    name = StringField("Имя: ", validators=[Length(min=4, max=100, message='Имя должно быть диной от 4 до 100 символов')])
    email = StringField("Email", validators=[Email("Емэил введен некоректно!")])
    psw = PasswordField("Пароль", validators=[DataRequired(), Length(min=5, max=100, message="Длинa пароля о 5 до 100 символов")])
    psw2 = PasswordField("Повторите пароль", validators=[DataRequired(), EqualTo('psw',message='Пароли не совпадают')])
    submit = SubmitField("Зарегистрироваться")














