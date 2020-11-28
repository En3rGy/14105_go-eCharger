# coding: UTF-8
import httplib
import json
from __builtin__ import set

##!!!!##################################################################################################
#### Own written code can be placed above this commentblock . Do not change or delete commentblock! ####
########################################################################################################
##** Code created by generator - DO NOT CHANGE! **##

class Go_eCharger_14105_14105(hsl20_3.BaseModule):

    def __init__(self, homeserver_context):
        hsl20_3.BaseModule.__init__(self, homeserver_context, "hsl20_3_json")
        self.FRAMEWORK = self._get_framework()
        self.LOGGER = self._get_logger(hsl20_3.LOGGING_NONE,())
        self.PIN_I_S_IP=1
        self.PIN_I_N_PORT=2
        self.PIN_I_N_TRIGGER=3
        self.PIN_I_N_AMP=4
        self.PIN_I_N_AST=5
        self.PIN_I_N_ALW=6
        self.PIN_I_N_STP=7
        self.PIN_I_N_DWO=8
        self.PIN_I_S_WSS=9
        self.PIN_I_S_WKE=10
        self.PIN_I_N_WEN=11
        self.PIN_I_N_TOF=12
        self.PIN_I_N_TDS=13
        self.PIN_I_N_LBR=14
        self.PIN_I_N_AHO=15
        self.PIN_I_N_AFO=16
        self.PIN_I_N_AL1=17
        self.PIN_I_N_AL2=18
        self.PIN_I_N_AL3=19
        self.PIN_I_N_AL4=20
        self.PIN_I_N_AL5=21
        self.PIN_I_N_CID=22
        self.PIN_I_N_CCH=23
        self.PIN_I_N_CFI=24
        self.PIN_I_N_LSE=25
        self.PIN_I_N_UST=26
        self.PIN_I_N_WAK=27
        self.PIN_I_N_R1X=28
        self.PIN_I_N_DTO=29
        self.PIN_I_N_NMO=30
        self.PIN_I_N_RNA=31
        self.PIN_I_N_RNM=32
        self.PIN_I_N_RNE=33
        self.PIN_I_N_RN1=34
        self.PIN_I_N_RN4=35
        self.PIN_I_N_RN5=36
        self.PIN_I_N_RN6=37
        self.PIN_I_N_RN7=38
        self.PIN_I_N_RN8=39
        self.PIN_I_N_RN9=40
        self.PIN_I_N_AZO=41
        self.PIN_I_N_AMA=42
        self.PIN_O_S_VERSION=1
        self.PIN_O_N_RBC=2
        self.PIN_O_N_RBT=3
        self.PIN_O_N_CAR=4
        self.PIN_O_N_RR=5
        self.PIN_O_N_CBL=6
        self.PIN_O_N_PHA=7
        self.PIN_O_N_CMP=8
        self.PIN_O_N_DWS=9
        self.PIN_O_N_ADI=10
        self.PIN_O_N_UBY=11
        self.PIN_O_N_ETO=12
        self.PIN_O_N_WST=13
        self.PIN_O_N_NRG=14
        self.PIN_O_S_FWV=15
        self.PIN_O_S_SSE=16
        self.PIN_O_N_ACE=17
        self.PIN_O_N_ECR=18
        self.PIN_O_N_ECD=19
        self.PIN_O_N_EC4=20
        self.PIN_O_N_EC5=21
        self.PIN_O_N_EC6=22
        self.PIN_O_N_EC7=23
        self.PIN_O_N_EC8=24
        self.PIN_O_N_EC9=25
        self.PIN_O_N_EC1=26
        self.PIN_O_N_RCA=27
        self.PIN_O_N_RCR=28
        self.PIN_O_N_RCD=29
        self.PIN_O_N_RC4=30
        self.PIN_O_N_RC5=31
        self.PIN_O_N_RC6=32
        self.PIN_O_N_RC7=33
        self.PIN_O_N_RC8=34
        self.PIN_O_N_RC9=35
        self.PIN_O_N_RC1=36
        self.PIN_O_N_AMP=37
        self.PIN_O_N_AST=38
        self.PIN_O_N_ALW=39
        self.PIN_O_N_STP=40
        self.PIN_O_N_DWO=41
        self.PIN_O_S_WSS=42
        self.PIN_O_S_WKE=43
        self.PIN_O_N_WEN=44
        self.PIN_O_N_TOF=45
        self.PIN_O_N_TDS=46
        self.PIN_O_N_LBR=47
        self.PIN_O_N_AHO=48
        self.PIN_O_N_AFO=49
        self.PIN_O_N_AL1=50
        self.PIN_O_N_AL2=51
        self.PIN_O_N_AL3=52
        self.PIN_O_N_AL4=53
        self.PIN_O_N_AL5=54
        self.PIN_O_N_CID=55
        self.PIN_O_N_CCH=56
        self.PIN_O_N_CFI=57
        self.PIN_O_N_LSE=58
        self.PIN_O_N_UST=59
        self.PIN_O_N_WAK=60
        self.PIN_O_N_R1X=61
        self.PIN_O_N_DTO=62
        self.PIN_O_N_NMO=63
        self.PIN_O_N_RNA=64
        self.PIN_O_N_RNM=65
        self.PIN_O_N_RNE=66
        self.PIN_O_N_RN1=67
        self.PIN_O_N_RN4=68
        self.PIN_O_N_RN5=69
        self.PIN_O_N_RN6=70
        self.PIN_O_N_RN7=71
        self.PIN_O_N_RN8=72
        self.PIN_O_N_RN9=73
        self.PIN_O_N_AZO=74
        self.PIN_O_N_AMA=75
        self.FRAMEWORK._run_in_context_thread(self.on_init)

########################################################################################################
#### Own written code can be placed after this commentblock . Do not change or delete commentblock! ####
###################################################################################################!!!##

    m_index2key = {}

    def getData(self, api_url, api_port):
        api_path = '/status'
        data = ""

        try:
            httpClient = httplib.HTTPConnection(api_url, int(api_port), timeout=5)
            httpClient.request("GET", api_path)
            response = httpClient.getresponse()
            status = response.status
            data = {'data' : response.read(), 'status' : status}
            self.DEBUG.add_message("14105: go-eCharger API: " + str(status))
        except Exception as e:
            self.DEBUG.add_message(str(e))
            return
        finally:
            if httpClient:
                httpClient.close()

        return data

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
                nRBT = jsonState['rbt']
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
                nDWS = jsonState['dws']
                self._set_output_value(self.PIN_O_N_DWS, int(nDWS))
            if 'adi' in jsonState:
                nADI = jsonState['adi']
                self._set_output_value(self.PIN_O_N_ADI, int(nADI))
            if 'uby' in jsonState:
                nUBY = jsonState['uby']
                self._set_output_value(self.PIN_O_N_UBY, int(nUBY))
            if 'eto' in jsonState:
                nETO = jsonState['eto']
                self._set_output_value(self.PIN_O_N_ETO, int(nETO))
            if 'wst' in jsonState:
                nWST = jsonState['wst']
                self._set_output_value(self.PIN_O_N_WST, int(nWST))
            if 'nrg' in jsonState:
                nNRG = jsonState['nrg']
                self._set_output_value(self.PIN_O_N_ERG, int(nNRG))
            if 'fwv' in jsonState:
                nFWV = jsonState['fwv']
                self._set_output_value(self.PIN_O_N_FWV, int(nFWV))
            if 'sse' in jsonState:
                nSSE = jsonState['sse']
                self._set_output_value(self.PIN_O_N_SSE, int(nSSE))
            if 'eca' in jsonState:
                nECA = jsonState['eca']
                self._set_output_value(self.PIN_O_N_ECA, int(nECA))
            if 'ecr' in jsonState:
                nECR = jsonState['ecr']
                self._set_output_value(self.PIN_O_N_ECR, int(nECR))
            if 'ecd' in jsonState:
                nECD = jsonState['ecd']
                self._set_output_value(self.PIN_O_N_ECD, int(nECD))
            if 'ec4' in jsonState:
                nEC4 = jsonState['ec4']
                self._set_output_value(self.PIN_O_N_EC4, int(nEC4))
            if 'ec5' in jsonState:
                nEC5 = jsonState['ec5']
                self._set_output_value(self.PIN_O_N_EC5, int(nEC5))
            if 'ec6' in jsonState:
                nEC6 = jsonState['ec6']
                self._set_output_value(self.PIN_O_N_EC6, int(nEC6))
            if 'ec7' in jsonState:
                nEC7 = jsonState['ec7']
                self._set_output_value(self.PIN_O_N_EC7, int(nEC7))
            if 'ec8' in jsonState:
                nEC8 = jsonState['ec8']
                self._set_output_value(self.PIN_O_N_EC8, int(nEC8))
            if 'ec9' in jsonState:
                nEC9 = jsonState['ec9']
                self._set_output_value(self.PIN_O_N_EC9, int(nEC9))
            if 'ec1' in jsonState:
                nEC1 = jsonState['ec1']
                self._set_output_value(self.PIN_O_N_EC1, int(nEC1))
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
                nDWO = jsonState['dwo']
                self._set_output_value(self.PIN_O_N_DWO, int(nDWO))
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
                nLBR = jsonState['lbr']
                self._set_output_value(self.PIN_O_N_LBR, str(nLBR))
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
                self._set_output_value(self.PIN_O_N_RNA, str(nRNA))
            if 'rnm' in jsonState:
                nRNM = jsonState['rnm']
                self._set_output_value(self.PIN_O_N_RNM, str(nRNM))
            if 'rne' in jsonState:
                nRNE = jsonState['rne']
                self._set_output_value(self.PIN_O_N_RNE, str(nRNE))
            if 'rn4' in jsonState:
                nRN4 = jsonState['rn4']
                self._set_output_value(self.PIN_O_N_RN4, str(nRN4))
            if 'rn5' in jsonState:
                nRN5 = jsonState['rn5']
                self._set_output_value(self.PIN_O_N_RN5, str(nRN5))
            if 'rn6' in jsonState:
                nRN6 = jsonState['rn6']
                self._set_output_value(self.PIN_O_N_RN6, str(nRN6))
            if 'rn7' in jsonState:
                nRN7 = jsonState['rn7']
                self._set_output_value(self.PIN_O_N_RN7, str(nRN7))
            if 'rn8' in jsonState:
                nRN7 = jsonState['rn8']
                self._set_output_value(self.PIN_O_N_RN8, str(nRN8))
            if 'rn9' in jsonState:
                nRN9 = jsonState['rn9']
                self._set_output_value(self.PIN_O_N_RN9, str(nRN9))
            if 'rn1' in jsonState:
                nRN1 = jsonState['rn1']
                self._set_output_value(self.PIN_O_N_RN1, str(nRN1))

        except:
            jsonState = []

        return json.dumps(jsonState)


    def httpGet(self, api_url, api_port, key, val):
        httpClient = None
        data = {'data' : "", 'status' : -1}
        try:
            api_path = '/mqtt?payload=' + str(key) + '=' + str(val)
            #headers = { "HOST": str(api_url + ":" + str(api_port)), "CONTENT-LENGTH": str(0), "Content-type": 'application/json' }
            httpClient = httplib.HTTPConnection(api_url, int(api_port), timeout=5)

            httpClient.request("GET", api_path) 
            response = httpClient.getresponse()
            status = response.status
            data = {'data' : response.read(), 'status' : status}
            return data
        #except Exception as e:
        except:
            return data
        finally:
            if httpClient:
                httpClient.close()


    def on_init(self):
        self.DEBUG = self.FRAMEWORK.create_debug_section()
        self.m_index2key = {self.PIN_I_N_AMP: 'amp',
                     self.PIN_I_N_AST: 'ast',
                     self.PIN_I_N_ALW: 'alw',
                     self.PIN_I_N_STP: 'stp',
                     self.PIN_I_N_DWO: 'dwo',
                     self.PIN_I_S_WSS: 'wss',
                     self.PIN_I_S_WKE: 'wke',
                     self.PIN_I_N_WEN: 'wen',
                     self.PIN_I_N_TOF: 'tof',
                     self.PIN_I_N_TDS: 'tds',
                     self.PIN_I_N_LBR: 'lbr',
                     self.PIN_I_N_AHO: 'aho',
                     self.PIN_I_N_AFO: 'afo',
                     self.PIN_I_N_AL1: 'al1',
                     self.PIN_I_N_AL2: 'al2',
                     self.PIN_I_N_AL3: 'al3',
                     self.PIN_I_N_AL4: 'al4',
                     self.PIN_I_N_AL5: 'al5',
                     self.PIN_I_N_CID: 'cid',
                     self.PIN_I_N_CCH: 'cch',
                     self.PIN_I_N_CFI: 'cfi',
                     self.PIN_I_N_LSE: 'lse',
                     self.PIN_I_N_UST: 'ust',
                     self.PIN_I_N_WAK: 'wak',
                     self.PIN_I_N_R1X: 'r1x',
                     self.PIN_I_N_DTO: 'dto',
                     self.PIN_I_N_NMO: 'nmo',
                     self.PIN_I_N_RNA: 'rna',
                     self.PIN_I_N_RNM: 'rnm',
                     self.PIN_I_N_RNE: 'rne',
                     self.PIN_I_N_RN1: 'rn1',
                     self.PIN_I_N_RN4: 'rn4',
                     self.PIN_I_N_RN5: 'rn5',
                     self.PIN_I_N_RN6: 'rn6',
                     self.PIN_I_N_RN7: 'rn7',
                     self.PIN_I_N_RN8: 'rn8',
                     self.PIN_I_N_RN9: 'rn9',
                     self.PIN_I_N_AZO: 'azo',
                     self.PIN_I_N_AMA: 'ama'}

    def on_input_value(self, index, value):

        sUrl = str(self._get_input_value(self.PIN_I_S_IP))
        nPort = int(self._get_input_value(self.PIN_I_N_PORT))

        if (self.PIN_I_N_TRIGGER == index):
            ret = self.getData( sUrl, nPort)
            readJson(ret['data'])
        else:
            self.httpGet(sUrl, nPort, self.m_index2key(index), str(self._get_input_value(index)))

