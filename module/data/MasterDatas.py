from enum import IntEnum, auto


# リリースデータ
class ReleaseData:
    def __init__( self, csv_data ):
        class eID(IntEnum):
            ReleaseDate = 0         # リリース日
            ReleaseTime = auto()    # リリース時間
            TitleName   = auto()    # タイトル名
            Supplement  = auto()    # 補足
            UserData1   = auto()    # なんでもデータ.名前が思いつかず適当.
            UserData2   = auto()    # ...
            UserData3   = auto()    # ...

        self.date       = csv_data[eID.ReleaseDate]
        self.time       = csv_data[eID.ReleaseTime]
        self.titleName  = csv_data[eID.TitleName]
        self.supplement = csv_data[eID.Supplement]
        self.userData1  = csv_data[eID.UserData1]
        self.userData2  = csv_data[eID.UserData2]
        self.userData3  = csv_data[eID.UserData3]
