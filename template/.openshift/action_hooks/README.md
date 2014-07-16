To use it :
    create account at Openshift.com
    create new application
    install rhc commandline tools (not needed if u work only from web console, but recommended)
    copy paste http://cartreflect-claytondev.rhcloud.com/github/v3ss0n/openshift-mongox-unbound at the bottom box
    
Categories:
  - service
  - web_framework
  - database
  - nosql

Provides:
  - mongodb
  - mongodb-2.6

Dedicated Latest Mongo 2.6 with Extra Port so it can be connected from any other application nodes, 
strip down to only 44MB of binary to MAXIMIZE free disk space. Takes up to 400~ MB of Journal,though.
This make it possible to bypass Openshift Limitation of databases unable to run its own gears
and non-scalable apps running at other gears unable to connect to dedicated database.

Installation
    
    rhc app create dev http://cartreflect-claytondev.rhcloud.com/github/v3ss0n/openshift-mongox-unbound

