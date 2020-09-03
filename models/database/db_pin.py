from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from config.database import Base


class PinModel(Base):
    __tablename__ = 'pin'

    id = Column(Integer, primary_key=True)
    channel = Column(Integer)
    board_configuration = Column(String(50))
    captor_id = Column(Integer, ForeignKey('captor.id'))
    captor = relationship("CaptorModel", backref='pins')