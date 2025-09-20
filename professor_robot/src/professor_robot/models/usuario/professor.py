from sqlalchemy import UUID, Column, ForeignKey

from ..base import Base


class Professor(Base):
    __tablename__ = "professores"

    id = Column(UUID(as_uuid=True), ForeignKey("usuarios.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "professor",
    }
