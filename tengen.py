#
# テンプレ出力
# 
import sys
from enum import IntEnum, auto
from TenGen import TenGenParam
from TenGen import TenGenMain


# 定数
IN_FILE_NAME = 'Xboxタイトルリリース.xlsx'
OUT_FILE_NAME = 'output.txt'

SHEET_NAME_TITLE_RELEASE = 'タイトルリリース'
SHEET_NAME_GAME_PASS_IN = 'ゲームパスIN'
SHEET_NAME_GAME_PASS_OUT = 'ゲームパスOUT'
SHEET_NAME_GAME_EVENTS = 'イベント'
SHEET_NAME_OUTPUT_SETTINGS = '出力設定'

# 引数
class eArgs(IntEnum):
    OouputFileName          = 1         # 出力ファイル名
    TitleReleaseDateStart   = auto()    # 発売タイトルの日付の範囲(開始)
    TitleReleaseDateEnd     = auto()    # 発売タイトルの日付の範囲(終了)
    GamePassDateStart       = auto()    # ゲームパスの日付の範囲(開始)
    GamePassDateEnd         = auto()    # ゲームパスの日付の範囲(終了)
    GameEventsDateStart     = auto()    # ゲームイベントの日付の範囲(開始)
    GameEventsDateEnd       = auto()    # ゲームイベントの日付の範囲(終了)
    Num                     = auto()    # 最大数

out_file_name = OUT_FILE_NAME
is_gen_param_item_from_file = True # パラメータのうち、発売タイトルなど各項目のものはファイルから取得する

tengen_param = TenGenParam.Body()
tengen_param.srcFileName = IN_FILE_NAME
tengen_param.outputSettings.sheetName  = SHEET_NAME_OUTPUT_SETTINGS
tengen_param.titleRelease.sheetName    = SHEET_NAME_TITLE_RELEASE
tengen_param.gamePassIn.sheetName      = SHEET_NAME_GAME_PASS_IN
tengen_param.gamePassOut.sheetName     = SHEET_NAME_GAME_PASS_OUT
tengen_param.gameEvents.sheetName      = SHEET_NAME_GAME_EVENTS

if len(sys.argv) == eArgs.Num:
    is_gen_param_item_from_file = False
    out_file_name                          = sys.argv[eArgs.OouputFileName]
    tengen_param.titleRelease.dateStart    = sys.argv[eArgs.TitleReleaseDateStart]
    tengen_param.titleRelease.dateEnd      = sys.argv[eArgs.TitleReleaseDateEnd]
    tengen_param.gamePassIn.dateStart      = sys.argv[eArgs.GamePassDateStart]
    tengen_param.gamePassIn.dateEnd        = sys.argv[eArgs.GamePassDateEnd]
    tengen_param.gamePassOut.dateStart     = sys.argv[eArgs.GamePassDateStart]
    tengen_param.gamePassOut.dateEnd       = sys.argv[eArgs.GamePassDateEnd]
    tengen_param.gameEvents.dateStart      = sys.argv[eArgs.GameEventsDateStart]
    tengen_param.gameEvents.dateEnd        = sys.argv[eArgs.GameEventsDateEnd]
elif len(sys.argv) == eArgs.OouputFileName+1: # 判定雑いけどファイル名のみ
    out_file_name = sys.argv[eArgs.OouputFileName]

TenGenMain.Exec( output_file_name=out_file_name, tengen_param=tengen_param, is_tengen_param_item_from_file=is_gen_param_item_from_file )
