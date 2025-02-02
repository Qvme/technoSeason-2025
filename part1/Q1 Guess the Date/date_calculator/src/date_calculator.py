class DateException(Exception):
    pass

# 0:"sun" ,1:"mon", 2:"tue", 3:"wed", 4:"thr", 5:"fri", 6:"sat"
class DateCalculator:
    def __init__(self, ref_date="1-1-2000", ref_day=6):
        self.ref_date = ref_date
        self.ref_day = ref_day
        if not DateCalculator.is_valid_date(self.ref_date):
            raise DateException("enter valid date mf")

    @staticmethod
    def is_leap(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @staticmethod
    def is_valid_date(date):
        dd, mm, yy = map(int, date.split("-"))

        if mm<1 or mm>12:
            return False

        else:
            if  dd<1 or DateCalculator.day(mm,yy) < dd:
                return False

        return True

    @staticmethod
    def day(month: int, year: int) -> int:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            return 29 if DateCalculator.is_leap(year) else 28

    def sort_dates(self, inp_date):
        d1, m1, y1 = map(int, self.ref_date.split("-"))
        d2, m2, y2 = map(int, inp_date.split("-"))
        if not DateCalculator.is_valid_date(inp_date):
            raise DateException("enter valid date mf")

        if (y2 > y1) or (y2 == y1 and m2 > m1) or (y2 == y1 and m2 == m1 and d2 > d1):
            is_future = True
            return self.ref_date, inp_date, is_future
        elif (y2 == y1) and (m2 == m1) and (d2 == d1):
            return (inp_date,)
            # dates are equal
        else:
            is_future = False
            return inp_date, self.ref_date, is_future  # input date is in the past

    def calc_days_bw(self, date1, date2):
        cnt = 0
        d1, m1, y1 = map(int, date1.split("-"))
        d2, m2, y2 = map(int, date2.split("-"))

        # Count full years between the two dates
        for y in range(y1 + 1, y2):
            cnt += 366 if self.is_leap(y) else 365

        if y2 > y1:
            # Count days in the upper half of the year y2
            for m in range(1, m2):
                cnt += self.day(m, y2)
            cnt += d2

            # Count days in the lower half of the year y1
            cntt = 0
            for m in range(1, m1):
                cntt += self.day(m, y1)
            cntt += d1
            cnt += ((366 if self.is_leap(y1) else 365) - cntt)

        if y2 == y1:
            for m in (m1 + 1, m2):
                cnt += self.day(m, y1)
            cnt += d2
            cnt += self.day(m1, y1) - d1

        return cnt

    def predict_day(self, inp_date):
        dday = {0:"sun" ,1:"mon", 2:"tue", 3:"wed", 4:"thr", 5:"fri", 6:"sat"}
        if len(self.sort_dates(inp_date)) == 1:
            return dday[self.ref_day]
            # return self.ref_day
        else:
            old, new, is_future = self.sort_dates(inp_date)
            gap = self.calc_days_bw(old, new)
            if is_future:
                return dday[(gap + self.ref_day) % 7]
                 # return (gap + self.ref_day) % 7
            else:
                return dday[(self.ref_day - gap) % 7]
                 # return (self.ref_day - gap) % 7

