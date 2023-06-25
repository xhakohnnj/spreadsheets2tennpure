#
# XLSXからリリースデータのリストに変換
#
from itertools import count
import openpyxl
from .lib import ReleaseDataListCreaterFromCsv
from .lib import Lib


# ファイルから作成
def FromFile( file_path, sheet_name, date_start_str, date_end_str ):
    wb = openpyxl.load_workbook( file_path )
    if wb is None:
        return None

    sheet = wb[sheet_name]
    if sheet is None:
        return None

    row = 3
    col = 1
    row_last = 0
    col_last = 5

    for cnt in count():
        cell = sheet.cell( row=row+cnt, column=col+1 ) # 日付がなければ終了
        if cell.value is None:
            break
        row_last = row+cnt

    cells = sheet.iter_rows( min_row=row, max_row=row_last, min_col=col, max_col=col_last )

    def get_value_list(t_2d):
        return ([[cell.value for cell in row] for row in t_2d])
    lines = get_value_list( cells )

    wb.close()

    datas= []
    line_count = 0
    for line in lines:
        #print( '{0} {1}'.format(sheet_name,line_count) )
        #if 2 <= line_count:
        datas.append( line )
        #print( '{0} {1} {2}'.format(line_count,sheet_name,line) )
        line_count = line_count + 1
    #file_data.close()
    return ReleaseDataListCreaterFromCsv.Create( datas, Lib.StrToDate(date_start_str), Lib.StrToDate(date_end_str) )
