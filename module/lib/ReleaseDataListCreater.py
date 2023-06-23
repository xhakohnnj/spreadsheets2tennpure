#
# リリースデータリスト作成
#
from enum import IntEnum, auto
from datetime import datetime
from datetime import timedelta
from ..lib import iCalLib
from .. import Datas


# 作成
def Create( ical_lines, date_start, date_end ):
    # データの配列のインデックス
    class eDataSourceIndex(IntEnum):
        Date      = 0 # 最初のauto()は1になるとのことで。
        Name      = auto()
        Options   = auto()
        UseTime   = auto()

    # 元データ(iCalを解析して整えたデータ)を作成
    data_sources = []
    data_source = None # あまり凝らずにとりあえず配列で.
    for item in ical_lines:
      if iCalLib.HasTag(item,iCalLib.eTag.Begin):
        data_source = [None,None,None,None] # eDataIndexと合わせる
      elif iCalLib.HasTag(item,iCalLib.eTag.End):
        data_sources.append( data_source )
        data_source = None
      elif iCalLib.HasTag(item,iCalLib.eTag.DateStart):
        date_start_value = iCalLib.GetTagValue(item)
        if -1 < date_start_value.find('T'):
          data_source[eDataSourceIndex.UseTime] = True
          # GoogleカレンダーのiCalで取得できる時刻が協定世界時(UTC)なので日本標準時(JST)に変換する。
          # 単純にUTCとJSTの時間差 9時間 を足す。
          data_source[eDataSourceIndex.Date] = datetime.strptime( date_start_value, '%Y%m%dT%H%M%SZ' ) + timedelta(hours=9)
        else:
          data_source[eDataSourceIndex.UseTime] = False
          data_source[eDataSourceIndex.Date] = datetime.strptime( date_start_value, '%Y%m%d' )
      elif iCalLib.HasTag(item,iCalLib.eTag.Summary):
        data_source[eDataSourceIndex.Name] = iCalLib.GetTagValue( item )
      elif iCalLib.HasTag(item,iCalLib.eTag.Description):
        data_source[eDataSourceIndex.Options] = iCalLib.GetTagValue( item )
  
    # iCalに登録されてるのが日付順じゃないのでソートする.
    data_sources.sort()

    release_title_data_list = []
    for data_source in data_sources:
      # 日付の範囲
      if not date_start <= data_source[eDataSourceIndex.Date] <= date_end:
        continue

      release_title_data_list.append(
        Datas.ReleaseData(
          data_source[eDataSourceIndex.Date]
          , data_source[eDataSourceIndex.Name]
          , data_source[eDataSourceIndex.Options]
          , data_source[eDataSourceIndex.UseTime]
        )
      )

    return release_title_data_list
