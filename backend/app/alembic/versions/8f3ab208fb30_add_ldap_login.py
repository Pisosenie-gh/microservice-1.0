"""Add ldap login

Revision ID: 8f3ab208fb30
Revises: b361666f692e
Create Date: 2022-04-19 07:44:53.687985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f3ab208fb30'
down_revision = 'b361666f692e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ldap-login',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(), nullable=True),
    sa.Column('isActive', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ldap-login_id'), 'ldap-login', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_ldap-login_id'), table_name='ldap-login')
    op.drop_table('ldap-login')
    # ### end Alembic commands ###
