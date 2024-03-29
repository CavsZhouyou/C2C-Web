"""empty message

Revision ID: a6df1ebf0352
Revises: f7c27cba7c8b
Create Date: 2018-07-09 11:23:23.625378

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a6df1ebf0352'
down_revision = 'f7c27cba7c8b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'address',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'address',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100),
               nullable=False)
    # ### end Alembic commands ###
