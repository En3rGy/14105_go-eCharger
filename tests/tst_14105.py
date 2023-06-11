# coding: UTF-8

import unittest
import logging
import json
import time


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
    tst = 0

    def setUp(self):
        logging.basicConfig()
        self.logger = logging.getLogger("UnitTests")
        self.logger.setLevel(logging.DEBUG)

        self.logger.info("###setUp")

        with open("credentials.txt") as f:
            self.cred = json.load(f)

        self.tst = Go_eCharger_14105_14105(0)
        self.tst.on_init()

        self.tst.debug_input_value[self.tst.PIN_I_S_IP] = self.cred["PIN_I_S_IP"]
        self.tst.debug_input_value[self.tst.PIN_I_N_PORT] = self.cred["PIN_I_N_PORT"]

    def test_trigger(self):
        self.logger.info("###test_trigger")
        self.tst.on_input_value(self.tst.PIN_I_N_TRIGGER, 1)
        self.assertTrue(True)

    def test_tme(self):
        self.logger.info("###test_tme")
        self.tst.on_init()
        js = '{"tme":"0104191236"}'
        self.tst.read_json(js)
        self.assertEqual("01.04.2019 12:36", self.tst.debug_output_value[self.tst.PIN_O_S_TME])

    def test_interval(self):
        self.logger.info("###test_interval")
        self.tst.on_init()
        self.tst.debug_get_data = False
        self.tst.debug_input_value[self.tst.PIN_I_N_INTERVAL] = 2
        self.tst.on_input_value(self.tst.PIN_I_N_INTERVAL, 2)
        self.assertTrue(self.tst.debug_get_data, "1")

        self.logger.info("test 2 cylce")
        self.tst.debug_get_data = False
        time.sleep(3)
        self.assertTrue(self.tst.debug_get_data, "2a")

        self.tst.debug_get_data = False
        time.sleep(3)
        self.assertTrue(self.tst.debug_get_data, "2b")

        self.logger.info("test stop cycle")
        self.tst.debug_input_value[self.tst.PIN_I_N_INTERVAL] = 0
        self.tst.on_input_value(self.tst.PIN_I_N_INTERVAL, 0)
        time.sleep(3)
        self.tst.debug_get_data = False
        time.sleep(3)

        self.assertFalse(self.tst.debug_get_data, "3")


if __name__ == '__main__':
    unittest.main()
