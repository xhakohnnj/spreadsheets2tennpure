#
# iCalendar関連ライブラリ
#
from enum import Enum

# タグ
class eTag(Enum):
    Begin       = "BEGIN:VEVENT"    # 予定情報開始
    End         = "END:VEVENT"      # 予定情報終了
    DateStart   = "DTSTART"         # 開始日
    DateEnd     = "DTEND"           # 終了日
    Summary     = "SUMMARY"         # 予定タイトル
    Description = "DESCRIPTION"     # 説明欄


#
# タグがあるかどうか
#
def HasTag( str, tag ):
    return -1 < str.find(tag.value)

#
# タグの値を取得
#
def GetTagValue( str ):
    return str.split(":",1)[-1]


