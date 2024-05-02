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
from .. import ErrorLog


class Result:
    def __init__( self, release_data_list, error_id=Error.eID.NoError ):
        self.releaseDataList    = release_data_list
        self.errorId            = error_id

# 作成
def Create( sheet_name, items, date_start_str, date_end_str ):
    date_start = Lib.StrToDate( date_start_str )
    date_end = Lib.StrToDate( date_end_str )

    release_data_list = []
    cnt = 0
    for item in items:
        master_data = MasterDatas.ReleaseData( item )
        error_logs = []

        # エラーチェック
        def ErrorCheck( err_condition, error_id, msg ):
            if err_condition:
                error_logs.append( ErrorLog.Log(error_id,msg) )
        def GetExtendInfo(end_newline_del=False):
            ret = ""
            if master_data.titleName is not None: ret += f"タイトル名: {master_data.titleName}\n"
            if end_newline_del: ret = ret.rstrip('\n')
            return ret

        ErrorCheck( master_data.titleName is None, Error.eID.ExportCommon_TitleIsNone, f"「{sheet_name}」シート\n{cnt+1} 番目" )
        ErrorCheck( master_data.date is None, Error.eID.ExportCommon_DateIsNone, f"「{sheet_name}」シート\n{cnt+1} 番目\n{GetExtendInfo(True)}" )
        ErrorCheck( type(master_data.date) is not str, Error.eID.ExportCommon_DateIsNotStrings, f"「{sheet_name}」シート\n{cnt+1} 番目\n{GetExtendInfo(True)}" )
        if master_data.time:
            ErrorCheck( type(master_data.time) is not str, Error.eID.ExportCommon_TimeIsNotStrings, f"「{sheet_name}」シート\n{cnt+1} 番目\n{GetExtendInfo(True)}" )
        if( 0 < len(error_logs) ):
            for error_log in error_logs:
                ErrorLog.Logs.Add( error_log )
            continue

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
    def ToSort( r_data ):
        return r_data.date
    release_data_list.sort( key=ToSort )

    return Result( release_data_list=release_data_list )
