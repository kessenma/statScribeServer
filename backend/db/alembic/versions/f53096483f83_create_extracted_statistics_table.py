"""Create extracted_statistics table

Revision ID: f53096483f83
Revises: 297d890fec7d
Create Date: 2024-07-04 22:53:27.412036

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f53096483f83'
down_revision: Union[str, None] = '297d890fec7d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('extracted_statistics',
                    sa.Column('stat_id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('user_id', sa.Integer(), sa.ForeignKey('user_accounts.user_id'), nullable=False),
                    sa.Column('source_citation', sa.Text(), nullable=False),
                    sa.Column('publication_name', sa.String(255), nullable=False),
                    sa.Column('publication_year', sa.Integer(), nullable=False),
                    sa.Column('publication_type', sa.String(50), nullable=False),
                    sa.Column('paper_title', sa.String(255), nullable=False),
                    sa.Column('abstract', sa.Text(), nullable=False),
                    sa.Column('hypotheses', sa.Text(), nullable=True),
                    sa.Column('sample_size', sa.Integer(), nullable=False),
                    sa.Column('participant_mean_age', sa.Integer(), nullable=True),
                    sa.Column('participants_age_standard_deviation', sa.Integer(), nullable=True),
                    sa.Column('number_of_females', sa.Integer(), nullable=True),
                    sa.Column('participants_country_of_origin', sa.String(255), nullable=True),
                    sa.Column('sample_type', sa.String(255), nullable=True),
                    sa.Column('participant_education_level', sa.String(255), nullable=True),
                    sa.Column('participant_race_or_ethnicity', sa.String(255), nullable=True),
                    sa.Column('research_method', sa.String(255), nullable=True),
                    sa.Column('study_setting', sa.String(255), nullable=True),
                    sa.Column('research_task_description_for_participants', sa.Text(), nullable=True),
                    sa.Column('task_duration', sa.Integer(), nullable=True),
                    sa.Column('other_statistics', sa.JSONB(), nullable=True),
                    sa.PrimaryKeyConstraint('stat_id')
                    )



def downgrade():
    op.drop_table('extracted_statistics')
    # ### end Alembic commands ###
