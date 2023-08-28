from scapy.all import *
import argparse
from Crypto.Cipher import AES
import base64
import hashlib
from urllib.parse import unquote

parser = argparse.ArgumentParser(description='Decrypt TrevorC2 traffic from a pcap')
parser.add_argument('pcap', metavar='pcap', type=str, help='PCAP file')
parser.add_argument('-k', metavar='key', type=str, help='key (default is "Tr3v0rC2R0x@nd1s@w350m3#TrevorForget")', default="Tr3v0rC2R0x@nd1s@w350m3#TrevorForget")
args = parser.parse_args()

pcap = rdpcap(args.pcap)
key = args.k

@staticmethod
def _unpad(s):
    return s[:-ord(s[len(s)-1:])]

def str_to_bytes(data):
        u_type = type(b''.decode('utf8'))
        if isinstance(data, u_type):
            return data.encode('utf8')
        return data

def decrypt(key, enc):
        key = hashlib.sha256(str_to_bytes(key)).digest()
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return _unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

for pkt in pcap:
    #get the commands being sent to the compromised host. Will be in html format </script><!-- oldcss=... --></body></html>
    try:
        if pkt[TCP].sport == 80:
            if b"<!-- oldcss=" in pkt[Raw].load:
                #grab the command
                command = pkt[Raw].load.split(b"<!-- oldcss=")[1].split(b" --></body>")[0]
                #decrypt the command
                try:
                    decrypted = decrypt(key, command)
                    #print the decrypted command
                    print("Decrypted command: " + str(decrypted))
                except Exception as e:
                    print(e)
                    pass
    except:
        pass

    #go through and look for HTTP(s) GET requests containing /images?guid=
    try:
        if pkt[TCP].dport == 80:
            if b"GET /images?guid=" in pkt[Raw].load:
                #grab the guid
                guid = pkt[Raw].load.split(b"guid=")[1].split(b" ")[0]
                #url decode the guid
                guid = unquote(guid)
                try:
                    guid = base64.b64decode(guid)
                    #decrypt the guid
                    decrypted = decrypt(key, guid)
                    #print the decrypted guid
                    print("Decrypted response: " + str(decrypted))
                except Exception as e:
                    print(e)
                    pass
    except:
        pass

