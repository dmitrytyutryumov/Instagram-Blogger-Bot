from datetime import datetime
import sqlalchemy as sa

from . import BaseModel


class UploadedData(BaseModel):
    __tablename__ = 'uploaded_data'

    id = sa.Column('id', sa.Integer(), primary_key=True)
    url = sa.Column('url', sa.String())
    cover_photo = sa.Column('cover_photo', sa.String())
    description = sa.Column('description', sa.String())
    creation_date = sa.Column(
        'creation_date', sa.DateTime(), default=datetime.utcnow)
    is_uploaded = sa.Column('is_uploaded', sa.Boolean(), default=True)
    is_video = sa.Column('is_video', sa.Boolean(), default=False)