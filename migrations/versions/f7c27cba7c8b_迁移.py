"""迁移

Revision ID: f7c27cba7c8b
Revises: 1e20f7f7a78b
Create Date: 2018-07-05 18:03:40.209749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7c27cba7c8b'
down_revision = '1e20f7f7a78b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accommodationtype',
    sa.Column('acctype_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('acctype_description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('acctype_id'),
    sa.UniqueConstraint('acctype_id')
    )
    op.create_table('city',
    sa.Column('city_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('city_name', sa.String(length=20), nullable=False),
    sa.Column('city_info', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('city_id'),
    sa.UniqueConstraint('city_id')
    )
    op.create_table('contractstate',
    sa.Column('constate_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('constate_name', sa.String(length=50), nullable=False),
    sa.Column('constate_description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('constate_id'),
    sa.UniqueConstraint('constate_id')
    )
    op.create_table('resstate',
    sa.Column('state_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('state_name', sa.String(length=50), nullable=False),
    sa.Column('state_info', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('state_id'),
    sa.UniqueConstraint('state_id')
    )
    op.create_table('role',
    sa.Column('role_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('role_name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('role_id'),
    sa.UniqueConstraint('role_id')
    )
    op.create_table('accommodation',
    sa.Column('acc_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('acc_address', sa.String(length=255), nullable=True),
    sa.Column('acc_capacity', sa.Integer(), nullable=True),
    sa.Column('acc_price', sa.String(length=100), nullable=True),
    sa.Column('acc_city', sa.Integer(), nullable=True),
    sa.Column('acc_description', sa.String(length=255), nullable=True),
    sa.Column('acc_user_id', sa.Integer(), nullable=True),
    sa.Column('acc_type_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['acc_city'], ['city.city_id'], ),
    sa.ForeignKeyConstraint(['acc_type_id'], ['accommodationtype.acctype_id'], ),
    sa.ForeignKeyConstraint(['acc_user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('acc_id'),
    sa.UniqueConstraint('acc_id')
    )
    op.create_table('disclaimer',
    sa.Column('disclaimer_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('publishdate', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('disclaimer_id'),
    sa.UniqueConstraint('disclaimer_id')
    )
    op.create_table('travelmessage',
    sa.Column('tmessage_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('addressoftravel', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('tmessage_id'),
    sa.UniqueConstraint('tmessage_id')
    )
    op.create_table('accommodationimage',
    sa.Column('accImage_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('accImage_acc_id', sa.Integer(), nullable=True),
    sa.Column('accImage_url', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['accImage_acc_id'], ['accommodation.acc_id'], ),
    sa.PrimaryKeyConstraint('accImage_id'),
    sa.UniqueConstraint('accImage_id')
    )
    op.create_table('reservation',
    sa.Column('res_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tenant_id', sa.Integer(), nullable=False),
    sa.Column('demand', sa.Text(), nullable=True),
    sa.Column('acc_id', sa.Integer(), nullable=True),
    sa.Column('state_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['acc_id'], ['accommodation.acc_id'], ),
    sa.ForeignKeyConstraint(['state_id'], ['resstate.state_id'], ),
    sa.PrimaryKeyConstraint('res_id'),
    sa.UniqueConstraint('res_id')
    )
    op.create_table('comment',
    sa.Column('comment_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('from_who', sa.Integer(), nullable=True),
    sa.Column('to_which', sa.Integer(), nullable=True),
    sa.Column('to_who', sa.Integer(), nullable=True),
    sa.Column('content', sa.String(length=15), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['from_who'], ['user.user_id'], ),
    sa.ForeignKeyConstraint(['to_which'], ['reservation.res_id'], ),
    sa.ForeignKeyConstraint(['to_who'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('comment_id'),
    sa.UniqueConstraint('comment_id')
    )
    op.create_table('contract',
    sa.Column('con_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('con_res_id', sa.Integer(), nullable=True),
    sa.Column('con_tenant_id', sa.Integer(), nullable=True),
    sa.Column('con_lessor_id', sa.Integer(), nullable=True),
    sa.Column('con_tenant_option', sa.Boolean(), nullable=True),
    sa.Column('con_lessor_option', sa.Boolean(), nullable=True),
    sa.Column('con_state_id', sa.Integer(), nullable=True),
    sa.Column('con_disclaimer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['con_disclaimer_id'], ['disclaimer.disclaimer_id'], ),
    sa.ForeignKeyConstraint(['con_lessor_id'], ['user.user_id'], ),
    sa.ForeignKeyConstraint(['con_res_id'], ['reservation.res_id'], ),
    sa.ForeignKeyConstraint(['con_state_id'], ['contractstate.constate_id'], ),
    sa.ForeignKeyConstraint(['con_tenant_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('con_id'),
    sa.UniqueConstraint('con_id')
    )
    op.add_column('user', sa.Column('address', sa.String(length=100), nullable=False))
    op.add_column('user', sa.Column('email', sa.String(length=100), nullable=False))
    op.add_column('user', sa.Column('id_card', sa.String(length=100), nullable=False))
    op.add_column('user', sa.Column('name', sa.String(length=100), nullable=False))
    op.add_column('user', sa.Column('nickname', sa.String(length=100), nullable=False))
    op.add_column('user', sa.Column('password', sa.String(length=100), nullable=False))
    op.add_column('user', sa.Column('phone', sa.String(length=50), nullable=False))
    op.add_column('user', sa.Column('registerdate', sa.DateTime(), nullable=False))
    op.add_column('user', sa.Column('role_id', sa.Integer(), nullable=True))
    op.create_unique_constraint(None, 'user', ['user_id'])
    op.create_foreign_key(None, 'user', 'role', ['role_id'], ['role_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'role_id')
    op.drop_column('user', 'registerdate')
    op.drop_column('user', 'phone')
    op.drop_column('user', 'password')
    op.drop_column('user', 'nickname')
    op.drop_column('user', 'name')
    op.drop_column('user', 'id_card')
    op.drop_column('user', 'email')
    op.drop_column('user', 'address')
    op.drop_table('contract')
    op.drop_table('comment')
    op.drop_table('reservation')
    op.drop_table('accommodationimage')
    op.drop_table('travelmessage')
    op.drop_table('disclaimer')
    op.drop_table('accommodation')
    op.drop_table('role')
    op.drop_table('resstate')
    op.drop_table('contractstate')
    op.drop_table('city')
    op.drop_table('accommodationtype')
    # ### end Alembic commands ###
