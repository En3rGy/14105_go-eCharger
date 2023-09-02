# coding: UTF-8
import httplib
import json
import threading


##!!!!##################################################################################################
#### Own written code can be placed above this commentblock . Do not change or delete commentblock! ####
########################################################################################################
##** Code created by generator - DO NOT CHANGE! **##

class Go_eCharger_14105_14105(hsl20_4.BaseModule):

    def __init__(self, homeserver_context):
        hsl20_4.BaseModule.__init__(self, homeserver_context, "hsl20_3_go_eCharger")
        self.FRAMEWORK = self._get_framework()
        self.LOGGER = self._get_logger(hsl20_4.LOGGING_NONE, ())
        self.PIN_I_S_IP = 1
        self.PIN_I_N_PORT = 2
        self.PIN_I_N_INTERVAL = 3
        self.PIN_I_N_TRIGGER = 4
        self.PIN_I_N_AMP = 5
        self.PIN_I_N_AST = 6
        self.PIN_I_N_ALW = 7
        self.PIN_I_N_STP = 8
        self.PIN_I_N_DWO = 9
        self.PIN_I_S_WSS = 10
        self.PIN_I_S_WKE = 11
        self.PIN_I_N_WEN = 12
        self.PIN_I_N_TOF = 13
        self.PIN_I_N_TDS = 14
        self.PIN_I_N_LBR = 15
        self.PIN_I_N_AHO = 16
        self.PIN_I_N_AFO = 17
        self.PIN_I_N_AL1 = 18
        self.PIN_I_N_AL2 = 19
        self.PIN_I_N_AL3 = 20
        self.PIN_I_N_AL4 = 21
        self.PIN_I_N_AL5 = 22
        self.PIN_I_N_CID = 23
        self.PIN_I_N_CCH = 24
        self.PIN_I_N_CFI = 25
        self.PIN_I_N_LSE = 26
        self.PIN_I_N_UST = 27
        self.PIN_I_S_WAK = 28
        self.PIN_I_N_R1X = 29
        self.PIN_I_N_DTO = 30
        self.PIN_I_N_NMO = 31
        self.PIN_I_S_RNA = 32
        self.PIN_I_S_RNM = 33
        self.PIN_I_S_RNE = 34
        self.PIN_I_S_RN1 = 35
        self.PIN_I_S_RN4 = 36
        self.PIN_I_S_RN5 = 37
        self.PIN_I_S_RN6 = 38
        self.PIN_I_S_RN7 = 39
        self.PIN_I_S_RN8 = 40
        self.PIN_I_S_RN9 = 41
        self.PIN_I_N_AZO = 42
        self.PIN_I_N_AMA = 43
        self.PIN_I_AMX = 44
        self.PIN_O_N_ONLINE = 1
        self.PIN_O_S_VERSION = 2
        self.PIN_O_N_RBC = 3
        self.PIN_O_N_RBT = 4
        self.PIN_O_N_CAR = 5
        self.PIN_O_N_ERR = 6
        self.PIN_O_N_CBL = 7
        self.PIN_O_N_PHA = 8
        self.PIN_O_N_TMP = 9
        self.PIN_O_N_DWS = 10
        self.PIN_O_N_ADI = 11
        self.PIN_O_N_UBY = 12
        self.PIN_O_N_ETO = 13
        self.PIN_O_N_WST = 14
        self.PIN_O_N_NRG_CURR = 15
        self.PIN_O_NRG_JSON = 16
        self.PIN_O_S_FWV = 17
        self.PIN_O_S_SSE = 18
        self.PIN_O_N_ECA = 19
        self.PIN_O_N_ECR = 20
        self.PIN_O_N_ECD = 21
        self.PIN_O_N_EC4 = 22
        self.PIN_O_N_EC5 = 23
        self.PIN_O_N_EC6 = 24
        self.PIN_O_N_EC7 = 25
        self.PIN_O_N_EC8 = 26
        self.PIN_O_N_EC9 = 27
        self.PIN_O_N_EC1 = 28
        self.PIN_O_S_RCA = 29
        self.PIN_O_S_RCR = 30
        self.PIN_O_S_RCD = 31
        self.PIN_O_S_RC4 = 32
        self.PIN_O_S_RC5 = 33
        self.PIN_O_S_RC6 = 34
        self.PIN_O_S_RC7 = 35
        self.PIN_O_S_RC8 = 36
        self.PIN_O_S_RC9 = 37
        self.PIN_O_S_RC1 = 38
        self.PIN_O_S_TME = 39
        self.PIN_O_N_AMP = 40
        self.PIN_O_N_AST = 41
        self.PIN_O_N_ALW = 42
        self.PIN_O_N_STP = 43
        self.PIN_O_N_DWO = 44
        self.PIN_O_S_WSS = 45
        self.PIN_O_S_WKE = 46
        self.PIN_O_N_WEN = 47
        self.PIN_O_N_TOF = 48
        self.PIN_O_N_TDS = 49
        self.PIN_O_N_LBR = 50
        self.PIN_O_N_AHO = 51
        self.PIN_O_N_AFI = 52
        self.PIN_O_N_AL1 = 53
        self.PIN_O_N_AL2 = 54
        self.PIN_O_N_AL3 = 55
        self.PIN_O_N_AL4 = 56
        self.PIN_O_N_AL5 = 57
        self.PIN_O_N_CID = 58
        self.PIN_O_N_CCH = 59
        self.PIN_O_N_CFI = 60
        self.PIN_O_N_LSE = 61
        self.PIN_O_N_UST = 62
        self.PIN_O_S_WAK = 63
        self.PIN_O_N_R1X = 64
        self.PIN_O_N_DTO = 65
        self.PIN_O_N_NMO = 66
        self.PIN_O_S_RNA = 67
        self.PIN_O_S_RNM = 68
        self.PIN_O_S_RNE = 69
        self.PIN_O_S_RN1 = 70
        self.PIN_O_S_RN4 = 71
        self.PIN_O_S_RN5 = 72
        self.PIN_O_S_RN6 = 73
        self.PIN_O_S_RN7 = 74
        self.PIN_O_S_RN8 = 75
        self.PIN_O_S_RN9 = 76
        self.PIN_O_N_AZO = 77
        self.PIN_O_N_AMA = 78
        self.PIN_O_N_UPD = 79
        self.PIN_O_AMX = 80

        ########################################################################################################
        #### Own written code can be placed after this commentblock . Do not change or delete commentblock! ####
        ###################################################################################################!!!##

        self.g_out_sbc = {}  # type: {int, object}
        self.in_pin_2_key = {str(self.PIN_I_N_AMP): 'amp',
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

        self.key_2_out_pin = {'version': self.PIN_O_S_VERSION,
                              'rbc': self.PIN_O_N_RBC,
                              'rbt': self.PIN_O_N_RBT,
                              'car': self.PIN_O_N_CAR,
                              'err': self.PIN_O_N_ERR,
                              'cbl': self.PIN_O_N_CBL,
                              'pha': self.PIN_O_N_PHA,
                              'tmp': self.PIN_O_N_TMP,
                              'dws': self.PIN_O_N_DWS,
                              'adi': self.PIN_O_N_ADI,
                              'uby': self.PIN_O_N_UBY,
                              'eto': self.PIN_O_N_ETO,
                              'wst': self.PIN_O_N_WST,
                              'nrg': self.PIN_O_NRG_JSON,
                              'fwv': self.PIN_O_S_FWV,
                              'sse': self.PIN_O_S_SSE,
                              'eca': self.PIN_O_N_ECA,
                              'ecr': self.PIN_O_N_ECR,
                              'ecd': self.PIN_O_N_ECD,
                              'ec4': self.PIN_O_N_EC4,
                              'ec5': self.PIN_O_N_EC5,
                              'ec6': self.PIN_O_N_EC6,
                              'ec7': self.PIN_O_N_EC7,
                              'ec8': self.PIN_O_N_EC8,
                              'ec9': self.PIN_O_N_EC9,
                              'ec1': self.PIN_O_N_EC1,
                              'rca': self.PIN_O_S_RCA,
                              'rcr': self.PIN_O_S_RCR,
                              'rcd': self.PIN_O_S_RCD,
                              'rc4': self.PIN_O_S_RC4,
                              'rc5': self.PIN_O_S_RC5,
                              'rc6': self.PIN_O_S_RC6,
                              'rc7': self.PIN_O_S_RC7,
                              'rc8': self.PIN_O_S_RC8,
                              'rc9': self.PIN_O_S_RC9,
                              'rc1': self.PIN_O_S_RC1,
                              'tme': self.PIN_O_S_TME,
                              'amp': self.PIN_O_N_AMP,
                              'ast': self.PIN_O_N_AST,
                              'alw': self.PIN_O_N_ALW,
                              'stp': self.PIN_O_N_STP,
                              'dwo': self.PIN_O_N_DWO,
                              'wss': self.PIN_O_S_WSS,
                              'wke': self.PIN_O_S_WKE,
                              'wen': self.PIN_O_N_WEN,
                              'tof': self.PIN_O_N_TOF,
                              'tds': self.PIN_O_N_TDS,
                              'lbr': self.PIN_O_N_LBR,
                              'aho': self.PIN_O_N_AHO,
                              'afi': self.PIN_O_N_AFI,
                              'al1': self.PIN_O_N_AL1,
                              'al2': self.PIN_O_N_AL2,
                              'al3': self.PIN_O_N_AL3,
                              'al4': self.PIN_O_N_AL4,
                              'al5': self.PIN_O_N_AL5,
                              'cid': self.PIN_O_N_CID,
                              'cch': self.PIN_O_N_CCH,
                              'cfi': self.PIN_O_N_CFI,
                              'lse': self.PIN_O_N_LSE,
                              'ust': self.PIN_O_N_UST,
                              'wak': self.PIN_O_S_WAK,
                              'r1x': self.PIN_O_N_R1X,
                              'dto': self.PIN_O_N_DTO,
                              'nmo': self.PIN_O_N_NMO,
                              'rna': self.PIN_O_S_RNA,
                              'rnm': self.PIN_O_S_RNM,
                              'rne': self.PIN_O_S_RNE,
                              'rn1': self.PIN_O_S_RN1,
                              'rn4': self.PIN_O_S_RN4,
                              'rn5': self.PIN_O_S_RN5,
                              'rn6': self.PIN_O_S_RN6,
                              'rn7': self.PIN_O_S_RN7,
                              'rn8': self.PIN_O_S_RN8,
                              'rn9': self.PIN_O_S_RN9,
                              'azo': self.PIN_O_N_AZO,
                              'ama': self.PIN_O_N_AMA,
                              'upd': self.PIN_O_N_UPD,
                              'amx': self.PIN_O_AMX}

        self.unknown_keys = []  # keys not respected in by module but received from go.e
        self.api_v2 = False

    def set_output_value_sbc(self, pin, val):
        # type:  (int, any) -> None
        if pin in self.g_out_sbc:
            if self.g_out_sbc[pin] == val:
                print ("# SBC: pin " + str(pin) + " <- data not send / " + str(val).decode("utf-8"))
                return

        self._set_output_value(pin, val)
        self.g_out_sbc[pin] = val

    def set_val(self, key, val):
        # type: (str, object) -> str
        """
        Sends an HTTP GET request to a remote MQTT API with a specified key-value pair as payload,
        and reads and processes the JSON data returned by the server.

        :param key: The key part of the key-value pair that will be sent as payload.
        :type key: str or object convertible to str
        :param val: The value part of the key-value pair that will be sent as payload.
        :type val: str or object convertible to str
        :return: A dictionary containing the data returned from the server.
        :rtype: dict
        """
        api_url = str(self._get_input_value(self.PIN_I_S_IP))
        api_port = int(self._get_input_value(self.PIN_I_N_PORT))
        api_path = '/mqtt?payload={key}={val}'.format(key=str(key), val=str(val))
        data = self.__http_get(api_url, api_port, api_path)
        self.read_json(data['data'])
        return data

    def get_data(self):
        # type: () -> None
        api_url = str(self._get_input_value(self.PIN_I_S_IP))
        api_port = int(self._get_input_value(self.PIN_I_N_PORT))
        n_interval = self._get_input_value(self.PIN_I_N_INTERVAL)
        if self.api_v2:
            api_path = "/api/status"
        else:
            api_path = "/status"
        data = self.__http_get(api_url, api_port, api_path)

        if data['data']:
            self.read_json(data['data'])
            self.set_output_value_sbc(self.PIN_O_N_ONLINE, 1)
        else:
            self.DEBUG.add_message("Module ID {} : get_data : ".format(self._get_module_id(), "No data received"))
            self.set_output_value_sbc(self.PIN_O_N_ONLINE, 0)

        if n_interval > 0:
            if self.t:
                if self.t.is_alive():
                    self.t.cancel()
            self.t = threading.Timer(n_interval, self.get_data).start()

    def __http_get(self, api_url, api_port, api_path):
        # type: (str, int, str) -> str
        print("Entering __http_get(self, {}, {}, {})".format(api_url, api_port, api_path))
        http_client = httplib.HTTPConnection(api_url, int(api_port), timeout=5)

        data = {'data': "", 'status': -1}

        try:
            http_client.request("GET", api_path)
            response = http_client.getresponse()
            status = response.status
            data = {'data': response.read(), 'status': status}
            self.DEBUG.add_message("Module ID {} : __get_data : status {}".format(self._get_module_id(), str(status)))
        except Exception as e:
            self.DEBUG.add_exception("Module ID {} : __http_get : {}".format(self._get_module_id(), str(e)))
        finally:
            if http_client:
                http_client.close()

        return data

    # read light data from json
    def read_json(self, json_state):
        try:
            json_state = json.loads(json_state)
        except Exception as e:
            json_state = []
            self.DEBUG.add_exception("Module ID {} : read_json : {}".format(self._get_module_id(), str(e)))

        if not json_state:
            return

        no_data_key = []
        no_key = []

        # if key exists apply API-V1, otherwise V2
        if "version" in json_state:
            self.api_v2 = False
        else:
            self.api_v2 = True

        self.DEBUG.set_value("Mod.ID {} : API Ver".format(self._get_module_id()), str("V2" if self.api_v2 else "V1"))

        # check for unknown keys from go-e
        for key in json_state:
            if key not in self.key_2_out_pin:
                if key not in self.unknown_keys:
                    self.unknown_keys.append(key)

        if not self.unknown_keys:
            self.DEBUG.set_value("Mod.ID {} : Unknown keys".format(self._get_module_id()),
                                 "Received unknown keys '{}'".format(self.unknown_keys))

        # start processing
        for key, pin in self.key_2_out_pin.items():
            if key not in json_state:
                no_data_key.append(key)
                continue

            value = json_state[key]

            if not value:
                no_key.append(key)
                continue

            # process and scale float values by / 10
            if key in ['dwo', 'ec1', 'ec4', 'ec5', 'ec6', 'ec7', 'ec8', 'ec9', 'ecd', 'ecr', 'eca', 'eto']:
                value = float(value) / 10.0
                self.set_output_value_sbc(pin, value)

            # process plain int values
            elif key in ['upd', 'stp', 'alw', 'ast', 'amp', 'sse', 'amx', 'wst', 'uby', 'adi', 'tmp', 'pha', 'cbl',
                         'err', 'car', 'rbc']:
                value = int(value)
                self.set_output_value_sbc(pin, value)

            elif key is 'rbt':
                value = int(value) / 1000
                self.set_output_value_sbc(pin, value)

            elif key is 'dws':  # Beispiel: 100'000 bedeutet, 1'000'000 Ws (= 277Wh = 0.277kWh)
                value = int(value) / 60.0 / 60.0 / 1000.0  # Ws zu kWh
                if value < 0.0005:
                    value = 0.0
                self.set_output_value_sbc(pin, value)

            elif key is 'nrg':
                nrg_curr = (int(value[4]) + int(value[5]) + int(value[6])) / 10.0
                self.set_output_value_sbc(self.PIN_O_N_NRG_CURR, nrg_curr)
                try:
                    nrg_json = {
                        "V L1": value[0], "V L2": value[1], "V L3": value[2], "V N": value[3],
                        "A L1": value[4] / 10.0, "A L2": value[5] / 10.0,
                        "A L3": value[6] / 10.0, "kW L1": value[7] / 10.0,
                        "kW L2": value[8] / 10.0, "kW L3": value[9] / 10.0, "kW N": value[10] / 10.0,
                        "kW Sum": value[11] / 100.0,
                        "P% L1": value[12], "P% L2": value[13], "P% L3": value[14], "P% N": value[15]
                    }
                    self.set_output_value_sbc(self.PIN_O_NRG_JSON, json.dumps(nrg_json))
                except Exception as e:
                    self.DEBUG.add_exception("Module ID {}: read_json: Error compiling nrg_json '{}'".format(
                        self._get_module_id(), str(e)))

            # process string output
            else:
                if key == 'tme' and len(value) == 10:
                    value = "{}.{}.20{} {}:{}".format(value[0:2], value[2:4], value[4:6], value[6:8], value[8:10])

                self.set_output_value_sbc(pin, str(value))

        if no_data_key:
            self.DEBUG.set_value("Empty data",
                                 "Mod.ID {} : read_json : Empty data for '{}'".format(self._get_module_id(),
                                                                                      no_data_key))
        if no_key:
            self.DEBUG.set_value("No data",
                                 "Mod.ID {} : read_json : No data for '{}'".format(self._get_module_id(), no_key))

        return json.dumps(json_state)

    def on_init(self):
        self.DEBUG = self.FRAMEWORK.create_debug_section()

        interval = self._get_input_value(self.PIN_I_N_INTERVAL)  # type: int
        self.t = threading.Timer(interval, self.get_data)  # type: threading.Timer

        if interval > 0:
            self.get_data()

    def on_input_value(self, index, value):
        if (self.PIN_I_N_TRIGGER == index) and (value != 0):
            self.get_data()
        elif index == self.PIN_I_N_INTERVAL:
            if self.t:
                if self.t.is_alive():
                    self.t.cancel()
            if value > 0:
                self.get_data()
        else:
            if str(index) in self.in_pin_2_key:
                s_key = self.in_pin_2_key[str(index)]
                if s_key == "lbr":
                    self.set_val(s_key, str(int(value) * 255 / 100))
                elif s_key == "dwo":
                    self.set_val(s_key, str(float(value) * 10))
                else:
                    self.set_val(s_key, str(value))
