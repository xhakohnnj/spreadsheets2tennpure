from enum import IntEnum, auto


class eID(IntEnum):
    NoError = 0                                                 # なし
    # 出力設定
    ExportSettings_ReleaseStartDateIsNotStrings = auto()        # 出力設定の発売タイトル開始日にちが文字列じゃない
    ExportSettings_ReleaseEndDateIsNotStrings = auto()          # 出力設定の発売タイトル開始日にちが文字列じゃない
    ExportSettings_GamePassStartDateIsNotStrings = auto()       # 出力設定のゲームパス開始日にちが文字列じゃない
    ExportSettings_GamePassEndDateIsNotStrings = auto()         # 出力設定のゲームパス開始日にちが文字列じゃない
    ExportSettings_EventStartDateIsNotStrings = auto()          # 出力設定のイベント開始日にちが文字列じゃない
    ExportSettings_EventEndDateIsNotStrings = auto()            # 出力設定のイベント開始日にちが文字列じゃない
    ### 廃止予定
    ExportSettings_ReleaseStartDateIsNotDateFormat = auto()     # 出力設定の発売タイトル開始日にちの書式が日付じゃない
    ExportSettings_ReleaseEndDateIsNotDateFormat = auto()       # 出力設定の発売タイトル開始日にちの書式が日付じゃない
    ExportSettings_GamePassStartDateIsNotDateFormat = auto()    # 出力設定のゲームパス開始日にちの書式が日付じゃない
    ExportSettings_GamePassEndDateIsNotDateFormat = auto()      # 出力設定のゲームパス開始日にちの書式が日付じゃない
    ExportSettings_EventStartDateIsNotDateFormat = auto()       # 出力設定のイベント開始日にちの書式が日付じゃない
    ExportSettings_EventEndDateIsNotDateFormat = auto()         # 出力設定のイベント開始日にちの書式が日付じゃない
    ###### 廃止予定
    # 出力処理時エラー共通
    ExportCommon_DateIsNone = auto()                            # 日付が未入力
    ExportCommon_TitleIsNone = auto()                           # タイトル名が未入力
    ExportCommon_DateIsNotStrings = auto()                      # 日付が文字列じゃない
    ExportCommon_TimeIsNotStrings = auto()                      # 時刻が文字列じゃない
    # TitleRelease
    TitleRelease_DateIsNone = auto()                            # 日付が未入力
    TitleRelease_TitleIsNone = auto()                           # タイトル名が未入力
    TitleRelease_DateIsNotStrings = auto()                      # 日付が文字列じゃない
    TitleRelease_TimeIsNotStrings = auto()                      # 時刻が文字列じゃない
    # GamePass In
    GamePassIn_DateIsNone = auto()                              # 日付が未入力
    GamePassIn_TitleIsNone = auto()                             # タイトル名が未入力
    GamePassIn_DateIsNotStrings = auto()                        # 日付が文字列じゃない
    GamePassIn_TimeIsNotStrings = auto()                        # 時刻が文字列じゃない
    # GamePass Out
    GamePassOut_DateIsNone = auto()                             # 日付が未入力
    GamePassOut_TitleIsNone = auto()                            # タイトル名が未入力
    GamePassOut_DateIsNotStrings = auto()                       # 日付が文字列じゃない
    GamePassOut_TimeIsNotStrings = auto()                       # 時刻が文字列じゃない
    # Event
    Event_DateIsNone = auto()                                   # 日付が未入力
    Event_TitleIsNone = auto()                                  # タイトル名が未入力
    Event_DateIsNotStrings = auto()                             # 日付が文字列じゃない
    Event_TimeIsNotStrings = auto()                             # 時刻が文字列じゃない

message_table = {
    eID.NoError:"エラーはありません。",
    eID.ExportSettings_ReleaseStartDateIsNotStrings:"「出力設定」シートの「発売タイトル開始日にち」の書式が「書式なしテキスト」ではありません。\n書式を「書式なしテキスト」に設定してください。",
    eID.ExportSettings_ReleaseEndDateIsNotStrings:"「出力設定」シートの「発売タイトル終了日にち」の書式が「書式なしテキスト」ではありません。\n書式を「書式なしテキスト」に設定してください。",
    eID.ExportSettings_GamePassStartDateIsNotStrings:"「出力設定」シートの「ゲームパス開始日にち」の書式が「書式なしテキスト」ではありません。\n書式を「書式なしテキスト」に設定してください。",
    eID.ExportSettings_GamePassEndDateIsNotStrings:"「出力設定」シートの「ゲームパス終了日にち」の書式が「書式なしテキスト」ではありません。\n書式を「書式なしテキスト」に設定してください。",
    eID.ExportSettings_EventStartDateIsNotStrings:"「出力設定」シートの「イベント開始日にち」の書式が「書式なしテキスト」ではありません。\n書式を「書式なしテキスト」に設定してください。",
    eID.ExportSettings_EventEndDateIsNotStrings:"「出力設定」シートの「イベント終了日にち」の書式が「書式なしテキスト」ではありません。\n書式を「書式なしテキスト」に設定してください。",
    eID.ExportSettings_ReleaseStartDateIsNotDateFormat:"「出力設定」シートの「発売タイトル開始日にち」の書式が「日付」ではありません。\n書式を「日付」に設定してください。",
    eID.ExportSettings_ReleaseEndDateIsNotDateFormat:"「出力設定」シートの「発売タイトル終了日にち」の書式が「日付」ではありません。\n書式を「日付」に設定してください。",
    eID.ExportSettings_GamePassStartDateIsNotDateFormat:"「出力設定」シートの「ゲームパス開始日にち」の書式が「日付」ではありません。\n書式を「日付」に設定してください。",
    eID.ExportSettings_GamePassEndDateIsNotDateFormat:"「出力設定」シートの「ゲームパス終了日にち」の書式が「日付」ではありません。\n書式を「日付」に設定してください。",
    eID.ExportSettings_EventStartDateIsNotDateFormat:"「出力設定」シートの「イベント開始日にち」の書式が「日付」ではありません。\n書式を「日付」に設定してください。",
    eID.ExportSettings_EventEndDateIsNotDateFormat:"「出力設定」シートの「イベント終了日にち」の書式が「日付」ではありません。\n書式を「日付」に設定してください。",
    eID.ExportCommon_DateIsNone:"「日付」が未入力のものがあります。\nログを確認して対応してください。",
    eID.ExportCommon_TitleIsNone:"「タイトル名」が未入力のものがあります。\nログを確認して対応してください。",
    eID.ExportCommon_DateIsNotStrings:"「日付」の書式が「書式なしテキスト」ではありません。\nログを確認して対応してください。",
    eID.ExportCommon_TimeIsNotStrings:"「時刻」の書式が「書式なしテキスト」ではありません。\nログを確認して対応してください。",
    eID.TitleRelease_DateIsNone:"「タイトルリリース」シートの「日付」が未入力のものがあります。\nログを確認して対応してください。",
    eID.TitleRelease_TitleIsNone:"「タイトルリリース」シートの「タイトル名」が未入力のものがあります。\nログを確認して対応してください。",
    eID.TitleRelease_DateIsNotStrings:"「タイトルリリース」シートの「日付」の書式が「書式なしテキスト」ではありません。\nログを確認して対応してください。",
    eID.TitleRelease_TimeIsNotStrings:"「タイトルリリース」シートの「時刻」の書式が「書式なしテキスト」ではありません。\nログを確認して対応してください。",
    eID.GamePassIn_DateIsNone:"「ゲームパスIN」シートの「日付」が未入力のものがあります。\nログを確認して対応してください。",
    eID.GamePassIn_TitleIsNone:"「ゲームパスIN」シートの「タイトル名」が未入力のものがあります。\nログを確認して対応してください。",
    eID.GamePassIn_DateIsNotStrings:"「ゲームパスIN」シートの「日付」の書式が「書式なしテキスト」ではありません。\n書式を「書式なしテキスト」に設定してください。",
    eID.GamePassIn_TimeIsNotStrings:"「ゲームパスIN」シートの「時刻」の書式が「書式なしテキスト」ではありません。\n書式を「書式なしテキスト」に設定してください。",
    eID.GamePassOut_DateIsNone:"「ゲームパスOUT」シートの「日付」が未入力のものがあります。\nログを確認して対応してください。",
    eID.GamePassOut_TitleIsNone:"「ゲームパスOUT」シートの「タイトル名」が未入力のものがあります。\nログを確認して対応してください。",
    eID.GamePassOut_DateIsNotStrings:"「ゲームパスOUT」シートの「日付」の書式が「書式なしテキスト」ではありません。\n書式を「書式なしテキスト」に設定してください。",
    eID.GamePassOut_TimeIsNotStrings:"「ゲームパスOUT」シートの「時刻」の書式が「書式なしテキスト」ではありません。\n書式を「書式なしテキスト」に設定してください。",
    eID.Event_DateIsNone:"「ゲームパスIN」シートの「日付」が未入力のものがあります。\nログを確認して対応してください。",
    eID.Event_TitleIsNone:"「ゲームパスIN」シートの「タイトル名」が未入力のものがあります。\nログを確認して対応してください。",
    eID.Event_DateIsNotStrings:"「イベント」シートの「日付」の書式が「書式なしテキスト」ではありません。\n書式を「書式なしテキスト」に設定してください。",
    eID.Event_TimeIsNotStrings:"「イベント」シートの「時刻」の書式が「書式なしテキスト」ではありません。\n書式を「書式なしテキスト」に設定してください。",
}

def toMessage( id ):
    #return "エラー: {0}".format(id)
    return message_table[id]

def IDConvExportCommonToTitleRelease( id ):
    table = {
        eID.ExportCommon_DateIsNone: eID.TitleRelease_DateIsNone,
        eID.ExportCommon_TitleIsNone: eID.TitleRelease_TitleIsNone,
        eID.ExportCommon_DateIsNotStrings: eID.TitleRelease_DateIsNotStrings,
        eID.ExportCommon_TimeIsNotStrings: eID.TitleRelease_TimeIsNotStrings,
    }
    if( id == eID.NoError ):
        return eID.NoError
    return table[id]

def IDConvExportCommonToGamePassIn( id ):
    table = {
        eID.ExportCommon_DateIsNone: eID.GamePassIn_DateIsNone,
        eID.ExportCommon_TitleIsNone: eID.GamePassIn_TitleIsNone,
        eID.ExportCommon_DateIsNotStrings: eID.GamePassIn_DateIsNotStrings,
        eID.ExportCommon_TimeIsNotStrings: eID.GamePassIn_TimeIsNotStrings,
    }
    if( id == eID.NoError ):
        return eID.NoError
    return table[id]

def IDConvExportCommonToGamePassOut( id ):
    table = {
        eID.ExportCommon_DateIsNone: eID.GamePassOut_DateIsNone,
        eID.ExportCommon_TitleIsNone: eID.GamePassOut_TitleIsNone,
        eID.ExportCommon_DateIsNotStrings: eID.GamePassOut_DateIsNotStrings,
        eID.ExportCommon_TimeIsNotStrings: eID.GamePassOut_TimeIsNotStrings,
    }
    if( id == eID.NoError ):
        return eID.NoError
    return table[id]

def IDConvExportCommonToEvent( id ):
    table = {
        eID.ExportCommon_DateIsNone: eID.Event_DateIsNone,
        eID.ExportCommon_TitleIsNone: eID.Event_TitleIsNone,
        eID.ExportCommon_DateIsNotStrings: eID.Event_DateIsNotStrings,
        eID.ExportCommon_TimeIsNotStrings: eID.Event_TimeIsNotStrings,
    }
    if( id == eID.NoError ):
        return eID.NoError
    return table[id]
