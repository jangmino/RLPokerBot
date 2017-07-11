# Heads Up Nonlimited Texas Holdem Environment for ACPC

import unittest
import ACPCCommunication
import re

class ACPCEnvironment:
    def __init__(self):
        """
        Environment for ACPC
        """

        self.name = "ACPC Environment"
        self.communication = ACPCCommunication.ACPCCommunication()


    def step(self, agent, action):
        """
        
        :param agent: 
        :param action: 
        :return: 
        """

        reward = []
        nextstate = []
        return reward, nextstate

    def connect(self, host, port):
        self.communication.connect(host, port)


    def get_next_situation(self):
        while True:
            msg = self.communication.get_line()

            print("Received acpc dealer message:" + msg)

            # TODO: interpreting message

    def play_action(self, action):
        message = ''

        #TODO: Fill the message
        self.communication.send_line(message)

    def interpret_message(self, message):
        """
        Interpret the message...
        example
            "MATCHSTATE:0:0:r12017:5d5c|"
        :param message: 
        :return: 
        """

    @staticmethod
    def makeGameStateFromMessage(message):
        re.compile(r'MATCHSTATE:(\d+):(\d+):')




class testUnit(unittest.TestCase):
    '''
    @brief test case using uniitest.TestCase
    '''
    def setUp(self):
        ''' @brief this method is called before every test methods '''
        pass
    def tearDown(self):
        ''' @brief this method is called after every test methods '''
        pass
    def test001_init(self):
        my = ACPCEnvironment()
        my.connect('localhost', 16177)
        my.communication.handshake()
        my.get_next_situation()
        self.assertTrue(True)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testUnit)
    unittest.TextTestRunner(verbosity=2).run(suite)