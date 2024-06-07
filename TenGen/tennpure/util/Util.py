#
# テンプレ出力関係のユーティリティ
#
from datetime import timedelta


#
# データリストをテンプレのフォーマットに変換して各アイテムごとにコールバックを呼び出す.
#
# date_list     データリスト
# is_use_time   時間も使用するかどうか
# func          データ1つに行う処理
#
def ForeachTitleDataListConvTennpureFormat( data_list:list, is_use_time:bool, func, *args ):
    year_tmp = None
    output_year = False
    insert_newline = False

    for data in data_list:
        if year_tmp is None:
            year_tmp = data.date.year

        # 年をまたいだら年も出力する.
        if year_tmp is None or not year_tmp is None and year_tmp != data.date.year:
            year_tmp = data.date.year
            output_year = True
            insert_newline = True

        date_format = '%m/%d'
        date = data.date
        if data.time is not None:
            date = date + timedelta( hours=data.time.hour, minutes=data.time.minute )
        if output_year is True:
            date_format = '%Y/{0}'.format( date_format )
        if is_use_time is True:
            date_format = '{0} %H:%M'.format( date_format )
        date_str = date.strftime( date_format )

        item = '{0}　{1}'.format( date_str, data.titleName )
        if data.supplement:
            item = '{0}　←{1}'.format( item , data.supplement )

        # 改行を頭に.
        if insert_newline is True:
            item = '\n' + item
            insert_newline = False

        func( item )

def ForeachTitleDataListConvEvent( data_list:list, is_use_time:bool, func, *args ):
    # ～TennpureFormatでやってる「年をまたいだら～」なところは未対応。めんどくさい。
    for data in data_list:
        date_format = '%m/%d'
        date = data.date
        if data.time is not None:
            date = date + timedelta( hours=data.time.hour, minutes=data.time.minute )
        if is_use_time is True:
            date_format = '{0} %H:%M'.format( date_format )
        date_str = date.strftime( date_format )

        item = '■ [{0}　{1}]'.format( date_str, data.titleName )
        # 配信URL
        if data.userData1:
            item = '{0}\n{1}'.format( item , data.userData1 )

        func( item )
