#
# テンプレ出力
#
import io
from .util import Util


#
# ファイルに出力
#
def ToFile( output_file:io.TextIOWrapper, title_release_list:list, gamepass_in_list:list, gamepass_out_list:list, gameevents_list:list ):
    def WriteFile( str ):
        output_file.write( str + '\n' )
        print( str )

    WriteFile( 'テンプレ 1' )
    WriteFile( '----------' )
    WriteFile( '【Xbox リリース スケジュール】' )
    WriteFile( '' )
    Util.ForeachTitleDataListConvTennpureFormat( title_release_list, False, lambda item: WriteFile( item ) )
    WriteFile( '' )
    WriteFile( '' )
    WriteFile( '' )
    WriteFile( 'テンプレ 2' )
    WriteFile( '----------' )
    WriteFile( '【XBOXゲームスペシャル】' )
    WriteFile( 'ttps://www.microsoft.com/ja-jp/store/deals/games/xbox' )
    WriteFile( '' )
    WriteFile( '【ゲームパス & EAPlay】' )
    WriteFile( '≪IN≫' )
    Util.ForeachTitleDataListConvTennpureFormat( gamepass_in_list, False, lambda item: WriteFile( item ) )
    WriteFile( '' )
    WriteFile( '≪OUT≫' )
    Util.ForeachTitleDataListConvTennpureFormat( gamepass_out_list, False, lambda item: WriteFile( item ) )
    if gameevents_list is not None and 0 < len(gameevents_list):
        WriteFile( '' )
        WriteFile( '【イベント】' )
        Util.ForeachTitleDataListConvTennpureFormat( gameevents_list, True, lambda item: WriteFile( item ) )
        WriteFile( '' )
        WriteFile( '' )
        WriteFile( '' )
        WriteFile( '↓↓↓テンプレとは別で配信のURLどこ～？って時に使ってもらえれば↓↓↓' )
        Util.ForeachTitleDataListConvEvent( gameevents_list, True, lambda item: WriteFile( item ) )

