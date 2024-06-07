#
# 出力パラメータ
#
import openpyxl
from enum import IntEnum, auto
from . import Error
from . import ErrorLog


# 出力パラメータ(本体)
class Body:
    def __init__( self ):
        self.srcFileName        = None                  # 元データのファイル名
        self.outputSettings     = OutputSettingsItem()  # 出力設定項目
        self.titleRelease       = Item()                # タイトルリリース項目パラメータ
        self.gamePassIn         = Item()                # ゲームパスIN項目パラメータ
        self.gamePassOut        = Item()                # ゲームパスOUT項目パラメータ
        self.gameEvents         = Item()                # イベント項目パラメータ

# 項目パラメータ
class Item:
    def __init__( self ):
        self.sheetName   = None     # シート名
        self.dateStart   = None     # 日にち(開始)
        self.dateEnd     = None     # 日にち(終了)

# 出力設定項目
class OutputSettingsItem:
    def __init__( self ):
        self.sheetName  = None      # シート名

# ファイルから取得
def FromXlsx( body:Body, file_path:str, sheet_name:str ):
    class eDataIndex(IntEnum):
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

    csv = [] # 正確にはCSVではないんだけど
    if 0 < row_last:
        # セルの値を取得
        cells = sheet.iter_rows( min_row=row_base, max_row=row_last, min_col=col_base, max_col=col_last )

        # 値だけの配列に変換=データ
        def get_value_list(t_2d):
            return ([[cell.value for cell in row] for row in t_2d])
        csv = get_value_list( cells )

    # ファイルはいらなくなったのでクローズ
    wb.close()

    # エラーチェック
    if not isinstance(csv[0][eDataIndex.ReleaseDateStart],str):
        ErrorLog.Logs.Add( ErrorLog.Log(error_id=Error.eID.ExportSettings_ReleaseStartDateIsNotStrings) )
    if not isinstance(csv[0][eDataIndex.ReleaseDateEnd],str):
        ErrorLog.Logs.Add( ErrorLog.Log(error_id=Error.eID.ExportSettings_ReleaseEndDateIsNotStrings) )
    if not isinstance(csv[0][eDataIndex.GamePassDateStart],str):
        ErrorLog.Logs.Add( ErrorLog.Log(error_id=Error.eID.ExportSettings_GamePassStartDateIsNotStrings) )
    if not isinstance(csv[0][eDataIndex.GamePassDateEnd],str):
        ErrorLog.Logs.Add( ErrorLog.Log(error_id=Error.eID.ExportSettings_GamePassEndDateIsNotStrings) )
    if not isinstance(csv[0][eDataIndex.GameEventDateStart],str):
        ErrorLog.Logs.Add( ErrorLog.Log(error_id=Error.eID.ExportSettings_EventStartDateIsNotStrings) )
    if not isinstance(csv[0][eDataIndex.GameEventDateEnd],str):
        ErrorLog.Logs.Add( ErrorLog.Log(error_id=Error.eID.ExportSettings_EventEndDateIsNotStrings) )

    if ErrorLog.Logs.IsErrors():
        return

    body.titleRelease.dateStart     = csv[0][eDataIndex.ReleaseDateStart]
    body.titleRelease.dateEnd       = csv[0][eDataIndex.ReleaseDateEnd]
    body.gamePassIn.dateStart       = csv[0][eDataIndex.GamePassDateStart]
    body.gamePassIn.dateEnd         = csv[0][eDataIndex.GamePassDateEnd]
    body.gamePassOut.dateStart      = csv[0][eDataIndex.GamePassDateStart]
    body.gamePassOut.dateEnd        = csv[0][eDataIndex.GamePassDateEnd]
    body.gameEvents.dateStart       = csv[0][eDataIndex.GameEventDateStart]
    body.gameEvents.dateEnd         = csv[0][eDataIndex.GameEventDateEnd]
   
