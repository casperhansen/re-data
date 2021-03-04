"""Add grafana url

Revision ID: fd3174b5f939
Revises: 1bf7cfcbcf23
Create Date: 2021-02-24 09:20:00.897497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "fd3174b5f939"
down_revision = "1bf7cfcbcf23"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "monitored_table", sa.Column("grafana_url", sa.String(), nullable=True)
    )
    op.drop_column("monitored_table", "time_column_type")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("monitored_table", "grafana_url")
    op.add_column("monitored_table", "time_column_type", sa.String(), nullable=True),
    # ### end Alembic commands ###
