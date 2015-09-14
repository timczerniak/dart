#!/usr/bin/env python
"""
API info at http://api.irishrail.ie/realtime/
"""

import httplib, urllib
import argparse
from xml.etree import ElementTree


HOST = "api.irishrail.ie"
NS = {'irishrail': "http://%s/realtime/" % HOST}


class Train():

    def __init__(self, dom):
        self.dom = dom
        self.type = self.dom.find('irishrail:Traintype', NS).text
        self.is_dart = self.type == "DART"
        self.destination = self.dom.find('irishrail:Destination', NS).text
        self.direction = self.dom.find('irishrail:Direction', NS).text
        self.due_in = int(self.dom.find('irishrail:Duein', NS).text)
        self.dep_time = self.dom.find('irishrail:Schdepart', NS).text

    def is_catchable(self, walk_time):
        return self.due_in > walk_time

    def when_to_leave(self, walk_time):
        if self.is_catchable(walk_time):
            return self.due_in - walk_time


def get_dom(url):
    conn = httplib.HTTPConnection(HOST)
    conn.request("GET", url)
    resp = conn.getresponse()
    if resp.status != 200:
        raise Exception("HTTP Error: %s" % resp)
    xml = resp.read()
    conn.close()
    return ElementTree.fromstring(xml)


def get_trains(station):
    url = "/realtime/realtime.asmx/getStationDataByNameXML" \
          "?StationDesc=%s" % station
    dom = get_dom(url)
    return [Train(train_dom) for train_dom in dom]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "departure_station",
        help="The departure station",
    )
    dir_grp = parser.add_mutually_exclusive_group(required=True)
    dir_grp.add_argument(
        "-n", "--northbound",
        action="store_const",
        const="Northbound",
        dest="direction",
        help="Use this if you're going northbound",
    )
    dir_grp.add_argument(
        "-s", "--southbound",
        action="store_const",
        const="Southbound",
        dest="direction",
        help="Use this if you're going southbound",
    )
    parser.add_argument(
        "-w", "--walk-time",
        help="The walk time (in minutes) from where you are to the "
             "departure station",
        type=int,
        default=0,
    )
    args = parser.parse_args()

    trains = get_trains(args.departure_station.replace(" ", "%20"))

    line_format = '{:<11s}  {:>6s}  {:>7s}  {:>6s}'
    print line_format.format("Destination", "Due", "Departs", "Leave", "")
    for train in trains:
        if train.is_dart and train.direction == args.direction:
            #catchable = "*" if train.is_catchable(WALK_TIME) else " "
            when_to_leave = train.when_to_leave(args.walk_time)
            leave_in = (
                "%s min" % when_to_leave
                if when_to_leave is not None
                else ""
            )
            print line_format.format(
                train.destination,
                "%s min" % train.due_in,
                train.dep_time,
                leave_in
            )


if __name__ == "__main__":
    main()
