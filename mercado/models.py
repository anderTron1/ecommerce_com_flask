from mercado import db

"""
para executar o codigo em modo debug
execute a linha de codigo no terminal:
    flask --app app run --debug

"""

"""
para criar as tabelas, utiliza o terminal, entrando com o comando python noterminal
importando as seguintes classes
from mercado import db
from mercado import app

e executa os seguintes comandos
app.app_context().push()
db.create_all()

dessa forma uma pasta chamada: instace
vai ser criada com o banco de dados sqlite dentro

---------------------------------------------------------------------
para adicionar elementos pelo terminal
importamos o Item
from mercado import Item

item1 = Item(nome="", preco=0, cod_barra="", descricao="")
db.session.add(item1)
db.session.commit()
"""
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=30), nullable=False, unique=True)
    preco = db.Column(db.Integer, nullable=False)
    cod_barra = db.Column(db.String(length=12), nullable=False, unique=True)
    descricao = db.Column(db.String(length=500), nullable=False, unique=True)
    dono = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return f"Item {self.nome}"
    
"""
para fazer um filtro e selecionar algum elemento 
User.query.filter_by(usuario='fulano').first().id
"""
class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    senha = db.Column(db.String(length=60), nullable=False, unique=True)
    valor = db.Column(db.Integer, nullable=False, default=5000)
    itens = db.relationship('Item', backref="dono_user", lazy=True)