"""create model

Revision ID: b4fbc3edc05d
Revises: 
Create Date: 2018-06-25 19:36:16.721045

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4fbc3edc05d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'uploaded_data',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('url', sa.String()),
        sa.Column('description', sa.String()),
        sa.Column('creation_date', sa.DateTime()),
        sa.Column('is_uploaded', sa.Boolean(), default=True, nullable=False),
        sa.Column('is_video', sa.Boolean(), default=False),
        sa.Column('cover_photo', sa.String())
    )

def downgrade():
    op.drop_table('service_config')