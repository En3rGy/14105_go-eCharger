# coding: UTF-8
import httplib
import json
import threading

##!!!!##################################################################################################
#### Own written code can be placed above this commentblock . Do not change or delete commentblock! ####
########################################################################################################
##** Code created by generator - DO NOT CHANGE! **##

class Go_eCharger_14105_14105(hsl20_3.BaseModule):

    def __init__(self, homeserver_context):
        hsl20_3.BaseModule.__init__(self, homeserver_context, "hsl20_3_go_eCharger")
        self.FRAMEWORK = self._get_framework()
        self.LOGGER = self._get_logger(hsl20_3.LOGGING_NONE,())
        self.PIN_I_S_IP=1
        self.PIN_I_N_PORT=2
        self.PIN_I_N_INTERVAL=3
        self.PIN_I_N_TRIGGER=4
        self.PIN_I_N_AMP=5
        self.PIN_I_N_AST=6
        self.PIN_I_N_ALW=7
        self.PIN_I_N_STP=8
        self.PIN_I_N_DWO=9
        self.PIN_I_S_WSS=10
        self.PIN_I_S_WKE=11
        self.PIN_I_N_WEN=12
        self.PIN_I_N_TOF=13
        self.PIN_I_N_TDS=14
        self.PIN_I_N_LBR=15
        self.PIN_I_N_AHO=16
        self.PIN_I_N_AFO=17
        self.PIN_I_N_AL1=18
        self.PIN_I_N_AL2=19
        self.PIN_I_N_AL3=20
        self.PIN_I_N_AL4=21
        self.PIN_I_N_AL5=22
        self.PIN_I_N_CID=23
        self.PIN_I_N_CCH=24
        self.PIN_I_N_CFI=25
        self.PIN_I_N_LSE=26
        self.PIN_I_N_UST=27
        self.PIN_I_S_WAK=28
        self.PIN_I_N_R1X=29
        self.PIN_I_N_DTO=30
        self.PIN_I_N_NMO=31
        self.PIN_I_S_RNA=32
        self.PIN_I_S_RNM=33
        self.PIN_I_S_RNE=34
        self.PIN_I_S_RN1=35
        self.PIN_I_S_RN4=36
        self.PIN_I_S_RN5=37
        self.PIN_I_S_RN6=38
        self.PIN_I_S_RN7=39
        self.PIN_I_S_RN8=40
        self.PIN_I_S_RN9=41
        self.PIN_I_N_AZO=42
        self.PIN_I_N_AMA=43
        self.PIN_O_N_ONLINE=1
        self.PIN_O_S_VERSION=2
        self.PIN_O_N_RBC=3
        self.PIN_O_N_RBT=4
        self.PIN_O_N_CAR=5
        self.PIN_O_N_ERR=6
        self.PIN_O_N_CBL=7
        self.PIN_O_N_PHA=8
        self.PIN_O_N_TMP=9
        self.PIN_O_N_DWS=10
        self.PIN_O_N_ADI=11
        self.PIN_O_N_UBY=12
        self.PIN_O_N_ETO=13
        self.PIN_O_N_WST=14
        self.PIN_O_N_NRG_CURR=15
        self.PIN_O_S_FWV=16
        self.PIN_O_S_SSE=17
        self.PIN_O_N_ECA=18
        self.PIN_O_N_ECR=19
        self.PIN_O_N_ECD=20
        self.PIN_O_N_EC4=21
        self.PIN_O_N_EC5=22
        self.PIN_O_N_EC6=23
        self.PIN_O_N_EC7=24
        self.PIN_O_N_EC8=25
        self.PIN_O_N_EC9=26
        self.PIN_O_N_EC1=27
        self.PIN_O_S_RCA=28
        self.PIN_O_S_RCR=29
        self.PIN_O_S_RCD=30
        self.PIN_O_S_RC4=31
        self.PIN_O_S_RC5=32
        self.PIN_O_S_RC6=33
        self.PIN_O_S_RC7=34
        self.PIN_O_S_RC8=35
        self.PIN_O_S_RC9=36
        self.PIN_O_S_RC1=37
        self.PIN_O_S_TME=38
        self.PIN_O_N_AMP=39
        self.PIN_O_N_AST=40
        self.PIN_O_N_ALW=41
        self.PIN_O_N_STP=42
        self.PIN_O_N_DWO=43
        self.PIN_O_S_WSS=44
        self.PIN_O_S_WKE=45
        self.PIN_O_N_WEN=46
        self.PIN_O_N_TOF=47
        self.PIN_O_N_TDS=48
        self.PIN_O_N_LBR=49
        self.PIN_O_N_AHO=50
        self.PIN_O_N_AFI=51
        self.PIN_O_N_AL1=52
        self.PIN_O_N_AL2=53
        self.PIN_O_N_AL3=54
        self.PIN_O_N_AL4=55
        self.PIN_O_N_AL5=56
        self.PIN_O_N_CID=57
        self.PIN_O_N_CCH=58
        self.PIN_O_N_CFI=59
        self.PIN_O_N_LSE=60
        self.PIN_O_N_UST=61
        self.PIN_O_S_WAK=62
        self.PIN_O_N_R1X=63
        self.PIN_O_N_DTO=64
        self.PIN_O_N_NMO=65
        self.PIN_O_S_RNA=66
        self.PIN_O_S_RNM=67
        self.PIN_O_S_RNE=68
        self.PIN_O_S_RN1=69
        self.PIN_O_S_RN4=70
        self.PIN_O_S_RN5=71
        self.PIN_O_S_RN6=72
        self.PIN_O_S_RN7=73
        self.PIN_O_S_RN8=74
        self.PIN_O_S_RN9=75
        self.PIN_O_N_AZO=76
        self.PIN_O_N_AMA=77
        self.PIN_O_N_UPD=78
        self.FRAMEWORK._run_in_context_thread(self.on_init)

########################################################################################################
#### Own written code can be placed after this commentblock . Do not change or delete commentblock! ####
###################################################################################################!!!##

    m_index2key = {}

    def getData(self):
        api_url = str(self._get_input_value(self.PIN_I_S_IP))
        api_port = int(self._get_input_value(self.PIN_I_N_PORT))
        nInterval = self._get_input_value(self.PIN_I_N_INTERVAL)

        api_path = '/status'
        data = {}

        try:
            httpClient = httplib.HTTPConnection(api_url, int(api_port), timeout=5)
            httpClient.request("GET", api_path)
            response = httpClient.getresponse()
            status = response.status
            data = {'data': response.read(), 'status': status}
            self.DEBUG.add_message("14105: http response code: " + str(status))
        except Exception as e:
            self.DEBUG.add_message("14105: " + str(e))
        finally:
            if httpClient:
                httpClient.close()

        if 'data' in data:
            self.readJson(data['data'])
            self._set_output_value(self.PIN_O_N_ONLINE, 1)

        else:
            self.DEBUG.add_message("14105: Could not receive data")
            self._set_output_value(self.PIN_O_N_ONLINE, 0)

        if (nInterval > 0):
            t = threading.Timer(nInterval, self.getData).start()

    # read light data from json
    def readJson(self, jsonState):
        try:
            jsonState = json.loads(jsonState)

            if 'version' in jsonState:
                sVer = jsonState['version']
                self._set_output_value(self.PIN_O_S_VERSION, str(sVer))
            if 'rbc' in jsonState:
                nRBC = jsonState['rbc']
                self._set_output_value(self.PIN_O_N_RBC, int(nRBC))
            if 'rbt' in jsonState:
                nRBT = int(jsonState['rbt']) / 1000
                self._set_output_value(self.PIN_O_N_RBT, int(nRBT))
            if 'car' in jsonState:
                nCar = jsonState['car']
                self._set_output_value(self.PIN_O_N_CAR, int(nCar))
            if 'car' in jsonState:
                nCar = jsonState['car']
                self._set_output_value(self.PIN_O_N_CAR, int(nCar))
            if 'err' in jsonState:
                nErr = jsonState['err']
                self._set_output_value(self.PIN_O_N_ERR, int(nErr))
            if 'cbl' in jsonState:
                nCBL = jsonState['cbl']
                self._set_output_value(self.PIN_O_N_CBL, int(nCBL))
            if 'pha' in jsonState:
                nPHA = jsonState['pha']
                self._set_output_value(self.PIN_O_N_PHA, int(nPHA))
            if 'tmp' in jsonState:
                nTMP = jsonState['tmp']
                self._set_output_value(self.PIN_O_N_TMP, int(nTMP))
            if 'dws' in jsonState:
                nDWS = int(jsonState['dws']) / 360000.0
                self._set_output_value(self.PIN_O_N_DWS, float(nDWS))
            if 'adi' in jsonState:
                nADI = jsonState['adi']
                self._set_output_value(self.PIN_O_N_ADI, int(nADI))
            if 'uby' in jsonState:
                nUBY = jsonState['uby']
                self._set_output_value(self.PIN_O_N_UBY, int(nUBY))
            if 'eto' in jsonState:
                nETO = int(jsonState['eto']) / 10.0
                self._set_output_value(self.PIN_O_N_ETO, float(nETO))
            if 'wst' in jsonState:
                nWST = jsonState['wst']
                self._set_output_value(self.PIN_O_N_WST, int(nWST))

            # nrg[0]: Spannung auf L1 in volts
            # nrg[1]: Spannung auf L2 in volts
            # nrg[2]: Spannung auf L3 in volts
            # nrg[3]: Spannung auf N in volts
            # nrg[4]: Ampere auf L1 in 0.1 A(123 entspricht 12.3 A)
            # nrg[5]: Ampere auf L2 in 0.1 A
            # nrg[6]: Ampere auf L3 in 0.1 A
            # nrg[7]: Leistung auf L1 in 0.1 kW(36 entspricht 3.6 kW)
            # nrg[8]: Leistung auf L2 in 0.1 kW
            # nrg[9]: Leistung auf L3 in 0.1 kW
            # nrg[10]: Leistung auf N in 0.1 kW
            # nrg[11]: Leistung gesamt 0.01 kW(360 entspricht 3.6 kW)
            # nrg[12]: Leistungsfaktor auf L1 in %
            # nrg[13]: Leistungsfaktor auf L2 in %
            # nrg[14]: Leistungsfaktor auf L3 in %
            # nrg[15]: Leistungsfaktor auf N in %
            if 'nrg' in jsonState:
                nrg = jsonState['nrg']
                nrg_curr = (int(nrg[4]) + int(nrg[5]) + int(nrg[6])) / 10
                self._set_output_value(self.PIN_O_N_NRG_CURR, nrg_curr)
            if 'fwv' in jsonState:
                sFWV = jsonState['fwv']
                self._set_output_value(self.PIN_O_S_FWV, str(sFWV))
            if 'sse' in jsonState:
                sSSE = jsonState['sse']
                self._set_output_value(self.PIN_O_S_SSE, int(sSSE))
            if 'eca' in jsonState:
                nECA = int(jsonState['eca']) / 10.0
                self._set_output_value(self.PIN_O_N_ECA, float(nECA))
            if 'ecr' in jsonState:
                nECR = int(jsonState['ecr']) / 10.0
                self._set_output_value(self.PIN_O_N_ECR, float(nECR))
            if 'ecd' in jsonState:
                nECD = int(jsonState['ecd']) / 10.0
                self._set_output_value(self.PIN_O_N_ECD, float(nECD))
            if 'ec4' in jsonState:
                nEC4 = int(jsonState['ec4']) / 10.0
                self._set_output_value(self.PIN_O_N_EC4, float(nEC4))
            if 'ec5' in jsonState:
                nEC5 = int(jsonState['ec5']) / 10.0
                self._set_output_value(self.PIN_O_N_EC5, float(nEC5))
            if 'ec6' in jsonState:
                nEC6 = int(jsonState['ec6']) / 10.0
                self._set_output_value(self.PIN_O_N_EC6, float(nEC6))
            if 'ec7' in jsonState:
                nEC7 = int(jsonState['ec7']) / 10.0
                self._set_output_value(self.PIN_O_N_EC7, float(nEC7))
            if 'ec8' in jsonState:
                nEC8 = int(jsonState['ec8']) / 10.0
                self._set_output_value(self.PIN_O_N_EC8, float(nEC8))
            if 'ec9' in jsonState:
                nEC9 = int(jsonState['ec9']) / 10.0
                self._set_output_value(self.PIN_O_N_EC9, float(nEC9))
            if 'ec1' in jsonState:
                nEC1 = int(jsonState['ec1']) / 10.0
                self._set_output_value(self.PIN_O_N_EC1, float(nEC1))
            if 'rca' in jsonState:
                sRCA = jsonState['rca']
                self._set_output_value(self.PIN_O_S_RCA, str(sRCA))
            if 'rcr' in jsonState:
                sRCR = jsonState['rcr']
                self._set_output_value(self.PIN_O_S_RCR, str(sRCR))
            if 'rcd' in jsonState:
                sRCD = jsonState['rcd']
                self._set_output_value(self.PIN_O_S_RCD, str(sRCD))
            if 'rc4' in jsonState:
                sRC4 = jsonState['rc4']
                self._set_output_value(self.PIN_O_S_RC4, str(sRC4))
            if 'rc5' in jsonState:
                sRC5 = jsonState['rc5']
                self._set_output_value(self.PIN_O_S_RC5, str(sRC5))
            if 'rc6' in jsonState:
                sRC6 = jsonState['rc6']
                self._set_output_value(self.PIN_O_S_RC6, str(sRC6))
            if 'rc7' in jsonState:
                sRC7 = jsonState['rc7']
                self._set_output_value(self.PIN_O_S_RC7, str(sRC7))
            if 'rc8' in jsonState:
                sRC8 = jsonState['rc8']
                self._set_output_value(self.PIN_O_S_RC8, str(sRC8))
            if 'rc9' in jsonState:
                sRC9 = jsonState['rc9']
                self._set_output_value(self.PIN_O_S_RC9, str(sRC9))
            if 'rc1' in jsonState:
                sRC1 = jsonState['rc1']
                self._set_output_value(self.PIN_O_S_RC1, str(sRC1))
            if 'tme' in jsonState:
                sTME = jsonState['tme']
                # ddmmyyhhmi -> dd.mm.yyyy hh:mi
                if (len(sTME) == 10):
                    sTME = sTME[0:1] + '.' + sTME[2:3] + sTME[4:5] + ' ' + sTME[6:7] + ":" + sTME[8:9]
                self._set_output_value(self.PIN_O_S_TME, str(sTME))
            if 'amp' in jsonState:
                nAMP = jsonState['amp']
                self._set_output_value(self.PIN_O_N_AMP, int(nAMP))
            if 'ast' in jsonState:
                nAST = jsonState['ast']
                self._set_output_value(self.PIN_O_N_AST, int(nAST))
            if 'alw' in jsonState:
                nALW = jsonState['alw']
                self._set_output_value(self.PIN_O_N_ALW, int(nALW))
            if 'stp' in jsonState:
                nSTP = jsonState['stp']
                self._set_output_value(self.PIN_O_N_STP, int(nSTP))
            if 'dwo' in jsonState:
                nDWO = int(jsonState['dwo']) / 10.0
                self._set_output_value(self.PIN_O_N_DWO, float(nDWO))
            if 'wss' in jsonState:
                sWSS = jsonState['wss']
                self._set_output_value(self.PIN_O_S_WSS, str(sWSS))
            if 'wke' in jsonState:
                sWKE = jsonState['wke']
                self._set_output_value(self.PIN_O_S_WKE, str(sWKE))
            if 'wen' in jsonState:
                nWEN = jsonState['wen']
                self._set_output_value(self.PIN_O_N_WEN, str(nWEN))
            if 'tof' in jsonState:
                nTOF = jsonState['tof']
                self._set_output_value(self.PIN_O_N_TOF, str(nTOF))
            if 'tds' in jsonState:
                nTDS = jsonState['tds']
                self._set_output_value(self.PIN_O_N_TDS, str(nTDS))
            if 'lbr' in jsonState:
                nLBR = int(jsonState['lbr']) / 255.0 * 100
                self._set_output_value(self.PIN_O_N_LBR, int(nLBR))
            if 'aho' in jsonState:
                nAHO = jsonState['aho']
                self._set_output_value(self.PIN_O_N_AHO, str(nAHO))
            if 'afi' in jsonState:
                nAFI = jsonState['afi']
                self._set_output_value(self.PIN_O_N_AFI, str(nAFI))
            if 'ama' in jsonState:
                nAMA = jsonState['ama']
                self._set_output_value(self.PIN_O_N_AMA, str(nAMA))
            if 'al1' in jsonState:
                nAL1 = jsonState['al1']
                self._set_output_value(self.PIN_O_N_AL1, str(nAL1))
            if 'al2' in jsonState:
                nAL2 = jsonState['al2']
                self._set_output_value(self.PIN_O_N_AL2, str(nAL2))
            if 'al3' in jsonState:
                nAL3 = jsonState['al3']
                self._set_output_value(self.PIN_O_N_AL3, str(nAL3))
            if 'al4' in jsonState:
                nAL4 = jsonState['al4']
                self._set_output_value(self.PIN_O_N_AL4, str(nAL4))
            if 'al5' in jsonState:
                nAL5 = jsonState['al5']
                self._set_output_value(self.PIN_O_N_AL5, str(nAL5))
            if 'cid' in jsonState:
                nCID = jsonState['cid']
                self._set_output_value(self.PIN_O_N_CID, str(nCID))
            if 'cch' in jsonState:
                nCCH = jsonState['cch']
                self._set_output_value(self.PIN_O_N_CCH, str(nCCH))
            if 'cfi' in jsonState:
                nCFI = jsonState['cfi']
                self._set_output_value(self.PIN_O_N_CFI, str(nCFI))
            if 'lse' in jsonState:
                nLSE = jsonState['lse']
                self._set_output_value(self.PIN_O_N_LSE, str(nLSE))
            if 'ust' in jsonState:
                nUST = jsonState['ust']
                self._set_output_value(self.PIN_O_N_UST, str(nUST))
            if 'wak' in jsonState:
                sWAK = jsonState['wak']
                self._set_output_value(self.PIN_O_S_WAK, str(sWAK))
            if 'r1x' in jsonState:
                nR1X = jsonState['r1x']
                self._set_output_value(self.PIN_O_N_R1X, str(nR1X))
            if 'dto' in jsonState:
                nDTO = jsonState['dto']
                self._set_output_value(self.PIN_O_N_DTO, str(nDTO))
            if 'nmo' in jsonState:
                nNMO = jsonState['nmo']
                self._set_output_value(self.PIN_O_N_NMO, str(nNMO))
            if 'rna' in jsonState:
                nRNA = jsonState['rna']
                self._set_output_value(self.PIN_O_S_RNA, str(nRNA))
            if 'rnm' in jsonState:
                nRNM = jsonState['rnm']
                self._set_output_value(self.PIN_O_S_RNM, str(nRNM))
            if 'rne' in jsonState:
                nRNE = jsonState['rne']
                self._set_output_value(self.PIN_O_S_RNE, str(nRNE))
            if 'rn4' in jsonState:
                nRN4 = jsonState['rn4']
                self._set_output_value(self.PIN_O_S_RN4, str(nRN4))
            if 'rn5' in jsonState:
                nRN5 = jsonState['rn5']
                self._set_output_value(self.PIN_O_S_RN5, str(nRN5))
            if 'rn6' in jsonState:
                nRN6 = jsonState['rn6']
                self._set_output_value(self.PIN_O_S_RN6, str(nRN6))
            if 'rn7' in jsonState:
                nRN7 = jsonState['rn7']
                self._set_output_value(self.PIN_O_S_RN7, str(nRN7))
            if 'rn8' in jsonState:
                nRN8 = jsonState['rn8']
                self._set_output_value(self.PIN_O_S_RN8, str(nRN8))
            if 'rn9' in jsonState:
                nRN9 = jsonState['rn9']
                self._set_output_value(self.PIN_O_S_RN9, str(nRN9))
            if 'rn1' in jsonState:
                nRN1 = jsonState['rn1']
                self._set_output_value(self.PIN_O_S_RN1, str(nRN1))
            if 'upd' in jsonState:
                nUPD = jsonState['upd']
                self._set_output_value(self.PIN_O_S_RN1, int(nUPD))
        except Exception as e:
            jsonState = []
            self.DEBUG.add_message("14105 in 'readJson': " + str(e))

        return json.dumps(jsonState)

    def httpGet(self, api_url, api_port, key, val):
        httpClient = None
        data = {'data': "", 'status': -1}
        try:
            api_path = '/mqtt?payload=' + str(key) + '=' + str(val)
            # headers = { "HOST": str(api_url + ":" + str(api_port)), "CONTENT-LENGTH": str(0), "Content-type": 'application/json' }
            httpClient = httplib.HTTPConnection(api_url, int(api_port), timeout=5)

            httpClient.request("GET", api_path)
            response = httpClient.getresponse()
            status = response.status
            data = {'data': response.read(), 'status': status}
            self.readJson(data['data'])
            return data
        except Exception as e:
            self.DEBUG.add_message("14105 in 'httpGet': " + str(e))
            return data
        finally:
            if httpClient:
                httpClient.close()

    def on_init(self):
        self.DEBUG = self.FRAMEWORK.create_debug_section()
        self.m_index2key = {}
        self.m_index2key = {str(self.PIN_I_N_AMP): 'amp',
                            str(self.PIN_I_N_AST): 'ast',
                            str(self.PIN_I_N_ALW): 'alw',
                            str(self.PIN_I_N_STP): 'stp',
                            str(self.PIN_I_N_DWO): 'dwo',
                            str(self.PIN_I_S_WSS): 'wss',
                            str(self.PIN_I_S_WKE): 'wke',
                            str(self.PIN_I_N_WEN): 'wen',
                            str(self.PIN_I_N_TOF): 'tof',
                            str(self.PIN_I_N_TDS): 'tds',
                            str(self.PIN_I_N_LBR): 'lbr',
                            str(self.PIN_I_N_AHO): 'aho',
                            str(self.PIN_I_N_AFO): 'afo',
                            str(self.PIN_I_N_AL1): 'al1',
                            str(self.PIN_I_N_AL2): 'al2',
                            str(self.PIN_I_N_AL3): 'al3',
                            str(self.PIN_I_N_AL4): 'al4',
                            str(self.PIN_I_N_AL5): 'al5',
                            str(self.PIN_I_N_CID): 'cid',
                            str(self.PIN_I_N_CCH): 'cch',
                            str(self.PIN_I_N_CFI): 'cfi',
                            str(self.PIN_I_N_LSE): 'lse',
                            str(self.PIN_I_N_UST): 'ust',
                            str(self.PIN_I_S_WAK): 'wak',
                            str(self.PIN_I_N_R1X): 'r1x',
                            str(self.PIN_I_N_DTO): 'dto',
                            str(self.PIN_I_N_NMO): 'nmo',
                            str(self.PIN_I_S_RNA): 'rna',
                            str(self.PIN_I_S_RNM): 'rnm',
                            str(self.PIN_I_S_RNE): 'rne',
                            str(self.PIN_I_S_RN1): 'rn1',
                            str(self.PIN_I_S_RN4): 'rn4',
                            str(self.PIN_I_S_RN5): 'rn5',
                            str(self.PIN_I_S_RN6): 'rn6',
                            str(self.PIN_I_S_RN7): 'rn7',
                            str(self.PIN_I_S_RN8): 'rn8',
                            str(self.PIN_I_S_RN9): 'rn9',
                            str(self.PIN_I_N_AZO): 'azo',
                            str(self.PIN_I_N_AMA): 'ama'}

        nInterval = self._get_input_value(self.PIN_I_N_INTERVAL)
        if (nInterval > 0):
            self.getData()

    def on_input_value(self, index, value):
        if ((self.PIN_I_N_TRIGGER == index) and (value != 0)):
            ret = self.getData()

        else:
            if str(index) in self.m_index2key:
                sUrl = str(self._get_input_value(self.PIN_I_S_IP))
                nPort = int(self._get_input_value(self.PIN_I_N_PORT))
                sKey = self.m_index2key[str(index)]
                if (sKey == "lbr"):
                    self.httpGet(sUrl, nPort, sKey, str(int(value) * 255 / 100))
                elif (sKey == "dwo"):
                    self.httpGet(sUrl, nPort, sKey, str(float(value) * 10))
                else:
                    self.httpGet(sUrl, nPort, sKey, str(value))
