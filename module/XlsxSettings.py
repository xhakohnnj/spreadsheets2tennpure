#
# CSVからリリースデータのリストに変換
#
import openpyxl
import datetime
from enum import IntEnum, auto
from . import Error


# 結果
class Result:
    def __init__( self, release_date_start=None, release_date_end=None, gamepass_date_start=None, gamepass_date_end=None, gameevent_date_start=None, gameevent_date_end=None, error_id=Error.eID.NoError ):
        self.release_date_start   = release_date_start    # タイトルリリース日にち(開始)
        self.release_date_end     = release_date_end      # タイトルリリース日にち(終了)
        self.gamepass_date_start  = gamepass_date_start   # ゲームパス日にち(開始)
        self.gamepass_date_end    = gamepass_date_end     # ゲームパス日にち(終了)
        self.gameevent_date_start = gameevent_date_start  # イベント日にち(開始)
        self.gameevent_date_end   = gameevent_date_end    # イベント日にち(終了)
        self.error_id             = error_id              # エラー

# ファイルから作成
def Get( file_path, sheet_name ):
    class eDataID(IntEnum):
        ReleaseDateStart = 0            # タイトルリリース日にち(開始)
        ReleaseDateEnd = auto()         # タイトルリリース日にち(終了)
        GamePassDateStart = auto()      # ゲームパス日にち(終了)
        GamePassDateEnd = auto()        # ゲームパス日にち(終了)
        GameEventDateStart = auto()     # ゲームイベント日にち(終了)
        GameEventDateEnd = auto()       # ゲームイベント日にち(終了)

    wb = openpyxl.load_workbook( file_path )
    if wb is None:
        return None

    sheet = wb[sheet_name]
    if sheet is None:
        return None

    row_base = 4
    row_last = 4
    col_base = 3
    col_last = 8 # ここなんかうまいことできたらいいんだけど.

    datas = []
    if 0 < row_last:
        # セルの値を取得
        cells = sheet.iter_rows( min_row=row_base, max_row=row_last, min_col=col_base, max_col=col_last )

        # 値だけの配列に変換=データ
        def get_value_list(t_2d):
            return ([[cell.value for cell in row] for row in t_2d])
        datas = get_value_list( cells )

    # ファイルはいらなくなったのでクローズ
    wb.close()

    # エラーチェック
    def CheckError():
        ### 廃止予定
        if not isinstance(datas[0][eDataID.ReleaseDateStart],datetime.date):
            return Error.eID.ExportSettings_ReleaseStartDateIsNotDateFormat
        if not isinstance(datas[0][eDataID.ReleaseDateEnd],datetime.date):
            return Error.eID.ExportSettings_ReleaseEndDateIsNotDateFormat
        if not isinstance(datas[0][eDataID.GamePassDateStart],datetime.date):
            return Error.eID.ExportSettings_GamePassStartDateIsNotDateFormat
        if not isinstance(datas[0][eDataID.GamePassDateEnd],datetime.date):
            return Error.eID.ExportSettings_GamePassEndDateIsNotDateFormat
        if not isinstance(datas[0][eDataID.GameEventDateStart],datetime.date):
            return Error.eID.ExportSettings_EventStartDateIsNotDateFormat
        if not isinstance(datas[0][eDataID.GameEventDateEnd],datetime.date):
            return Error.eID.ExportSettings_EventEndDateIsNotDateFormat
        ### 廃止予定
        # 正式
        #if not isinstance(datas[0][eDataID.ReleaseDateStart],str):
        #    return Error.eID.ExportSettings_ReleaseStartDateIsNotStrings
        #if not isinstance(datas[0][eDataID.ReleaseDateEnd],str):
        #    return Error.eID.ExportSettings_ReleaseEndDateIsNotStrings
        #if not isinstance(datas[0][eDataID.GamePassDateStart],str):
        #    return Error.eID.ExportSettings_GamePassStartDateIsNotStrings
        #if not isinstance(datas[0][eDataID.GamePassDateEnd],str):
        #    return Error.eID.ExportSettings_GamePassEndDateIsNotStrings
        #if not isinstance(datas[0][eDataID.GameEventDateStart],str):
        #    return Error.eID.ExportSettings_EventStartDateIsNotStrings
        #if not isinstance(datas[0][eDataID.GameEventDateEnd],str):
        #    return Error.eID.ExportSettings_EventEndDateIsNotStrings
        ######
        return Error.eID.NoError
    error_id = CheckError()

    if error_id is not Error.eID.NoError:
        return Result( error_id=error_id )

    def DateToStr( date ):
        return date.strftime( '%Y/%m/%d' )
    return Result(
        release_date_start=DateToStr( datas[0][eDataID.ReleaseDateStart] )
        , release_date_end=DateToStr( datas[0][eDataID.ReleaseDateEnd] )
        , gameevent_date_start=DateToStr( datas[0][eDataID.GamePassDateStart] )
        , gamepass_date_end=DateToStr( datas[0][eDataID.GamePassDateEnd] )
        , gamepass_date_start=DateToStr( datas[0][eDataID.GameEventDateStart] )
        , gameevent_date_end=DateToStr( datas[0][eDataID.GameEventDateEnd] )
        , error_id=error_id
    )

