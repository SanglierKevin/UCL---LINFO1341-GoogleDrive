import pyshark
import asyncio
import os
import subprocess

traces_directory = "Traces_Shortened_Decrypted/"

for filename in os.listdir(traces_directory):
    trace = os.path.join(traces_directory, filename)
    if os.path.isfile(trace):
        print(filename)
        with pyshark.FileCapture(input_file=trace, display_filter="dns") as capture:
            for packet in capture:
                #print(packet.dns.field_names)
                dnslayer = packet.dns
                if dnslayer.flags_response != '0' and dnslayer.count_answers > '0': # check si la dns est une réponse à une query et si elle contient une réponse
                    print("\n\n\n\n\n\n")
                    print(dnslayer.resp_name)
                    if 'dns.a' in dnslayer._all_fields.keys() and 'dns.resp.ttl' in dnslayer._all_fields.keys(): # check si c'est une requête IPv4 et si on a reçu un ttl
                        print("IPv4 : ")
                        print("\t" + str(dnslayer.resp_ttl))
                        print("\t" + str(dnslayer._all_fields.keys()))
                        print("\t" + str(dnslayer.field_names))
                    #print(dnslayer.resp_ttl)
                    #print(dnslayer.field_names)
                    #print(dnslayer)