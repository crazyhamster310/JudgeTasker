"""increase source length

Revision ID: e336621923e6
Revises: 542048fd98e0
Create Date: 2024-12-16 11:00:00.309916

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e336621923e6'
down_revision = '542048fd98e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pdf', schema=None) as batch_op:
        batch_op.alter_column('source',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=100),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pdf', schema=None) as batch_op:
        batch_op.alter_column('source',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=50),
               existing_nullable=False)

    # ### end Alembic commands ###
