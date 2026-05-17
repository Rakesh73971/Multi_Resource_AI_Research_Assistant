from sqlalchemy.orm import Session
from app.models.user import User
from app.core.utils import hash_password

def create_user_service(db:Session,user):
    user = User(
        full_name = user.full_name,
        email=user.email,
        password = hash_password(user.password),
        role = user.role,
        is_active = user.is_active if user.is_active is not None else True
    )
    db.add(user)
    db.commit(user)
    db.refresh(User)
    return user

def get_users_service(db:Session):
    users = db.query(User).all()
    return users

def get_user_service(db:Session,id):
    user = db.query(User).filter(User.id ==id ).first()
    return user


def delete_user_service(db:Session,id):
    user = db.query(User).filter(User.id == id).first()
    db.delete(user)
    db.commit()
    return None