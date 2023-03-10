from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[Email("Емэил введен некоректно!")])
    psw = PasswordField("Пароль", validators=[DataRequired(), Length(min=5, max=100, message="Длинa пароля от 6 до 100 символов")])
    remember = BooleanField("Не запоминать", default=True)
    submit = SubmitField("Войти")
















