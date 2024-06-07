#
# テンプレ出力メイン
#
import os
from . import TenGenParam
from . import ErrorLog
from .data import TitleData
from .tennpure import TennpureGenerate


def Exec( output_file_name:str, tengen_param:TenGenParam, is_tengen_param_item_from_file:bool ):
    ErrorLog.Logs.Clear()

    # 出力設定
    if is_tengen_param_item_from_file:
        TenGenParam.FromXlsx( body=tengen_param, file_path=tengen_param.srcFileName, sheet_name=tengen_param.outputSettings.sheetName )

    # 出力設定でエラーがあったら出力処理しない
    if not ErrorLog.Logs.IsErrors():
        # 各項目のタイトルリストを作成
        def ToTitleDataList( param:TenGenParam.Item ):
            return TitleData.BodyListFromXlsx( file_path=tengen_param.srcFileName, sheet_name=param.sheetName, date_start_str=param.dateStart, date_end_str=param.dateEnd )
        # タイトルリリース
        title_release_list = ToTitleDataList( param=tengen_param.titleRelease )
        # ゲームパス IN
        gamepass_in_list = ToTitleDataList( param=tengen_param.gamePassIn )
        # ゲームパス OUT
        gamepass_out_list = ToTitleDataList( param=tengen_param.gamePassOut )
        # ゲームイベント
        gameevents_list = ToTitleDataList( param=tengen_param.gameEvents )

        # エラーがあったら出力しない
        if not ErrorLog.Logs.IsErrors():
            # テンプレ出力
            with open( output_file_name, mode='w', encoding='utf-8', newline=os.linesep ) as output_file:
                TennpureGenerate.ToFile(
                    output_file=output_file,
                    title_release_list=title_release_list,
                    gamepass_in_list=gamepass_in_list,
                    gamepass_out_list=gamepass_out_list,
                    gameevents_list=gameevents_list if gameevents_list is not None else None
                )

    if ErrorLog.Logs.IsErrors():
        print("～～～～～～～～～～～～～～～～～～")
        print("入力情報にエラーがあったため出力しませんでした。")
        print("下記に出力されるエラーの内容を確認して修正をお願いします。")
        print("エラーの内容は出力ファイルにも出力しています。")
        print("～～～～～～～～～～～～～～～～～～")
        print("\n")
        with open( output_file_name, mode='w', encoding='utf-8', newline=os.linesep ) as output_file:
            ErrorLog.Logs.Dump( output_file )
