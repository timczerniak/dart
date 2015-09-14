# DART
A script for judging when to leave for the DART (Dublin Area Rapid Transit, it's a train line in Dublin).

## Example
You want to leave from Tara Street, go southbound, and the walk time to the station is 10 mins
```bash
$ ./dart.py "Tara Street" --southbound --walk-time 10
Destination     Due  Departs   Leave
Bray         14 min    19:13   4 min
Greystones   29 min    19:28  19 min
Bray         44 min    19:43  34 min
Greystones   59 min    19:58  49 min
Bray         74 min    20:13  64 min
Greystones   90 min    20:29  80 min
```
