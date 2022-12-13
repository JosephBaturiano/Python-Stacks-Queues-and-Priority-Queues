from sixthqueues import PriorityQueue
from dataclasses import dataclass

CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1


@dataclass
class Message:
    event: str


wipers = Message("Windshield wipers turned on")
hazard_lights = Message("Hazard lights turned on")

wipers < hazard_lights
