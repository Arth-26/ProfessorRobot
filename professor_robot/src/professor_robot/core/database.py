from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///professor_robot.db"

engine = create_engine(DATABASE_URL, echo=True)  # echo=True para log SQL
SessionLocal = sessionmaker(bind=engine)

# instância da sessão para ser usada no sistema
db_session = SessionLocal()
