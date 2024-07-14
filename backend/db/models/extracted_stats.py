# backend/db/models/extracted_stats.py
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

Base = declarative_base()

class Statistics(Base):
    __tablename__ = 'extracted_statistics'
    stat_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user_accounts.user_id'), nullable=False)
    source_citation = Column(Text, nullable=False)
    publication_name = Column(String(255), nullable=False)
    publication_year = Column(Integer, nullable=False)
    publication_type = Column(String(50), nullable=False)
    paper_title = Column(String(255), nullable=False)
    abstract = Column(Text, nullable=False)
    hypotheses = Column(Text, nullable=True)
    sample_size = Column(Integer, nullable=False)
    participant_mean_age = Column(Integer, nullable=True)
    participants_age_standard_deviation = Column(Integer, nullable=True)
    number_of_females = Column(Integer, nullable=True)
    participants_country_of_origin = Column(String(255), nullable=True)
    sample_type = Column(String(255), nullable=True)
    participant_education_level = Column(String(255), nullable=True)
    participant_race_or_ethnicity = Column(String(255), nullable=True)
    research_method = Column(String(255), nullable=True)
    study_setting = Column(String(255), nullable=True)
    research_task_description_for_participants = Column(Text, nullable=True)
    task_duration = Column(Integer, nullable=True)
    other_statistics = Column(JSONB, nullable=True)
    user = relationship("User", back_populates="statistics")

    def __repr__(self):
        return f"<Statistics(paper_title='{self.paper_title}')>"
