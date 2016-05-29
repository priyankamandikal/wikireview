"""added table roles

Revision ID: c63b38933176
Revises: 738885178785
Create Date: 2016-05-29 23:58:46.139844

"""

# revision identifiers, used by Alembic.
revision = 'c63b38933176'
down_revision = '738885178785'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('default', sa.Boolean(), nullable=True),
    sa.Column('permissions', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    op.add_column('reviewers', sa.Column('role_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'reviewers', 'roles', ['role_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'reviewers', type_='foreignkey')
    op.drop_column('reviewers', 'role_id')
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    op.drop_table('roles')
    ### end Alembic commands ###
