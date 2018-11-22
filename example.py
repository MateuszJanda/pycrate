#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Compile Python sources from your own ASN.1 definitions
python ./tools/pycrate_asn1compile.py -i ./pycrate_asn1dir/3GPP_EUTRAN_MINIMAL/ -o lte_asn -j
"""

import ltemini
from binascii import unhexlify, hexlify


def decode_own_payload():
    # List all (one) definitions
    # ['PCCH-Message-Definition'] - object will have all '-' replaced with '_'
    # print(list(ltemini.GLOBAL.MOD.keys()))

    # List all PDUs from definitions
    # print(dir(ltemini.PCCH_Message_Definition))

    pdu = lte_asn.PCCH_Message_Definition.PCCH_Message
    pdu.from_uper(unhexlify('0b00'))
    print(pdu.to_asn1())


if __name__ == '__main__':
    decode_own_payload()
