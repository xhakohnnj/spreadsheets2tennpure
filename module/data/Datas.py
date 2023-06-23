# リリースデータ
class ReleaseData:
    def __init__( self, date=None, time=None, titleName=None, supplement=None ):
      self.date = date              # リリース日
      self.time = time              # リリース時間
      self.titleName = titleName    # タイトル名
      self.supplement = supplement  # 補足
