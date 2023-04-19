import constants as c
from constants import defenders_data
import arcade
from bullet import Bullet
from defender import Defender
from sun import Sun


class Sunflower(Defender):
    def __init__(self, type, lane):
        super().__init__(type, lane, None, 0)
        self.wait_time = c.SUNFLOWER_WAIT_TIME
        self.has_sun = False
        self.time_without_sun = 0
        self.sun = None

    def collect_sun(self) -> Sun:
        if self.has_sun:
            self.time_without_sun = 0
            self.has_sun = False
            tmp = self.sun
            self.sun = None
            return tmp

    def spawn_sun(self) -> Sun:
        if not self.has_sun:
            self.has_sun = True
            self.sun = Sun(sunflower_sun=True)
            return self.sun

    def on_update(self, delta_time: float = 1 / 60) -> Sun:
        self.time_without_sun += delta_time
        if not self.has_sun:
            if self.time_without_sun > self.wait_time:
                return self.spawn_sun()
        else:
            self.sun.on_update(delta_time)
            if self.sun.lifespan <= 0:
                self.collect_sun()
