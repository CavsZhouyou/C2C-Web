"""empty message

Revision ID: e55dbcbddfd0
Revises: df6bdb273287
Create Date: 2018-07-11 22:30:17.299346

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e55dbcbddfd0'
down_revision = 'df6bdb273287'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reservation', sa.Column('begin', sa.BigInteger(), nullable=False))
    op.add_column('reservation', sa.Column('end', sa.BigInteger(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reservation', 'end')
    op.drop_column('reservation', 'begin')
    # ### end Alembic commands ###