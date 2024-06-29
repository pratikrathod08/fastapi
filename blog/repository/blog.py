from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models, database


get_db = database.get_db

def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request:schemas.Blog, db:Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1 )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(id:int , db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(id:int, request, db:Session,):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found")
    blog.update(dict(request))
    db.commit()
    return 'updated successfully'


def show(id:int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=400, detail=f"Blog with id {id} not availbale")
    return blog