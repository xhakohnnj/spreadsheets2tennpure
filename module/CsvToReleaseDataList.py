#
# CSVからリリースデータのリストに変換
#
import csv
from .lib import ReleaseDataListCreaterFromCsv


# ファイルから作成
def FromFile( file_path, date_start_str, date_end_str ):
    f = open(file_path, 'r', encoding="utf_8")
    if f is None:
        return None

    # データ取得
    datas = []
    reader = csv.reader( f )
    for line in reader:
        line.pop(0) # 空白の不要要素削除
        datas.append( line )

    # 頭は非データなので削除
    datas.pop(0)
    datas.pop(0)

    # ファイルはいらなくなったのでクローズ
    f.close()

    return ReleaseDataListCreaterFromCsv.Create( datas, date_start_str, date_end_str ) if datas != None and 0 < len(datas) else None
