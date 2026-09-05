# Models
#
# This contains the various dataclass models that are used
# to represent objects in the code.
from dataclasses import dataclass


# SpeedRun
@dataclass
class SpeedRun:
	player: str
	game: str
	category: str
	time: str
	raw: dict | None
	emulator: bool
	place: int | None
	link: str
	id: int | None
