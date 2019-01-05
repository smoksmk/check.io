#!/usr/bin/env python
# -*- coding: utf-8 -*-
from twisted.internet import reactor
from twisted.internet.protocol import ServerFactory
from twisted.protocols.basic import LineOnlyReceiver

import logging
logger = logging.getLogger('main')

class ChatProtocol(LineOnlyReceiver):
    name = ""

    def getName(self):
        if self.name != "":
            return self.name
        return self.transport.getPeer().host

    def connectionMade(self):
        logger.info("New connection from " + self.getName())
        self.sendLine("Welcome to my my chat serverbot.")
        self.sendLine("Send '/name [new name]' to change your name.")
        self.sendLine("Send '/exit' to quit.")
        self.factory.sendMessageToAllClients(self.getName() + " has joined the party.")
        self.factory.clientProtocols.append(self)

    def connectionLost(self, reason):
        logger.info("Lost connection from " + self.getName())
        self.factory.clientProtocols.remove(self)
        self.factory.sendMessageToAllClients(self.getName() + " has disconnected.")

    def lineReceived(self, line):
        logger.info(self.getName() + ": " + line)

        if line[:5] == "/name":
            oldName = self.getName()
            self.name = line[5:].strip()
            self.factory.sendMessageToAllClients(oldName + " changed name to "+self.getName())
        elif line == "/exit":
            self.transport.loseConnection()
        else:
            self.factory.sendMessageToAllClients(self.getName() + ": " + line)

    def sendLine(self, line):
        self.transport.write(line + "\r\n")



class ChatProtocolFactory(ServerFactory):
    protocol = ChatProtocol
    def __init__(self):
        self.clientProtocols = []

    def sendMessageToAllClients(self, mesg):
        for client in self.clientProtocols:
            client.sendLine(mesg)


if __name__ == '__main__':
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s [%(levelname)s] %(message)s',
        '%H:%M:%S'
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.info('Run')
    factory = ChatProtocolFactory()

    reactor.listenTCP(12345, factory)
    reactor.run()