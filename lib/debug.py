#!/usr/bin/env python3
import ipdb

from classes.national_park import NationalPark
from classes.visitor import Visitor
from classes.trip import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    v1 = Visitor( 'adam' )
    v2 = Visitor( 'emiley' )

    np1 = NationalPark( 'Yosemite' )
    np2 = NationalPark( 'Red Rocks' )
    
    np3 = NationalPark( 'The Gunks')


    t1 = Trip( v1, np1, 'last week', 'tomorrow' )
    t4 = Trip( v1, np1, 'last weekagain', 'tomorrowagain' )

    Trip( v2, np1, '6/6', '12/10')
    t2 = Trip( v2, np2, 'today', 'next week' )
    
    ipdb.set_trace()
