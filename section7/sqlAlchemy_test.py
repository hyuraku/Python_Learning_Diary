import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

# engine = sqlalchemy.create_engine('sqlite:///test_sqlite2')
engine = sqlalchemy.create_engine(
    'mysql+pymysql:///test_mysql_base2', echo=True)

Base = sqlalchemy.ext.declarative.declarative_base()

# テーブル作成


class Person(Base):
    __tablename__ = 'persons'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True
    )
    name = sqlalchemy.Column(
        sqlalchemy.String(14)
    )


Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

# person=Person(name='Mike')
# session.add(person)

# 行を追加


def add_person(Name):
    person = Person(name=Name)
    session.add(person)
    session.commit()

# 行の情報を書き換える


def change_name(before_name, after_name):
    target = session.query(Person).filter_by(name=before_name).first()
    target.name = after_name
    session.add(target)
    session.commit()

# 行を削除する


def delete_name(Name):
    target = session.query(Person).filter_by(name=Name).first()
    session.delete(target)
    session.commit()


add_person('Mike')
add_person('Tom')
add_person('Jack')

change_name('Mike', 'Zack')

delete_name('Jack')

# テーブル内の情報の一覧
persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name)
