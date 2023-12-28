"""Add Posts Model

Revision ID: 2d5929bad9c0
Revises: aef2fc794a99
Create Date: 2023-11-25 22:30:52.842398

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d5929bad9c0'
down_revision = 'aef2fc794a99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('auther', sa.String(length=255), nullable=True),
    sa.Column('date_posted', sa.DateTime(), nullable=True),
    sa.Column('slug', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    # ### end Alembic commands ###