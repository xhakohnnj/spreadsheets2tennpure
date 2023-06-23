#
# テンプレ出力
# 
import sys
from enum import IntEnum, auto
from module import CsvToReleaseDataList
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

# リリースカレンダー
release_list = CsvToReleaseDataList.FromFile( 'タイトルリリース - タイトルリリース.csv', sys.argv[Args.TITLE_RELEASE_DATE_START], sys.argv[Args.TITLE_RELEASE_DATE_END] )
# ゲームパス IN
gamepass_in_list = CsvToReleaseDataList.FromFile( 'タイトルリリース - ゲームパスIN.csv', sys.argv[Args.GAME_PASS_DATE_START], sys.argv[Args.GAME_PASS_DATE_END] )
# ゲームパス OUT
gamepass_out_list = CsvToReleaseDataList.FromFile( 'タイトルリリース - ゲームパスOUT.csv', sys.argv[Args.GAME_PASS_DATE_START], sys.argv[Args.GAME_PASS_DATE_END] )
# ゲームイベント
gameevents_list = CsvToReleaseDataList.FromFile( 'タイトルリリース - イベント.csv', sys.argv[Args.GAME_EVENTS_DATE_START], sys.argv[Args.GAME_EVENTS_DATE_END] )
#######
# csvだと上と同じようにファイルが分割されてしまう。
# csvは一括でDLできないのでエクセルの方がいいかも。
# 処理的にはシートを1つずつ指定して行うので、上のようにデータごとに呼び出しは行うが
# ファイルのDLがめんどくさいのでエクセルの方がいいかも。
#######

with open( sys.argv[Args.OUTPUT_FILE], mode='w', encoding='utf-8', newline='\n' ) as output_file:
    TennpureGenerate.ToFile( output_file, release_list, gamepass_in_list, gamepass_out_list, gameevents_list )

