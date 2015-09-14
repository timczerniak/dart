# DART
The DART is a train system in Dublin (Dublin Area Rapid Transit)

It has an API, and so this is a script for judging when to leave for the DART.

It will tell you the next few trains, their destination, departure time, and
when you should leave your current location to catch them.

## Help
```
$ ./dart.py --help
usage: dart.py [-h] (-n | -s) [-w WALK_TIME] departure_station

positional arguments:
  departure_station     The departure station

optional arguments:
  -h, --help            show this help message and exit
  -n, --northbound      Use this if you're going northbound
  -s, --southbound      Use this if you're going southbound
  -w WALK_TIME, --walk-time WALK_TIME
                        The walk time (in minutes) from where you are to the
                        departure station
```

## Example
You want to leave from Tara Street, go southbound, and the walk-time to the station is 10 mins
```
$ ./dart.py "Tara Street" --southbound --walk-time 10
Destination     Due  Departs   Leave
Bray         14 min    19:13   4 min
Greystones   29 min    19:28  19 min
Bray         44 min    19:43  34 min
Greystones   59 min    19:58  49 min
Bray         74 min    20:13  64 min
Greystones   90 min    20:29  80 min
```
