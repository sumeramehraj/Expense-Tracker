from peewee import *

db = SqliteDatabase('fintrack.db')

class User(Model):
    username = CharField()
    password = CharField()

    class Meta:
        database = db

class Wallet(Model):
    name = CharField()
    amount = IntegerField()
    owner = ForeignKeyField(User)

    class Meta:
        database = db

class Transaction(Model):
    amount = IntegerField()
    timestamp = DateTimeField()
    wallet = ForeignKeyField(Wallet, backref="transactions")
    note = TextField()
    is_debit = BooleanField()

    class Meta:
        database = db


if __name__ == "__main__":
    db.connect()
    db.create_tables([User, Wallet, Transaction])
