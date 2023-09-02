# coding: UTF-8

import unittest
import logging
import json
import time
from mock import patch, MagicMock

################################
# get the code
with open('./framework_helper.py', 'r') as f1, open('../src/14105_go-eCharger (14105).py', 'r') as f2:
    framework_code = f1.read()
    debug_code = f2.read()

exec (framework_code + debug_code)


################################
# unit tests
class RequirementsVerification(unittest.TestCase):

    cred = 0
    obj = 0

    def setUp(self):
        logging.basicConfig()
        self.logger = logging.getLogger("UnitTests")
        self.logger.setLevel(logging.DEBUG)

        self.logger.info("###setUp")

        with open("credentials.txt") as f:
            self.cred = json.load(f)

        self.obj = Go_eCharger_14105_14105(0)
        self.obj.debug_input_value[self.obj.PIN_I_S_IP] = self.cred["PIN_I_S_IP"]
        self.obj.debug_input_value[self.obj.PIN_I_N_PORT] = self.cred["PIN_I_N_PORT"]
        self.obj.debug_input_value[self.obj.PIN_I_N_INTERVAL] = 0

        self.obj.on_init()

    def test_set_output_value_sbc__pin_exists_val_not_equal(self):
        self.obj.g_out_sbc = {1: 0}  # Set an existing pin with a different value
        with patch('__builtin__.print') as mock_print:
            self.obj.set_output_value_sbc(1, 1)
            self.assertEqual(mock_print.call_count, 0)  # Ensure print is not called
            self.assertEqual(self.obj.g_out_sbc[1], 1)  # Ensure pin value is updated

    def test_set_output_value_sbc__pin_exists_val_equal(self):
        self.obj.g_out_sbc = {2: 3}  # Set an existing pin with the same value
        self.obj.debug_output_value[2] = 1
        with patch('__builtin__.print') as mock_print:
            self.obj.set_output_value_sbc(2, 3)
            self.assertTrue(self.obj.debug_output_value[2] == 1)
            # mock_print.assert_called_once_with("# SBC: pin 2 <- data not send / 3".decode("utf-8"))
            self.assertEqual(self.obj.g_out_sbc[2], 3)  # Ensure pin value is not updated

    def test_set_output_value_sbc__pin_not_exists(self):
        self.obj.g_out_sbc = {}  # Set an empty dictionary
        with patch.object(self.obj, '_set_output_value') as mock_set_output:
            self.obj.set_output_value_sbc(3, 4)
            mock_set_output.assert_called_once_with(3, 4)  # Ensure _set_output_value is called
            self.assertEqual(self.obj.g_out_sbc[3], 4)  # Ensure pin value is updated

    def test_trigger(self):
        self.logger.info("###test_trigger")
        self.obj.on_input_value(self.obj.PIN_I_N_TRIGGER, 1)
        self.assertTrue(self.obj.debug_output_value[self.obj.PIN_O_N_ONLINE])

    def test_tme(self):
        self.logger.info("###test_tme")
        js = '{"tme":"0104191236"}'
        self.obj.read_json(js)
        self.assertEqual("01.04.2019 12:36", self.obj.debug_output_value[self.obj.PIN_O_S_TME])

    def test_nrg(self):
        self.logger.info("###test_nrg")
        js = '{"nrg": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]}'

        self.obj.read_json(js)
        self.assertEqual(self.obj.debug_output_value[self.obj.PIN_O_N_NRG_CURR], 1.5)
        self.assertTrue('"V N": 3' in self.obj.debug_output_value[self.obj.PIN_O_NRG_JSON])
        self.assertTrue('"kW L3": 0.9' in self.obj.debug_output_value[self.obj.PIN_O_NRG_JSON])
        self.assertTrue('"V L2": 1' in self.obj.debug_output_value[self.obj.PIN_O_NRG_JSON])
        self.assertTrue('"kW Sum": 0.11' in self.obj.debug_output_value[self.obj.PIN_O_NRG_JSON])

    def test_interval(self):
        self.logger.info("###test_interval")
        self.obj.g_out_sbc[self.obj.PIN_O_N_ONLINE] = False
        self.obj.debug_input_value[self.obj.PIN_I_N_INTERVAL] = 2
        self.obj.on_input_value(self.obj.PIN_I_N_INTERVAL, 2)
        self.assertTrue(self.obj.g_out_sbc[self.obj.PIN_O_N_ONLINE], "1")

        self.logger.info("test 2 cylce")
        self.obj.g_out_sbc[self.obj.PIN_O_N_ONLINE] = False
        time.sleep(3)
        self.assertTrue(self.obj.g_out_sbc[self.obj.PIN_O_N_ONLINE], "2a")

        self.obj.g_out_sbc[self.obj.PIN_O_N_ONLINE] = False
        time.sleep(3)
        self.assertTrue(self.obj.g_out_sbc[self.obj.PIN_O_N_ONLINE], "2b")

        self.logger.info("test stop cycle")
        self.obj.debug_input_value[self.obj.PIN_I_N_INTERVAL] = 0
        self.obj.on_input_value(self.obj.PIN_I_N_INTERVAL, 0)
        time.sleep(3)
        self.obj.g_out_sbc[self.obj.PIN_O_N_ONLINE] = False
        time.sleep(3)

        self.assertFalse(self.obj.g_out_sbc[self.obj.PIN_O_N_ONLINE], "3")

    def test_no_connection(self):
        self.logger.info("###test_no_connection")
        self.obj.debug_input_value[self.obj.PIN_I_N_PORT] = 1234
        self.obj.debug_input_value[self.obj.PIN_I_N_INTERVAL] = 0
        self.obj.get_data()
        self.assertFalse(self.obj.debug_output_value[self.obj.PIN_O_N_ONLINE])


if __name__ == '__main__':
    unittest.main()
