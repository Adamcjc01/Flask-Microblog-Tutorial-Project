"""New fields in user model

Revision ID: dcedaecbec88
Revises: ac6cc7e1f9f1
Create Date: 2020-06-12 09:23:42.255180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dcedaecbec88'
down_revision = 'ac6cc7e1f9f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    op.drop_column('user', 'password_has')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password_has', sa.VARCHAR(length=128), nullable=True))
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
