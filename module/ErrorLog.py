#
# エラーログ
# 
from . import Error

class Log:
    def __init__( self, error_id=Error.eID.NoError, body_message=None ):
        self.errorId = error_id
        self.bodyMessage = body_message

class Logs:
    __list = []

    def __init__( self ):
        Logs.__list = []
    
    @staticmethod
    def Add( log ):
        Logs.__list.append( log )
    
    @staticmethod
    def Clear():
        Logs.__list.clear()
    
    @staticmethod
    def IsErrors():
        return 0 < len(Logs.__list)
    
    @staticmethod
    def Dump( output_file=None ):
        def OutputLog( str ):
            if output_file is not None:
                output_file.write( str + '\n' )
            print( str )

        for item in Logs.__list:
            OutputLog( "<<< ERROR !!! >>>" )
            OutputLog( Error.toMessage(item.errorId) )
            if item.bodyMessage is not None:
                OutputLog( "- - - - - - - - -" )
                OutputLog( item.bodyMessage )
            OutputLog( "^^^^^^^^^^^^^^^^^" )

