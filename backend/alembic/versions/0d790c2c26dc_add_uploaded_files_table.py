"""Add uploaded_files table

Revision ID: 0d790c2c26dc
Revises: aa3d85891014
Create Date: 2023-09-26 19:21:46.195955

"""
from alembic import op
import sqlalchemy as sa
from api.database.custom_types import UTCDateTime, Pydantic
from api.models.json import UploadedFileOpenaiWebInfo

# revision identifiers, used by Alembic.
revision = '0d790c2c26dc'
down_revision = 'aa3d85891014'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('uploaded_files',
                    sa.Column('id', sa.Uuid(), nullable=False, comment='uuid'),
                    sa.Column('original_filename', sa.String(length=256), nullable=False, comment='原始文件名'),
                    sa.Column('size', sa.Integer(), nullable=False, comment='文件大小(bytes)'),
                    sa.Column('content_type', sa.String(length=256), nullable=True, comment='文件类型'),
                    sa.Column('storage_path', sa.String(length=1024), nullable=True,
                              comment='文件在服务器的存储路径，相对于配置中的存储路径；为空表示未在服务器上存储，即未上传或者已清理'),
                    sa.Column('upload_time', UTCDateTime(timezone=True),
                              nullable=False, comment='上传日期'),
                    sa.Column('uploader_id', sa.Integer(), nullable=False, comment='上传的用户id'),
                    sa.Column('openai_web_info', Pydantic(UploadedFileOpenaiWebInfo), nullable=True),
                    sa.ForeignKeyConstraint(['uploader_id'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('uploaded_files')
    # ### end Alembic commands ###