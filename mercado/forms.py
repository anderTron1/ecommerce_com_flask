from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from mercado.models import User

#, DataRequired() faz com que seja obrigatorio preencher os valores
class CadastroForm(FlaskForm):  
    usuario = StringField(label="Username:", validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label="Email:", validators=[Email(), DataRequired()])
    senha1 = PasswordField(label="Senha:", validators=[Length(min=6), DataRequired()])
    senha2 = PasswordField(label="Confirmação de Senha:", validators=[EqualTo('senha1'), DataRequired()])
    submit = SubmitField(label='Cadastrar')
    
    def validate_usuario(FlaskForm, check_user):
        user = User.query.filter_by(usuario=check_user.data).first()
        if user:
            raise ValidationError("Usuário já existe! Cadastre outro nome de usuário")
        return True
            
    def validate_email(FlaskForm, check_email):
        email1 = User.query.filter_by(email=check_email.data).first()
        if email1:
            raise ValidationError("Email já existe! Cadastre outro endereço de Email")
        return True
            
    def validade_senha(FlaskForm, check_senha):
        senha = User.query.filter_by(senha=check_senha.data).first()
        if senha:
            raise ValidationError("Senha já existe! cadastre outra senha")
        return True