"""Update model class

Revision ID: 7ccd889298cc
Revises: b4cb613abe68
Create Date: 2022-05-14 22:02:31.576709

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7ccd889298cc'
down_revision = 'b4cb613abe68'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'users', ['user_id'], ['id'])
    op.add_column('pitches', sa.Column('pitch', sa.String(length=255), nullable=False))
    op.add_column('pitches', sa.Column('pitch_time', sa.DateTime(), nullable=True))
    op.alter_column('pitches', 'title',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.create_index(op.f('ix_pitches_category'), 'pitches', ['category'], unique=False)
    op.drop_column('pitches', 'post')
    op.drop_column('pitches', 'post_time')
    op.add_column('votes', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'votes', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'votes', type_='foreignkey')
    op.drop_column('votes', 'user_id')
    op.add_column('pitches', sa.Column('post_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('pitches', sa.Column('post', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_pitches_category'), table_name='pitches')
    op.alter_column('pitches', 'title',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.drop_column('pitches', 'pitch_time')
    op.drop_column('pitches', 'pitch')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'user_id')
    # ### end Alembic commands ###
