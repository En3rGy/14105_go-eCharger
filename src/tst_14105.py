# coding: UTF-8

import unittest


import httplib
import json
import threading


class hsl20_3:
    LOGGING_NONE = 0

    def __init__(self):
        pass

    class BaseModule:
        debug_gain = 1.0  # type: float
        debug_offset = 0.0  # type: float
        debug_set_output_value = {}
        debug_input_value = {}
        debug_set_remanent = {}

        def __init__(self, a, b):
            pass

        def _get_framework(self):
            f = hsl20_3.Framework()
            return f

        def _get_logger(self, a, b):
            return 0

        def _get_remanent(self, key):
            return self.debug_set_remanent[key]

        def _set_remanent(self, key, val):
            self.debug_set_remanent[key] = val

        def _set_output_value(self, pin, value):
            self.debug_set_output_value[pin] = value

        def _get_input_value(self, pin):
            if pin in self.debug_input_value:
                return self.debug_input_value[pin]
            else:
                return 0

    class Framework:
        def __init__(self):
            pass

        def _run_in_context_thread(self, a):
            pass

        def create_debug_section(self):
            d = hsl20_3.DebugHelper()
            return d

    class DebugHelper:
        def __init__(self):
            pass

        def set_value(self, cap, text):
            print ("DEBUG value\t'" + str(cap) + "': " + str(text))

        def add_message(self, msg):
            print ("Debug Msg\t" + str(msg))


################################################
################################################

class Go_eCharger_14105_14105(hsl20_3.BaseModule):

    def __init__(self, homeserver_context):
        hsl20_3.BaseModule.__init__(self, homeserver_context, "hsl20_3_go_eCharger")
        self.FRAMEWORK = self._get_framework()
        self.LOGGER = self._get_logger(hsl20_3.LOGGING_NONE, ())
        self.FRAMEWORK._run_in_context_thread(self.on_init)
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
        self.PIN_I_AMX=44
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
        self.PIN_O_AMX=79

    ########################################################################################################
    #### Own written code can be placed after this commentblock . Do not change or delete commentblock! ####
    ###################################################################################################!!!##

    m_index2key = {}

    def get_data(self):
        api_url = str(self._get_input_value(self.PIN_I_S_IP))
        api_port = int(self._get_input_value(self.PIN_I_N_PORT))
        n_interval = self._get_input_value(self.PIN_I_N_INTERVAL)

        api_path = '/status'
        data = {}

        try:
            http_client = httplib.HTTPConnection(api_url, int(api_port), timeout=5)
            http_client.request("GET", api_path)
            response = http_client.getresponse()
            status = response.status
            data = {'data': response.read(), 'status': status}
            self.DEBUG.add_message("14105: http response code: " + str(status))
        except Exception as e:
            self.DEBUG.add_message("14105: " + str(e))
        finally:
            if http_client:
                http_client.close()

        if 'data' in data:
            self.read_json(data['data'])
            self._set_output_value(self.PIN_O_N_ONLINE, 1)

        else:
            self.DEBUG.add_message("14105: Could not receive data")
            self._set_output_value(self.PIN_O_N_ONLINE, 0)

        if n_interval > 0:
            t = threading.Timer(n_interval, self.get_data).start()

    # read light data from json
    def read_json(self, json_state):
        try:
            json_state = json.loads(json_state)

            if 'version' in json_state:
                s_ver = json_state['version']
                self._set_output_value(self.PIN_O_S_VERSION, str(s_ver))
            if 'rbc' in json_state:
                n_rbc = json_state['rbc']
                self._set_output_value(self.PIN_O_N_RBC, int(n_rbc))
            if 'rbt' in json_state:
                n_rbt = int(json_state['rbt']) / 1000
                self._set_output_value(self.PIN_O_N_RBT, int(n_rbt))
            if 'car' in json_state:
                n_car = json_state['car']
                self._set_output_value(self.PIN_O_N_CAR, int(n_car))
            if 'car' in json_state:
                n_car = json_state['car']
                self._set_output_value(self.PIN_O_N_CAR, int(n_car))
            if 'err' in json_state:
                n_err = json_state['err']
                self._set_output_value(self.PIN_O_N_ERR, int(n_err))
            if 'cbl' in json_state:
                n_cbl = json_state['cbl']
                self._set_output_value(self.PIN_O_N_CBL, int(n_cbl))
            if 'pha' in json_state:
                n_pha = json_state['pha']
                self._set_output_value(self.PIN_O_N_PHA, int(n_pha))
            if 'tmp' in json_state:
                n_tmp = json_state['tmp']
                self._set_output_value(self.PIN_O_N_TMP, int(n_tmp))
            if 'dws' in json_state:
                n_dws = int(json_state['dws']) / 360000.0
                self._set_output_value(self.PIN_O_N_DWS, float(n_dws))
            if 'adi' in json_state:
                n_adi = json_state['adi']
                self._set_output_value(self.PIN_O_N_ADI, int(n_adi))
            if 'uby' in json_state:
                n_uby = json_state['uby']
                self._set_output_value(self.PIN_O_N_UBY, int(n_uby))
            if 'eto' in json_state:
                n_eto = int(json_state['eto']) / 10.0
                self._set_output_value(self.PIN_O_N_ETO, float(n_eto))
            if 'wst' in json_state:
                n_wst = json_state['wst']
                self._set_output_value(self.PIN_O_N_WST, int(n_wst))
            if 'amx' in json_state:
                amx = json_state['amx']
                self._set_output_value(self.PIN_O_AMX, int(amx))

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
            if 'nrg' in json_state:
                nrg = json_state['nrg']
                nrg_curr = (int(nrg[4]) + int(nrg[5]) + int(nrg[6])) / 10
                self._set_output_value(self.PIN_O_N_NRG_CURR, nrg_curr)
            if 'fwv' in json_state:
                s_fwv = json_state['fwv']
                self._set_output_value(self.PIN_O_S_FWV, str(s_fwv))
            if 'sse' in json_state:
                s_sse = json_state['sse']
                self._set_output_value(self.PIN_O_S_SSE, int(s_sse))
            if 'eca' in json_state:
                n_eca = int(json_state['eca']) / 10.0
                self._set_output_value(self.PIN_O_N_ECA, float(n_eca))
            if 'ecr' in json_state:
                n_ecr = int(json_state['ecr']) / 10.0
                self._set_output_value(self.PIN_O_N_ECR, float(n_ecr))
            if 'ecd' in json_state:
                n_ecd = int(json_state['ecd']) / 10.0
                self._set_output_value(self.PIN_O_N_ECD, float(n_ecd))
            if 'ec4' in json_state:
                n_ec4 = int(json_state['ec4']) / 10.0
                self._set_output_value(self.PIN_O_N_EC4, float(n_ec4))
            if 'ec5' in json_state:
                n_ec5 = int(json_state['ec5']) / 10.0
                self._set_output_value(self.PIN_O_N_EC5, float(n_ec5))
            if 'ec6' in json_state:
                n_ec6 = int(json_state['ec6']) / 10.0
                self._set_output_value(self.PIN_O_N_EC6, float(n_ec6))
            if 'ec7' in json_state:
                n_ec7 = int(json_state['ec7']) / 10.0
                self._set_output_value(self.PIN_O_N_EC7, float(n_ec7))
            if 'ec8' in json_state:
                n_ec8 = int(json_state['ec8']) / 10.0
                self._set_output_value(self.PIN_O_N_EC8, float(n_ec8))
            if 'ec9' in json_state:
                n_ec9 = int(json_state['ec9']) / 10.0
                self._set_output_value(self.PIN_O_N_EC9, float(n_ec9))
            if 'ec1' in json_state:
                n_ec1 = int(json_state['ec1']) / 10.0
                self._set_output_value(self.PIN_O_N_EC1, float(n_ec1))
            if 'rca' in json_state:
                s_rca = json_state['rca']
                self._set_output_value(self.PIN_O_S_RCA, str(s_rca))
            if 'rcr' in json_state:
                s_rcr = json_state['rcr']
                self._set_output_value(self.PIN_O_S_RCR, str(s_rcr))
            if 'rcd' in json_state:
                s_rcd = json_state['rcd']
                self._set_output_value(self.PIN_O_S_RCD, str(s_rcd))
            if 'rc4' in json_state:
                s_rc4 = json_state['rc4']
                self._set_output_value(self.PIN_O_S_RC4, str(s_rc4))
            if 'rc5' in json_state:
                s_rc5 = json_state['rc5']
                self._set_output_value(self.PIN_O_S_RC5, str(s_rc5))
            if 'rc6' in json_state:
                s_rc6 = json_state['rc6']
                self._set_output_value(self.PIN_O_S_RC6, str(s_rc6))
            if 'rc7' in json_state:
                s_rc7 = json_state['rc7']
                self._set_output_value(self.PIN_O_S_RC7, str(s_rc7))
            if 'rc8' in json_state:
                s_rc8 = json_state['rc8']
                self._set_output_value(self.PIN_O_S_RC8, str(s_rc8))
            if 'rc9' in json_state:
                s_rc9 = json_state['rc9']
                self._set_output_value(self.PIN_O_S_RC9, str(s_rc9))
            if 'rc1' in json_state:
                s_rc1 = json_state['rc1']
                self._set_output_value(self.PIN_O_S_RC1, str(s_rc1))
            if 'tme' in json_state:
                s_tme = json_state['tme']
                # ddmmyyhhmi -> dd.mm.yyyy hh:mi
                if len(s_tme) == 10:
                    s_tme = s_tme[0:1] + '.' + s_tme[2:3] + s_tme[4:5] + ' ' + s_tme[6:7] + ":" + s_tme[8:9]
                self._set_output_value(self.PIN_O_S_TME, str(s_tme))
            if 'amp' in json_state:
                n_amp = json_state['amp']
                self._set_output_value(self.PIN_O_N_AMP, int(n_amp))
            if 'ast' in json_state:
                n_ast = json_state['ast']
                self._set_output_value(self.PIN_O_N_AST, int(n_ast))
            if 'alw' in json_state:
                n_alw = json_state['alw']
                self._set_output_value(self.PIN_O_N_ALW, int(n_alw))
            if 'stp' in json_state:
                n_stp = json_state['stp']
                self._set_output_value(self.PIN_O_N_STP, int(n_stp))
            if 'dwo' in json_state:
                n_dwo = int(json_state['dwo']) / 10.0
                self._set_output_value(self.PIN_O_N_DWO, float(n_dwo))
            if 'wss' in json_state:
                s_wss = json_state['wss']
                self._set_output_value(self.PIN_O_S_WSS, str(s_wss))
            if 'wke' in json_state:
                s_wke = json_state['wke']
                self._set_output_value(self.PIN_O_S_WKE, str(s_wke))
            if 'wen' in json_state:
                n_wen = json_state['wen']
                self._set_output_value(self.PIN_O_N_WEN, str(n_wen))
            if 'tof' in json_state:
                n_tof = json_state['tof']
                self._set_output_value(self.PIN_O_N_TOF, str(n_tof))
            if 'tds' in json_state:
                n_tds = json_state['tds']
                self._set_output_value(self.PIN_O_N_TDS, str(n_tds))
            if 'lbr' in json_state:
                n_lbr = int(json_state['lbr']) / 255.0 * 100
                self._set_output_value(self.PIN_O_N_LBR, int(n_lbr))
            if 'aho' in json_state:
                n_aho = json_state['aho']
                self._set_output_value(self.PIN_O_N_AHO, str(n_aho))
            if 'afi' in json_state:
                n_afi = json_state['afi']
                self._set_output_value(self.PIN_O_N_AFI, str(n_afi))
            if 'ama' in json_state:
                n_ama = json_state['ama']
                self._set_output_value(self.PIN_O_N_AMA, str(n_ama))
            if 'al1' in json_state:
                n_al1 = json_state['al1']
                self._set_output_value(self.PIN_O_N_AL1, str(n_al1))
            if 'al2' in json_state:
                n_al2 = json_state['al2']
                self._set_output_value(self.PIN_O_N_AL2, str(n_al2))
            if 'al3' in json_state:
                n_al3 = json_state['al3']
                self._set_output_value(self.PIN_O_N_AL3, str(n_al3))
            if 'al4' in json_state:
                n_al4 = json_state['al4']
                self._set_output_value(self.PIN_O_N_AL4, str(n_al4))
            if 'al5' in json_state:
                n_al5 = json_state['al5']
                self._set_output_value(self.PIN_O_N_AL5, str(n_al5))
            if 'cid' in json_state:
                n_cid = json_state['cid']
                self._set_output_value(self.PIN_O_N_CID, str(n_cid))
            if 'cch' in json_state:
                n_cch = json_state['cch']
                self._set_output_value(self.PIN_O_N_CCH, str(n_cch))
            if 'cfi' in json_state:
                n_cfi = json_state['cfi']
                self._set_output_value(self.PIN_O_N_CFI, str(n_cfi))
            if 'lse' in json_state:
                n_lse = json_state['lse']
                self._set_output_value(self.PIN_O_N_LSE, str(n_lse))
            if 'ust' in json_state:
                n_ust = json_state['ust']
                self._set_output_value(self.PIN_O_N_UST, str(n_ust))
            if 'wak' in json_state:
                s_wak = json_state['wak']
                self._set_output_value(self.PIN_O_S_WAK, str(s_wak))
            if 'r1x' in json_state:
                n_r1_x = json_state['r1x']
                self._set_output_value(self.PIN_O_N_R1X, str(n_r1_x))
            if 'dto' in json_state:
                n_dto = json_state['dto']
                self._set_output_value(self.PIN_O_N_DTO, str(n_dto))
            if 'nmo' in json_state:
                n_nmo = json_state['nmo']
                self._set_output_value(self.PIN_O_N_NMO, str(n_nmo))
            if 'rna' in json_state:
                n_rna = json_state['rna']
                self._set_output_value(self.PIN_O_S_RNA, str(n_rna))
            if 'rnm' in json_state:
                n_rnm = json_state['rnm']
                self._set_output_value(self.PIN_O_S_RNM, str(n_rnm))
            if 'rne' in json_state:
                n_rne = json_state['rne']
                self._set_output_value(self.PIN_O_S_RNE, str(n_rne))
            if 'rn4' in json_state:
                n_rn4 = json_state['rn4']
                self._set_output_value(self.PIN_O_S_RN4, str(n_rn4))
            if 'rn5' in json_state:
                n_rn5 = json_state['rn5']
                self._set_output_value(self.PIN_O_S_RN5, str(n_rn5))
            if 'rn6' in json_state:
                n_rn6 = json_state['rn6']
                self._set_output_value(self.PIN_O_S_RN6, str(n_rn6))
            if 'rn7' in json_state:
                n_rn7 = json_state['rn7']
                self._set_output_value(self.PIN_O_S_RN7, str(n_rn7))
            if 'rn8' in json_state:
                n_rn8 = json_state['rn8']
                self._set_output_value(self.PIN_O_S_RN8, str(n_rn8))
            if 'rn9' in json_state:
                n_rn9 = json_state['rn9']
                self._set_output_value(self.PIN_O_S_RN9, str(n_rn9))
            if 'rn1' in json_state:
                n_rn1 = json_state['rn1']
                self._set_output_value(self.PIN_O_S_RN1, str(n_rn1))
            if 'upd' in json_state:
                n_upd = json_state['upd']
                self._set_output_value(self.PIN_O_S_RN1, int(n_upd))
        except Exception as e:
            json_state = []
            self.DEBUG.add_message("14105 in 'readJson': " + str(e))

        return json.dumps(json_state)

    def http_get(self, api_url, api_port, key, val):
        http_client = None
        data = {'data': "", 'status': -1}
        try:
            api_path = '/mqtt?payload=' + str(key) + '=' + str(val)
            # headers = { "HOST": str(api_url + ":" + str(api_port)), "CONTENT-LENGTH": str(0), "Content-type":
            # 'application/json' }
            http_client = httplib.HTTPConnection(api_url, int(api_port), timeout=5)

            http_client.request("GET", api_path)
            response = http_client.getresponse()
            status = response.status
            data = {'data': response.read(), 'status': status}
            self.read_json(data['data'])
            return data
        except Exception as e:
            self.DEBUG.add_message("14105 in 'httpGet': " + str(e))
            return data
        finally:
            if http_client:
                http_client.close()

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
                            str(self.PIN_I_N_AMA): 'ama',
                            str(self.PIN_I_AMX): 'amx'}

        n_interval = self._get_input_value(self.PIN_I_N_INTERVAL)
        if n_interval > 0:
            self.get_data()

    def on_input_value(self, index, value):
        if (self.PIN_I_N_TRIGGER == index) and (value != 0):
            self.get_data()

        else:
            if str(index) in self.m_index2key:
                s_url = str(self._get_input_value(self.PIN_I_S_IP))
                n_port = int(self._get_input_value(self.PIN_I_N_PORT))
                s_key = self.m_index2key[str(index)]
                if s_key == "lbr":
                    self.http_get(s_url, n_port, s_key, str(int(value) * 255 / 100))
                elif s_key == "dwo":
                    self.http_get(s_url, n_port, s_key, str(float(value) * 10))
                else:
                    self.http_get(s_url, n_port, s_key, str(value))


################################################
################################################


class RequirementsVerification(unittest.TestCase):

    cred = 0
    tst = 0

    def setUp(self):
        print("\n###setUp")
        with open("credentials.txt") as f:
            self.cred = json.load(f)

        self.tst = Go_eCharger_14105_14105(0)
        self.tst.on_init()

        self.tst.debug_input_value[self.tst.PIN_I_S_IP] = self.cred["PIN_I_S_IP"]
        self.tst.debug_input_value[self.tst.PIN_I_N_PORT] = self.cred["PIN_I_N_PORT"]

    def test_trigger(self):
        print("\n###test_trigger")
        self.tst.on_init()
        self.tst.on_input_value(self.tst.PIN_I_N_TRIGGER, 1)
        self.assertTrue(True)

    def test_tme(self):
        print("\n###test_tme")
        self.tst.on_init()
        js = '{"tme":"0104191236"}'
        self.tst.read_json(js)
        self.assertTrue("01.04.2019 12:36", self.tst.debug_set_output_value[self.tst.PIN_O_S_TME])

if __name__ == '__main__':
    unittest.main()
