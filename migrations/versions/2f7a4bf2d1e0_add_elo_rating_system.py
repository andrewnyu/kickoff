"""Add elo rating system

Revision ID: 2f7a4bf2d1e0
Revises: 
Create Date: 2020-05-09 17:00:16.799065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f7a4bf2d1e0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('player',
    sa.Column('player_id', sa.Integer(), nullable=False),
    sa.Column('sofifa_id', sa.Integer(), nullable=True),
    sa.Column('club', sa.String(length=64), nullable=True),
    sa.Column('country', sa.String(length=64), nullable=True),
    sa.Column('short_name', sa.String(length=128), nullable=True),
    sa.Column('long_name', sa.String(length=128), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('overall', sa.Integer(), nullable=True),
    sa.Column('potential', sa.Integer(), nullable=True),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.Column('wage', sa.Integer(), nullable=True),
    sa.Column('player_position', sa.String(length=128), nullable=True),
    sa.Column('preferred_foot', sa.String(length=128), nullable=True),
    sa.Column('elo_ranking', sa.Integer(), nullable=True),
    sa.Column('cumulative_score', sa.Integer(), nullable=True),
    sa.Column('num_selections', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('player_id')
    )
    op.create_index(op.f('ix_player_club'), 'player', ['club'], unique=False)
    op.create_index(op.f('ix_player_country'), 'player', ['country'], unique=False)
    op.create_index(op.f('ix_player_elo_ranking'), 'player', ['elo_ranking'], unique=False)
    op.create_index(op.f('ix_player_height'), 'player', ['height'], unique=False)
    op.create_index(op.f('ix_player_long_name'), 'player', ['long_name'], unique=True)
    op.create_index(op.f('ix_player_overall'), 'player', ['overall'], unique=False)
    op.create_index(op.f('ix_player_potential'), 'player', ['potential'], unique=False)
    op.create_index(op.f('ix_player_short_name'), 'player', ['short_name'], unique=True)
    op.create_index(op.f('ix_player_sofifa_id'), 'player', ['sofifa_id'], unique=False)
    op.create_index(op.f('ix_player_value'), 'player', ['value'], unique=False)
    op.create_index(op.f('ix_player_wage'), 'player', ['wage'], unique=False)
    op.create_index(op.f('ix_player_weight'), 'player', ['weight'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('team', sa.String(length=64), nullable=True),
    sa.Column('player', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('result',
    sa.Column('result_no', sa.Integer(), nullable=False),
    sa.Column('player1_id', sa.Integer(), nullable=True),
    sa.Column('player2_id', sa.Integer(), nullable=True),
    sa.Column('selection', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('result_no')
    )
    op.create_index(op.f('ix_result_player1_id'), 'result', ['player1_id'], unique=False)
    op.create_index(op.f('ix_result_player2_id'), 'result', ['player2_id'], unique=False)
    op.create_index(op.f('ix_result_timestamp'), 'result', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_result_timestamp'), table_name='result')
    op.drop_index(op.f('ix_result_player2_id'), table_name='result')
    op.drop_index(op.f('ix_result_player1_id'), table_name='result')
    op.drop_table('result')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_player_weight'), table_name='player')
    op.drop_index(op.f('ix_player_wage'), table_name='player')
    op.drop_index(op.f('ix_player_value'), table_name='player')
    op.drop_index(op.f('ix_player_sofifa_id'), table_name='player')
    op.drop_index(op.f('ix_player_short_name'), table_name='player')
    op.drop_index(op.f('ix_player_potential'), table_name='player')
    op.drop_index(op.f('ix_player_overall'), table_name='player')
    op.drop_index(op.f('ix_player_long_name'), table_name='player')
    op.drop_index(op.f('ix_player_height'), table_name='player')
    op.drop_index(op.f('ix_player_elo_ranking'), table_name='player')
    op.drop_index(op.f('ix_player_country'), table_name='player')
    op.drop_index(op.f('ix_player_club'), table_name='player')
    op.drop_table('player')
    # ### end Alembic commands ###