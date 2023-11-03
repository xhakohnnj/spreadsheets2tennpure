#
# テンプレ出力(XLSX版)
# 
import sys
import os
from enum import IntEnum, auto
from module import XlsxSettings
from module import XlsxToReleaseDataList
from module.tennpure import TennpureGenerate


# 引数
class Args(IntEnum):
    OUTPUT_FILE     = 1                     # 出力ファイル
    TITLE_RELEASE_DATE_START    = auto()    # 発売タイトルの日付の範囲(開始)
    TITLE_RELEASE_DATE_END      = auto()    # 発売タイトルの日付の範囲(終了)
    GAME_PASS_DATE_START        = auto()    # ゲームパスの日付の範囲(開始)
    GAME_PASS_DATE_END          = auto()    # ゲームパスの日付の範囲(終了)
    GAME_EVENTS_DATE_START      = auto()    # ゲームイベントの日付の範囲(開始)
    GAME_EVENTS_DATE_END        = auto()    # ゲームイベントの日付の範囲(終了)

settings = None
if len(sys.argv) == 2: # 雑いけど引数が出力ファイルのみだった場合
    settings = XlsxSettings.Get( 'Xboxタイトルリリース.xlsx', '出力設定' )
else:
    settings = XlsxSettings.Settings(
        sys.argv[Args.TITLE_RELEASE_DATE_START]
        , sys.argv[Args.TITLE_RELEASE_DATE_END]
        , sys.argv[Args.GAME_PASS_DATE_START]
        , sys.argv[Args.GAME_PASS_DATE_END]
        , sys.argv[Args.GAME_EVENTS_DATE_START]
        , sys.argv[Args.GAME_EVENTS_DATE_END]
    )




# リリースカレンダー
release_list = XlsxToReleaseDataList.FromFile( 'Xboxタイトルリリース.xlsx', 'タイトルリリース', settings.release_date_start, settings.release_date_end )
# ゲームパス IN
gamepass_in_list = XlsxToReleaseDataList.FromFile( 'Xboxタイトルリリース.xlsx', 'ゲームパスIN', settings.gamepass_date_start, settings.gamepass_date_end )
# ゲームパス OUT
gamepass_out_list = XlsxToReleaseDataList.FromFile( 'Xboxタイトルリリース.xlsx', 'ゲームパスOUT', settings.gamepass_date_start, settings.gamepass_date_end )
# ゲームイベント
gameevents_list = XlsxToReleaseDataList.FromFile( 'Xboxタイトルリリース.xlsx', 'イベント', settings.gameevent_date_start, settings.gameevent_date_end )

with open( sys.argv[Args.OUTPUT_FILE], mode='w', encoding='utf-8', newline=os.linesep ) as output_file:
    TennpureGenerate.ToFile( output_file, release_list, gamepass_in_list, gamepass_out_list, gameevents_list )

