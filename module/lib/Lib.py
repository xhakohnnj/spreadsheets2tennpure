#
# ライブラリ
#
from datetime import datetime



# タグ
# 文字列から日付に変換
def StrToDate( str ):
    return datetime.strptime( str.replace('/','-'),'%Y-%m-%d' )


