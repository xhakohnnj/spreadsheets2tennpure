#
# リリースデータリストから出力
#
from .lib import Lib


#
# ファイルに出力
#
def ToFile( output_file, release_list, gamepass_in_list, gamepass_out_list, gameevents_list ):
    def WriteFile( str ):
        output_file.write( str + '\n' )
        print( str )

    WriteFile( 'テンプレ 1' )
    WriteFile( '----------' )
    WriteFile( '【Xbox リリース スケジュール】' )
    WriteFile( '' )
    Lib.ForeachReleaseDataListConvTennpureFormat( release_list, False, lambda item: WriteFile( item ) )
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
    Lib.ForeachReleaseDataListConvTennpureFormat( gamepass_in_list, False, lambda item: WriteFile( item ) )
    WriteFile( '' )
    WriteFile( '≪OUT≫' )
    Lib.ForeachReleaseDataListConvTennpureFormat( gamepass_out_list, False, lambda item: WriteFile( item ) )
    if gameevents_list is not None and 0 < len(gameevents_list):
        WriteFile( '' )
        WriteFile( '【イベント】' )
        Lib.ForeachReleaseDataListConvTennpureFormat( gameevents_list, True, lambda item: WriteFile( item ) )
