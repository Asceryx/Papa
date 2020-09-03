from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, Enum

from config.database import init, persistent, Base, session
from models.Captor import Type
from models.database.db_captor import CaptorModel
from models.database.db_pin import PinModel


class LedModel(CaptorModel):
    __tablename__ = 'led'

    id = Column(Integer, ForeignKey('captor.id'), primary_key=True)
    bright = Column(Integer, nullable=False)
    light = Column(Boolean, nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs['shutdown']:
            self.bright = 0
            self.light = False

    __mapper_args__ = {
        'polymorphic_identity': Type.TOR,
    }


if __name__ == '__main__':
    init()
    l = LedModel(name='led', shutdown=False, pause=False, type=Type.TOR, bright=10, light=False)
    p = PinModel(channel=12,board_configuration='BCM', captor=l)
    p = PinModel(channel=13, board_configuration='BCM', captor=l)
    p = PinModel(channel=14, board_configuration='BCM', captor=l)
    p = PinModel(channel=15, board_configuration='BCM', captor=l)
    persistent(l)