import pandas as pd
import datetime
import requests
from xml.etree import ElementTree as ET


def get_currency_rates(date):
    url = f"http://cbr.ru/scripts/XML_daily.asp?date_req={date.strftime('%d/%m/%Y')}"
    response = requests.get(url)
    if response.status_code == 200:
        root = ET.fromstring(response.content)
        rates = {}
        for valute in root.findall('Valute'):
            code = valute.find('CharCode').text
            vunit_rate_element = valute.find('VunitRate')
            if vunit_rate_element is not None and vunit_rate_element.text:
                rates[code] = vunit_rate_element.text.replace(',', '.')
            else:
                rates[code] = None
        return rates
    else:
        return None


def main():
    start_date = datetime.date(2003, 1, 1)
    end_date = datetime.date(2023, 6, 1)

    dates = [start_date + datetime.timedelta(days=x) for x in range((end_date - start_date).days + 1)]
    first_day_of_month_dates = [d for d in dates if d.day == 1]

    all_rates = []
    for date in first_day_of_month_dates:
        rates = get_currency_rates(date)
        if rates:
            row = {'date': date.strftime('%Y-%m')}
            row.update(rates)
            all_rates.append(row)

    df = pd.DataFrame(all_rates)

    df.to_csv('data/currency.csv', index=False)


if __name__ == "__main__":
    main()