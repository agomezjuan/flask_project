"""empty message

Revision ID: 2089cc537da5
Revises: 
Create Date: 2023-02-07 20:37:35.606557

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2089cc537da5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.drop_table('some_table')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('some_table',
    sa.Column('x', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('y', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.drop_table('users')
    # ### end Alembic commands ###
