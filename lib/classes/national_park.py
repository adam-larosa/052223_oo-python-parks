class NationalPark:

    def __init__(self, name):
        self.name = name
        
    
    def get_name( self ):
        return self._name

    def set_name( self, new_name ):
        if hasattr( self, '_name' ):
            raise Exception( 'Name can not be changed!' )
        else:
            self._name = new_name

    name = property( get_name, set_name )



    def trips( self ):
        from classes.trip import Trip
        return [ t for t in Trip.all if t.national_park == self ]
    
    def visitors( self ):


#                    what will end up
#                       in the set
#                          |
#                          V 
        visitor_set = { t.visitor for t in self.trips() }
#                                     ^
#                                     |
#                             a variable we are 
#                             declaring right here
#                           to represent one of the 
#                            "trips" in self.trips()

        # returning a list cause the README.md sez so.
        return list( visitor_set )
        


    
    def total_visits( self ):
        return len( self.trips() )
    
    # Returns the Visitor who has visited the park the most 
    def best_visitor(self):
        
        memory = {}
        for t in self.trips():
            if memory.get( t.visitor ):
                memory[ t.visitor ] += 1
            else:
                memory[ t.visitor ] = 1

        winner = { 'total': 0 }
        for instance, amount in memory.items():
            if amount > winner[ 'total' ]:
                winner[ 'name' ] = instance
                winner[ 'total' ] = amount
        return winner[ 'name' ]
            