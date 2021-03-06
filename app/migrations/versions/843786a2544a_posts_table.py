"""posts table

Revision ID: 843786a2544a
Revises: 0fd3acfbed11
Create Date: 2020-06-05 22:16:05.161248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '843786a2544a'
down_revision = '0fd3acfbed11'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist', sa.String(length=140), nullable=True),
    sa.Column('artwork', sa.String(length=140), nullable=True),
    sa.Column('medium', sa.String(length=140), nullable=True),
    sa.Column('location', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_table('post')
    # ### end Alembic commands ###
