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
    def Dump():
        for item in Logs.__list:
            print( "<<< ERROR !!! >>>" )
            print( Error.toMessage(item.errorId) )
            if item.bodyMessage is not None:
                print( "- - - - - - - - -" )
                print( item.bodyMessage )
            print( "^^^^^^^^^^^^^^^^^" )

