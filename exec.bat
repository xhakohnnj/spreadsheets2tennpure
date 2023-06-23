echo off

rem タイトルリリース(開始、終了), ゲームパス(開始、終了), ゲームイベント(開始、終了)
py generateTennpure.py output.txt 2023/06/01 2023/12/31 2023/06/15 2023/12/31 2023/06/01 2023/12/31
rem py generateTennpureWithFile.py output.txt release.ics gamepass_in.ics gamepass_out.ics 2022/11/22 2023/03/31 2022/11/22 2023/03/31

pause

