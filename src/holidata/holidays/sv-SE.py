# coding=utf-8
from dateutil.easter import EASTER_WESTERN

from holidata.utils import SmartDayArrow
from .holidays import Locale, Holiday

"""
source: https://www.riksdagen.se/sv/dokument-lagar/dokument/svensk-forfattningssamling/lag-1989253-om-allmanna-helgdagar_sfs-1989-253
source: https://www.riksdagen.se/sv/dokument-lagar/dokument/svensk-forfattningssamling/semesterlag-1977480_sfs-1977-480
"""


class sv_SE(Locale):
    """
    01-01: [NF] Nyårsdagen
    01-06: [NRF] Trettondedag jul
    05-01: [NF] Första maj
    06-06: [NF] Nationaldagen
    12-24: [NRF] Julafton
    12-25: [NRF] Juldagen
    12-26: [NRF] Annandag jul
    12-31: [NF] Nyårsafton
    2 days before Easter: [NRV] Långfredagen
    Easter: [NRV] Påskdagen
    1 day after Easter: [NRV] Annandag påsk
    39 days after Easter: [NRV] Kristi himmelsfärdsdag
    49 days after Easter: [NRV] Pingstdagen
    """

    id = "sv-SE"
    easter_type = EASTER_WESTERN

    def __midsommar(self, year):
        """
        Find the Saturday between 20 and 26 June
        """
        return SmartDayArrow(year, 6, 19).shift_to_weekday("saturday", order=1, reverse=False)

    def holiday_midsommarafton(self, year):
        """
        The day before midsommardagen: [NV] Midsommarafton
        """
        return [Holiday(
            self.id,
            "",
            self.__midsommar(year).shift(days=-1),
            "Midsommarafton",
            "NV"
        )]

    def holiday_midsommardagen(self, year):
        """
        Saturday between 20 and 26 June: [NV] Midsommardagen
        """
        return [Holiday(
            self.id,
            "",
            self.__midsommar(year),
            "Midsommardagen",
            "NV"
        )]

    def holiday_alla_helgons_dag(self, year):
        """
        Saturday between 31 October and 6 November: [NRV] Alla helgons dag
        """
        return [Holiday(
            self.id,
            "",
            SmartDayArrow(year, 10, 30).shift_to_weekday("saturday", order=1, reverse=False),
            "Alla helgons dag",
            "NRV"
        )]
