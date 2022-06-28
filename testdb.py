from pybo.models import Question, Answer
from datetime import datetime
from pybo import db

def test():
    q = Question(subject='pybo가 무엇인가요?', content='pybo에 대해서 알고 싶습니다.', create_date=datetime.now())
    db.session.add(q)
    db.session.commit()