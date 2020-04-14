"""Add foreign key to results table

Revision ID: 4d5a67a10b8a
Revises: 559941bd1444
Create Date: 2020-04-14 20:42:29.094973

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d5a67a10b8a'
down_revision = '559941bd1444'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('result', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'result', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'result', type_='foreignkey')
    op.drop_column('result', 'user_id')
    # ### end Alembic commands ###
