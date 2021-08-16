import datetime

import pandas as pd


from qstrader import settings
from qstrader.simulation.sim_engine import SimulationEngine
from qstrader.simulation.event import SimulationEvent


class EverydaySimulationEngine(SimulationEngine):
    """A simulation engine where the market never sleep.

    Market open and close events are still emitted, because how QSTrader is wired up.
    """

    def __init__(self, starting_day, ending_day, pre_market=True, post_market=True):
        if ending_day < starting_day:
            raise ValueError(
                "Ending date time %s is earlier than starting date time %s. "
                "Cannot create DailyBusinessDaySimulationEngine "
                "instance." % (ending_day, starting_day)
            )

        self.starting_day = starting_day
        self.ending_day = ending_day
        self.pre_market = pre_market
        self.post_market = post_market
        self.trading_days = self._generate_trading_days()

    def _generate_trading_days(self):
        """
        Generate the list of business days using midnight UTC as
        the timestamp.

        Returns
        -------
        `list[pd.Timestamp]`
            The business day range list.
        """
        days = pd.date_range(
            self.starting_day, self.ending_day,
        )
        return days

    def __iter__(self):
        """
        Generate the daily timestamps and event information
        for pre-market, market open, market close and post-market.

        Yields
        ------
        `SimulationEvent`
            Market time simulation event to yield
        """
        for index, bday in enumerate(self.trading_days):
            year = bday.year
            month = bday.month
            day = bday.day

            if self.pre_market:
                yield SimulationEvent(
                    pd.Timestamp(
                        datetime.datetime(year, month, day), tz=settings.TIMEZONE,
                    ), event_type="pre_market"
                )

            yield SimulationEvent(
                pd.Timestamp(
                    datetime.datetime(year, month, day, 14, 30),
                    tz=settings.TIMEZONE,
                ), event_type="market_open"
            )

            yield SimulationEvent(
                pd.Timestamp(
                    datetime.datetime(year, month, day, 21, 00),
                    tz=settings.TIMEZONE,
                ), event_type="market_close"
            )

            if self.post_market:
                yield SimulationEvent(
                    pd.Timestamp(
                        datetime.datetime(year, month, day, 23, 59), tz=settings.TIMEZONE,
                    ), event_type="post_market"
                )
