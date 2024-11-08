"""Add costs

Revision ID: 000002
Revises: 000001
Create Date: 2023-05-05 13:15:23.742633

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = "000002"
down_revision = "000001"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "invoice_consumption_log", sa.Column("calculated_costs_applied_tax_percentage", sa.Float(), nullable=True)
    )
    op.add_column(
        "invoice_consumption_log", sa.Column("calculated_costs_currency", sa.String(length=128), nullable=True)
    )
    op.add_column("invoice_consumption_log", sa.Column("calculated_costs_without_tax", sa.Float(), nullable=True))
    op.add_column("invoice_consumption_log", sa.Column("calculated_tax_from_costs", sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("invoice_consumption_log", "calculated_tax_from_costs")
    op.drop_column("invoice_consumption_log", "calculated_costs_without_tax")
    op.drop_column("invoice_consumption_log", "calculated_costs_currency")
    op.drop_column("invoice_consumption_log", "calculated_costs_applied_tax_percentage")
    # ### end Alembic commands ###
