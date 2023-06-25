#
# リリースデータリスト作成
#
from enum import IntEnum, auto
from datetime import datetime
from datetime import timedelta
from ..lib import iCalLib
from ..lib import Lib
from ..data import Datas


# ただの配列を処理してるだけだからCsvって名前に付けるべきじゃなかったな。

# 作成
def Create( items, date_start_str, date_end_str ):
    class eDataID(IntEnum):
        ReleaseDate = 0         # リリース日
        ReleaseTime = auto()    # リリース時間
        TitleName   = auto()    # タイトル名
        Supplement  = auto()    # 補足

    # データの配列のインデックス
    class eDataSourceIndex(IntEnum):
        Date        = 0 # 最初のauto()は1になるとのことで。
        Time        = auto()
        Name        = auto()
        Supplement  = auto()

    date_start = Lib.StrToDate( date_start_str )
    date_end = Lib.StrToDate( date_end_str )

    # 元データ(iCalを解析して整えたデータ)を作成
    data_sources = []
    cnt = 0
    for item in items:
        data_source = [None,None,None,None] # eDataIndexと合わせる.クラスを挟めばいいんだけど、そこまでやる手間も必須ではないかな.
        data_source[eDataSourceIndex.Date] = datetime.strptime( item[eDataID.ReleaseDate], '%Y/%m/%d' )
        if item[eDataID.ReleaseTime]:
            data_source[eDataSourceIndex.Time] = datetime.strptime( item[eDataID.ReleaseTime], '%H:%M' )
        data_source[eDataSourceIndex.Name] = item[eDataID.TitleName]
        data_source[eDataSourceIndex.Supplement] = item[eDataID.Supplement]
        data_sources.append( data_source )
        cnt = cnt + 1

    # 日付順でソートしておく.
    data_sources.sort()

    release_data_list = []
    for data_source in data_sources:
        # 日付の範囲
        if not date_start <= data_source[eDataSourceIndex.Date] <= date_end:
            continue

        release_data_list.append(
            Datas.ReleaseData(
                data_source[eDataSourceIndex.Date]
                , data_source[eDataSourceIndex.Time]
                , data_source[eDataSourceIndex.Name]
                , data_source[eDataSourceIndex.Supplement]
            )
        )

    return release_data_list
