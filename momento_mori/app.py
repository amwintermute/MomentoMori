from datetime import date

class timeLeft:
    def days():
        reaper  = date(year=2070, month=5, day=19)
        today   = date.today()
        return reaper - today

    def years():
        reaper    = date(year=2070, month=5, day=19)
        today     = date.today()
        this_year = today.year
        return reaper.year - this_year
