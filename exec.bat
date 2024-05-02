echo off

rem ************************************************************************************************************************
rem テンプレを出力します。
rem py tengen.py ([オプション]出力先ファイル名) ([オプション]期間)
rem 
rem 指定された期間内にあるタイトルで出力先ファイルに出力します。
rem 出力先ファイル名を指定していない場合は output.txt になります。
rem 期間を指定していない場合は xlsx 内の「出力設定」シートから取得します。
rem 
rem オプションの期間は左から下記の内容になります。
rem ・タイトルリリース(開始)
rem ・タイトルリリース(終了)
rem ・ゲームパス(開始)
rem ・ゲームパス(終了)
rem ・ゲームイベント(開始)
rem ・ゲームイベント(終了)
rem 例)
rem py tengen.py output.txt 2023/10/22 2023/11/22 2023/10/01 2024/12/31 2023/08/01 2023/08/31
rem 
rem ************************************************************************************************************************
py tengen.py


pause

