"""Empty revision to fix missing migration

Revision ID: b86b1d554c2e
Revises: 001
Create Date: 2025-01-07 11:29:03.886520

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b86b1d554c2e'
down_revision = '001'
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
