Polar2Strava
============

Allow to convert Polar (RC3 for the moment) trainings to Strava very easily

Requirements
------------

* Python 2.7
* awk in your path (due to current implementation of converted based on http://colby.id.au/combining-gpx-and-hrm-files/) 

Installation
------------

Clone this repository.

Usage
-----

Run python polar2strava.py --folder=data [--email=raymond.barre@gmail.com]
(the email passed has to be the one associated to your Strava account).
Connect to Strava a few minutes later and go to "new activites tab"
