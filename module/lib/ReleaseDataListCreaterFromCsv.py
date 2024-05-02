#
# リリースデータリスト作成
#
# ただの配列を処理してるだけだからCsvって名前に付けるべきじゃなかったな。
#
from datetime import datetime
from ..lib import Lib
from ..data import MasterDatas
from ..data import Datas
from .. import Error


class Result:
    def __init__( self, release_data_list, error_id=Error.eID.NoError ):
        self.releaseDataList    = release_data_list
        self.errorId            = error_id

# 作成
def Create( items, date_start_str, date_end_str ):
    date_start = Lib.StrToDate( date_start_str )
    date_end = Lib.StrToDate( date_end_str )

    error_id = Error.eID.NoError
    release_data_list = []
    cnt = 0
    for item in items:
        master_data = MasterDatas.ReleaseData( item )

        # エラーチェック
        def ErrorCheck( err_condition, msg ):
            if err_condition:
                print( "<<ERROR>>" )
                print( msg )
                print( "<<<<<<<<<<" )
                return True
            return False
        if ErrorCheck( master_data.titleName is None, f"{cnt+1}番目のタイトル名が未入力です。" ):
            error_id = Error.eID.ExportCommon_TitleIsNone
            break
        if ErrorCheck( master_data.date is None, f"{cnt+1}番目の日付が未入力です。\nタイトル名={master_data.titleName}" ):
            error_id = Error.eID.ExportCommon_DateIsNone
            break
        if ErrorCheck( type(master_data.date) is not str, f"{cnt+1}番目の日付が文字列ではありません！\n「書式なしテキスト」に設定してください。\nタイトル名={master_data.titleName}" ):
            error_id = Error.eID.ExportCommon_DateIsNotStrings
            break
        if master_data.time and ErrorCheck( type(master_data.time) is not str, f"{cnt+1}番目の時刻が文字列ではありません！\n「書式なしテキスト」に設定してください。\nタイトル名={master_data.titleName}" ):
            error_id = Error.eID.ExportCommon_TimeIsNotStrings
            break

        release_date = Lib.StrToDate( master_data.date )

        # 日付の範囲
        if date_start <= release_date <= date_end:
            release_data = Datas.ReleaseData()
            release_data.date = datetime.strptime( master_data.date, '%Y/%m/%d' )
            release_data.time = datetime.strptime( master_data.time, '%H:%M' ) if master_data.time is not None else None
            release_data.titleName = master_data.titleName
            release_data.supplement = master_data.supplement
            release_data.userData1 = master_data.userData1
            release_data.userData2 = master_data.userData2
            release_data.userData3 = master_data.userData3

            release_data_list.append( release_data )

        cnt = cnt + 1

    # 日付順でソート.
    #release_data_list.sort()

    return Result( release_data_list=release_data_list, error_id=error_id )
