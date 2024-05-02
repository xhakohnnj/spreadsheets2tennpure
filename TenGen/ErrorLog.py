#
# エラーログ
# 
import io
from . import Error

# ログ
class Log:
    def __init__( self, error_id:Error.eID=Error.eID.NoError, body_message:str=None ):
        self.errorId = error_id
        self.bodyMessage = body_message

# ログリスト
class Logs:
    __list = []

    def __init__( self ):
        Logs.__list = []
    
    # 追加
    @staticmethod
    def Add( log ):
        Logs.__list.append( log )
    
    # クリア
    @staticmethod
    def Clear():
        Logs.__list.clear()
    
    # エラーがあるかどうか
    @staticmethod
    def IsErrors():
        return 0 < len(Logs.__list)
    
    # 出力
    @staticmethod
    def Dump( output_file:io.TextIOWrapper=None ):
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

