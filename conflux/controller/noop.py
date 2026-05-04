"""No-op controller that does nothing."""

from __future__ import annotations

from fractions import Fraction

from conflux.clock import SimulationClock
from conflux.controller.base import Controller
from conflux.datacenter.base import DatacenterBackend
from conflux.datacenter.command import DatacenterCommand
from conflux.events import EventEmitter
from conflux.grid.base import GridBackend
from conflux.grid.command import GridCommand


class NoopController(Controller[DatacenterBackend, GridBackend]):
    """Controller that always returns an empty action."""

    def __init__(self, dt_s: Fraction = Fraction(1)) -> None:
        self._dt_s = dt_s

    @property
    def dt_s(self) -> Fraction:
        return self._dt_s

    def reset(self) -> None:
        pass

    def step(
        self,
        clock: SimulationClock,
        events: EventEmitter,
    ) -> list[DatacenterCommand | GridCommand]:
        return []
