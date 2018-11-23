#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Compile Python sources from your own ASN.1 definitions
python ./tools/pycrate_asn1compile.py -i ./pycrate_asn1dir/3GPP_EUTRAN_MINIMAL/ -o lte_asn -j
"""

from pycrate_asn1dir import RRCLTE
import lte_asn
from binascii import unhexlify, hexlify


def decode_own_definition():
    # List all (one) definitions
    # ['PCCH-Message-Definition'] - object will have all '-' replaced with '_'
    # print(list(lte_asn.GLOBAL.MOD.keys()))

    # List all PDUs from definitions
    # print(dir(lte_asn.PCCH_Message_Definition))

    pdu = lte_asn.PCCH_Message_Definition.PCCH_Message
    pdu.from_uper(unhexlify('0b00'))
    print(pdu.to_asn1())


def decode_rrc_definition():
    pdu = RRCLTE.EUTRA_RRC_Definitions.RRCConnectionSetup
    pdu.from_uper(unhexlify('0080A000000100'))
    print(pdu.to_asn1())


def encode_own_definition():
    pdu = lte_asn.PCCH_Message_Definition.PCCH_Message

    # List internals of pdu and their types - here there is one 'message' of type PCCH-MessageType
    # {
    # message: <message ([PCCH-MessageType] CHOICE)>
    # }
    print(pdu._cont)

    # List internals of pdu and their types - here there is one 'message' of type PCCH-MessageType
    # {'name': 'PCCH-Message', 'mode': 'TYPE', 'tag': None, 'typeref': None, 'tr': None, 'param': False, 'parent': None, 'opt': False, 'def': None, 'uniq': False, 'group': None, 'cont': {
    # message: <message ([PCCH-MessageType] CHOICE)>
    # }, 'root': ['message'], 'ext': None, 'val': None, 'const_val': None, 'const_tab': None, 'root_mand': ['message']}
    print(pdu.get_internals())

    val = {'message': ('c1', ('paging', {'etws-Indication': 'true'}))}
    pdu.set_val(val)

    # Print encoded (UPER) payload
    print(hexlify(pdu.to_uper()))


if __name__ == '__main__':
    decode_own_definition()
    decode_rrc_definition()

    encode_own_definition()
