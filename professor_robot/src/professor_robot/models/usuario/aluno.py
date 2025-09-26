from sqlalchemy import UUID, Column, Date, ForeignKey, Integer

from ..base import Base


class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(UUID(as_uuid=True), ForeignKey("usuarios.id"), primary_key=True)
    data_nascimento = Column(Date, nullable=False)
    nivel = Column(Integer, default=1)
    xp = Column(Integer, default=0)

    __mapper_args__ = {
        "polymorphic_identity": "aluno",
    }
