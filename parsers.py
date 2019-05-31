from lxml import html
import lxml.etree as et

items_xpath = '//ul[contains(@class, "day-list")]/li[contains(@class, "day-list-item")]'

depart_xpath = './/div[contains(@class, "LegInfo__leg-depart")]'
depart_time_xpath = './/span[contains(@class, "LegInfo__times")]'
depart_airport_xpath = './/span[contains(@class, "LegInfo__tooltipTarget")]'

duration_xpath = './/span[contains(@class, "LegInfo__duration")]'

arrive_xpath = './/div[contains(@class, "LegInfo__leg-arrive")]'
arrive_time_xpath = './/span[contains(@class, "LegInfo__times")]'
arrive_airport_xpath = './/span[contains(@class, "LegInfo__tooltipTarget")]'

price_xpath = './/a[contains(@class, "price")]'


def get_flights_details(source):
    tree = html.fromstring(source, parser=et.HTMLParser(remove_comments=True))
    items = tree.xpath(items_xpath)
    flights = []
    for item in items:
        flight = {}

        depart = item.xpath(depart_xpath)
        if depart:
            time = depart[0].xpath(depart_time_xpath)[0].text
            airport = depart[0].xpath(depart_airport_xpath)[0].text
            flight['depart_time'] = time
            flight['depart_airport'] = airport
        else:
            continue                     # seems like current item doesn't contain flight info, lets proceed with rest

        duration = item.xpath(duration_xpath)
        if duration:
            flight['duration'] = duration[0].text

        arrive = item.xpath(arrive_xpath)
        if arrive:
            time = arrive[0].xpath(arrive_time_xpath)[0].text
            airport = arrive[0].xpath(arrive_airport_xpath)[0].text
            flight['arrive_time'] = time
            flight['arrive_airport'] = airport

        price = item.xpath(price_xpath)
        if price:
            flight['price'] = price[0].text

        flights.append(flight)

    return flights
