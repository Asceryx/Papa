from sqlalchemy import Column, Integer, String, Text, Boolean, Enum
from config.database import Base, init, persistent
from models.database.db_pin import PinModel
from models.Captor import Type


class CaptorModel(Base):
    __tablename__ = 'captor'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(Text(250))
    shutdown = Column(Boolean, nullable=False)
    pause = Column(Boolean, nullable=False)
    type = Column(Enum(Type))

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'captor',
    }


if __name__ == '__main__':
    init()
    captor = CaptorModel(name='led', shutdown=False, pause=False, type=Type.TOR)
    pin1 = PinModel(channel='12', board_configuration='BCM')
    pin2 = PinModel(channel='13', board_configuration='BCM')

    captor.pins.append(pin1)
    captor.pins.append(pin2)

    persistent(pin1)
    persistent(pin2)
    persistent(captor)
