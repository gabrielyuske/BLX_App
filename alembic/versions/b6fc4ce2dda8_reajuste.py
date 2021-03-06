"""Reajuste

Revision ID: b6fc4ce2dda8
Revises: 
Create Date: 2022-02-23 00:21:23.336881

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6fc4ce2dda8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pedido',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantidade', sa.Integer(), nullable=True),
    sa.Column('local_estrega', sa.String(), nullable=True),
    sa.Column('tipo_entrega', sa.String(), nullable=True),
    sa.Column('observacao', sa.String(), nullable=True),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.Column('produto_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['produto_id'], ['produto.id'], name='fk_pedido_produto'),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], name='fk_pedido_usuario'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('pedido', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_pedido_id'), ['id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pedido', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_pedido_id'))

    op.drop_table('pedido')
    # ### end Alembic commands ###
