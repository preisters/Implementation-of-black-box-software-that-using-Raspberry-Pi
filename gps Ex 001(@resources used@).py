

if strData.startswith('$GPGGA'):
    if self.mDtDateTime is None :
        return False
    try:
        arrFields = strData[:strData.index('*')].strip().split(',')
        self.mStrSentenceType = 'GGA'

        # 시간 : $GPRMC 에서 구한걸로 이용
        strUtcTime = arrFields[1]

        intYear     = self.mDtDateTime.year
        intMonth    = self.mDtDateTime.month
        intDay      = self.mDtDateTime.day
        intHour     = int(strUtcTime[0:2])
        intMinute   = int(strUtcTime[2:4])
        intSecond   = int(strUtcTime[4:6])

        dtGpsDateTime = datetime.datetime(intYear, intMonth, intDay, intHour, intMinute, intSecond)
        self.mDtDateTime = DateUtil.utcToLocal(dtGpsDateTime)

        # 위도
        self.mFltLat = float(self.dmToSd(arrFields[2]) * (1 if arrFields[3] == 'N' else -1))

        # 경도
        self.mFltLon = float(self.dmToSd(arrFields[4]) * (1 if arrFields[5] == 'E' else -1))

        # 품질 (0 : invalid한 데이터, 1 : gps위성신호만으로 계산, 2 : dgps도 사용하여 계산)
        self.mIntPositionFix = int(arrFields[6])

        # 위성
        self.mIntSatelliteCount = int(arrFields[7])

        # 노이즈
        #self.mFltHdop = float(arrFields[8])

        # 고도
        if arrFields[10].upper() == 'M':
            self.mFltAltitude = float(arrFields[9])

    except ValueError:
        return False
