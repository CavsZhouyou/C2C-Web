"""empty message

Revision ID: 194dc955c10c
Revises: 2389556b3de5
Create Date: 2018-07-11 20:47:05.851953

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '194dc955c10c'
down_revision = '2389556b3de5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('comment_ibfk_4', 'comment', type_='foreignkey')
    op.drop_column('comment', 'to_which')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('to_which', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('comment_ibfk_4', 'comment', 'accommodation', ['to_which'], ['acc_id'])
    # ### end Alembic commands ###
