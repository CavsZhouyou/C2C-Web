"""empty message

Revision ID: 2389556b3de5
Revises: 16db8838c513
Create Date: 2018-07-11 20:18:01.968383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2389556b3de5'
down_revision = '16db8838c513'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('to_which', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comment', 'accommodation', ['to_which'], ['acc_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.drop_column('comment', 'to_which')
    # ### end Alembic commands ###
