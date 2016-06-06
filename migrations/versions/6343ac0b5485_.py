"""empty message

Revision ID: 6343ac0b5485
Revises: de70b8fe2f4a
Create Date: 2016-06-02 17:15:41.835938

"""

# revision identifiers, used by Alembic.
revision = '6343ac0b5485'
down_revision = 'de70b8fe2f4a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    op.drop_table('sqlite_stat1')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sqlite_stat1',
    sa.Column('tbl', sa.NullType(), nullable=True),
    sa.Column('idx', sa.NullType(), nullable=True),
    sa.Column('stat', sa.NullType(), nullable=True)
    )
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_table('post')
    ### end Alembic commands ###