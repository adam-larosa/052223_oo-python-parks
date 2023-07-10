class Visitor:

    def __init__(self, name):
        self.name = name
        
    def get_name( self ):
        return self._name

    def set_name( self, new_name ):
        if type( new_name ) == str:
            if 1 <= len( new_name ) <= 15:
                self._name = new_name
            else:
                raise Exception( 'Must be between 1 & 15 in length, inclusive' )
        else:
            raise Exception( 'Strings only please' )

    name = property( get_name, set_name )


    def trips( self ):
        from classes.trip import Trip
        # same but list comprehension
        # return [ t for t in Trip.all if t.visitor == self ]
        trip_list = []
        for trip in Trip.all:
            if trip.visitor == self:
                trip_list.append( trip )
        return trip_list
       
   

    def national_parks( self ):
        # antother list comprehension!
        # park_list = [ t.national_park for t in self.trips() ]
        # return list( set( park_list ) )
        park_list = []
        for trip in self.trips():
            park_list.append( trip.national_park )
        return list( set( park_list ) )