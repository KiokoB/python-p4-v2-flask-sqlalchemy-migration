"""add Department

Revision ID: 33840f60beed
Revises: 8bdb01244372
Create Date: 2024-06-26 23:17:13.235158

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33840f60beed'
down_revision = '8bdb01244372'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
