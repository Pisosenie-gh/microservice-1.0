"""add replacement

Revision ID: b204068c1f55
Revises: 5209f48258e7
Create Date: 2022-04-20 08:42:46.756853

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b204068c1f55'
down_revision = '5209f48258e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('replacement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('startDate', sa.Date(), nullable=True),
    sa.Column('endDate', sa.Date(), nullable=True),
    sa.Column('isActive', sa.Integer(), nullable=True),
    sa.Column('typeId', sa.Integer(), nullable=True),
    sa.Column('replacedId', sa.Integer(), nullable=True),
    sa.Column('replacerId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['replacedId'], ['internal-employee.id'], ),
    sa.ForeignKeyConstraint(['replacerId'], ['internal-employee.id'], ),
    sa.ForeignKeyConstraint(['typeId'], ['replacement-type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_replacement_id'), 'replacement', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_replacement_id'), table_name='replacement')
    op.drop_table('replacement')
    # ### end Alembic commands ###
