echo off

rem ************************************************************************************************************************
rem XLSX版を実行します.
rem こちらがうまくいかない場合は下方にあるCSV版をお試しください.
rem -----
rem タイトルリリース(開始、終了), ゲームパス(開始、終了), ゲームイベント(開始、終了)
rem py generateTennpureXlsx.py output.txt 2023/10/22 2023/11/22 2023/10/01 2024/12/31 2023/08/01 2023/08/31
rem -----
rem タイトルリリースなどの期間の設定をxlsxファイルの「出力設定」から取得するようになりました。
py generateTennpureXlsx.py output.txt


rem ************************************************************************************************************************
rem CSV版を実行します.
rem -----
rem タイトルリリース(開始、終了), ゲームパス(開始、終了), ゲームイベント(開始、終了)
rem py generateTennpureCsv.py output.txt 2023/08/01 2023/10/31 2023/08/01 2023/12/31 2023/08/01 2023/08/31


pause

