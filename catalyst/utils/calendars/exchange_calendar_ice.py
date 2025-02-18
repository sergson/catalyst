from datetime import time
from itertools import chain

from pandas.tseries.holiday import (
    GoodFriday,
    USPresidentsDay,
    USLaborDay,
    USThanksgivingDay
)
import pandas as pd
from distutils.version import StrictVersion
pandas_version = StrictVersion(pd.__version__)
new_pandas = pandas_version >= StrictVersion('0.19')
if pandas_version >= StrictVersion('0.20'):
    from pandas import Timestamp
else:
    from pandas.tslib import Timestamp
from pytz import timezone

from catalyst.utils.calendars import TradingCalendar
from catalyst.utils.calendars.trading_calendar import HolidayCalendar
from catalyst.utils.calendars.us_holidays import (
    USNewYearsDay,
    Christmas,
    USMartinLutherKingJrAfter1998,
    USMemorialDay,
    USIndependenceDay,
    USNationalDaysofMourning)


class ICEExchangeCalendar(TradingCalendar):
    """
    Exchange calendar for ICE US.

    Open Time: 8pm, US/Eastern
    Close Time: 6pm, US/Eastern

    https://www.theice.com/publicdocs/futures_us/ICE_Futures_US_Regular_Trading_Hours.pdf # noqa
    """
    @property
    def name(self):
        return "ICE"

    @property
    def tz(self):
        return timezone("US/Eastern")

    @property
    def open_time(self):
        return time(20, 1)

    @property
    def close_time(self):
        return time(18)

    @property
    def open_offset(self):
        return -1

    @property
    def special_closes(self):
        return [
            (time(13), HolidayCalendar([
                USMartinLutherKingJrAfter1998,
                USPresidentsDay,
                USMemorialDay,
                USIndependenceDay,
                USLaborDay,
                USThanksgivingDay
            ]))
        ]

    @property
    def adhoc_holidays(self):
        return list(chain(
            USNationalDaysofMourning,
            # ICE was only closed on the first day of the Hurricane Sandy
            # closings (was not closed on 2012-10-30)
            [Timestamp('2012-10-29', tz='UTC')]
        ))

    @property
    def regular_holidays(self):
        # https://www.theice.com/publicdocs/futures_us/exchange_notices/NewExNot2016Holidays.pdf # noqa
        return HolidayCalendar([
            USNewYearsDay,
            GoodFriday,
            Christmas
        ])
