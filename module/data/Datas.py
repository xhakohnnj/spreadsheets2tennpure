# リリースデータ
class ReleaseData:
    def __init__( self, date=None, time=None, titleName=None, supplement=None, userData1=None, userData2=None, userData3=None ):
      self.date = date              # リリース日
      self.time = time              # リリース時間
      self.titleName = titleName    # タイトル名
      self.supplement = supplement  # 補足
      self.userData1 = userData1    # なんでもデータ 1
      self.userData2 = userData2    # なんでもデータ 2
      self.userData3 = userData3    # なんでもデータ 3
