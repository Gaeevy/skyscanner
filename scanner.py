from sources import get_response
from parsers import get_flights_details
import sys
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=2)
def timed_job():
    source = get_response(pattern_url)
    flights = get_flights_details(source)
    print('{} printing flights:'.format(datetime.datetime.now()))
    print(flights)
    sys.stdout.flush()


depart = 'reyk'
arrive = 'waw'
date = '190919'

pattern_url = f'https://www.skyscanner.ru/transport/flights/{depart}/{arrive}/{date}/?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=0&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&ref=home&currency=USD#results'

if __name__ == "__main__":
    print('{} Scheduler start'.format(datetime.datetime.now()))
    sched.start()
