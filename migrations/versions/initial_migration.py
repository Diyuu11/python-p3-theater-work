"""Initial migration for roles and auditions tables.

Revision ID: <revision_id>
Revises: 
Create Date: <date>
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '<revision_id>'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Create roles table
    op.create_table(
        'roles',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('character_name', sa.String, nullable=False)
    )

    # Create auditions table
    op.create_table(
        'auditions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('actor', sa.String, nullable=False),
        sa.Column('location', sa.String, nullable=False),
        sa.Column('phone', sa.Integer, nullable=False),
        sa.Column('hired', sa.Boolean, default=False),
        sa.Column('role_id', sa.Integer, sa.ForeignKey('roles.id'))
    )

def downgrade():
    # Drop auditions table
    op.drop_table('auditions')

    # Drop roles table
    op.drop_table('roles')
