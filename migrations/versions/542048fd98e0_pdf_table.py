"""pdf table

Revision ID: 542048fd98e0
Revises: 
Create Date: 2024-12-14 01:56:12.497703

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '542048fd98e0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pdf',
    sa.Column('source', sa.String(length=50), nullable=False),
    sa.Column('file', sa.LargeBinary(), nullable=False),
    sa.PrimaryKeyConstraint('source')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pdf')
    # ### end Alembic commands ###
