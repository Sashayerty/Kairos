import sqlalchemy

from app.models.db_session import SqlAlchemyBase


class CourseModel(SqlAlchemyBase):
    """Модель курса, в ней хранится курс."""

    __tablename__ = "courses"

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
    )
    theme = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=False,
    )
    desires_of_user = sqlalchemy.Column(
        sqlalchemy.Text,
        nullable=True,
    )
    user_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable=False,
    )
    course = sqlalchemy.Column(
        sqlalchemy.JSON,
        nullable=False,
    )
