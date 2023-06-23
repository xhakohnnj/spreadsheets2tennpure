#
# iCalendarからリリースデータのリストに変換
#
import csv
from .lib import ReleaseDataListCreaterFromCsv
from .lib import Lib


# ファイルから作成
def FromFile( file_path, date_start_str, date_end_str ):
    file_data = open(file_path, 'r', encoding="utf_8")
    if file_data is None:
        return None

    datas= []
    reader = csv.reader(file_data)
    count = 0
    for line in reader:
        if 2 <= count:
            datas.append( line )
        count = count + 1
    file_data.close()
    return ReleaseDataListCreaterFromCsv.Create( datas, Lib.StrToDate(date_start_str), Lib.StrToDate(date_end_str) )
