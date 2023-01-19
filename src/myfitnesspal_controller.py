import myfitnesspal
from decorators import mfp
import datetime


@mfp
def get_day_totals(date: datetime.date, client: myfitnesspal.Client) -> dict[str, float]:
    day_results = client.get_date(date.year, date.month, date.day)
    return day_results.totals


def main():
    date = datetime.date.today()
    print(get_day_totals(date))


if __name__ == '__main__':
    main()
