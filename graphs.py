import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('test.csv')

keys_ipv6 = ["IPv6", "UDP", "QUIC", "TCP", "TLS over TCP"]
keys_ipv4 = ["IPv4", "UDP", "DNS", "TCP", "TLS over TCP"]
data_ipv6 = []
data_ipv4 = []

ipv = 6

for idx in df.index:
    if df["Protocol"][idx] == "Internet Protocol Version 6":
        data_ipv6.append(df["Percent Packets"][idx])
    elif df["Protocol"][idx] == "User Datagram Protocol":
        if ipv == 6:
            data_ipv6.append(df["Percent Packets"][idx])
        elif ipv == 4:
             data_ipv4.append(df["Percent Packets"][idx])
    elif df["Protocol"][idx] == "QUIC IETF":
        data_ipv6.append(df["Percent Packets"][idx])
    elif df["Protocol"][idx] == "Transmission Control Protocol":
        if ipv == 6:
            data_ipv6.append(df["Percent Packets"][idx])
        elif ipv == 4:
            data_ipv4.append(df["Percent Packets"][idx])
    elif df["Protocol"][idx] == "Transport Layer Security":
        if ipv == 6:
            data_ipv6.append(df["Percent Packets"][idx])
        else:
            data_ipv4.append(df["Percent Packets"][idx])
    elif df["Protocol"][idx] == "Internet Protocol Version 4":
        ipv = 4
        data_ipv4.append(df["Percent Packets"][idx])
    elif df["Protocol"][idx] == "Domain Name System":
        data_ipv4.append(df["Percent Packets"][idx])
    
print(data_ipv6)
print(data_ipv4)

print(len(data_ipv4))
print(len(keys_ipv4))



#X = ["IPv6", "IPv4"]
# ind = np.arange(2)
# width = 0.2

# bar1 = plt.bar(ind, [data_ipv6[1], data_ipv4[1]], width, color = 'r') 
# bar2 = plt.bar(ind+width, [data_ipv6[2], data_ipv4[2]], width, color='g') 
# bar3 = plt.bar(ind+width*2, [data_ipv6[3], data_ipv4[3]], width, color='b') 
# bar4 = plt.bar(ind+width*3, [data_ipv6[4], data_ipv4[4]], width, color='y') 


# plt.xlabel("Dates") 
# plt.ylabel('Scores') 
# plt.title("Players Score") 

# plt.show() 

fig = plt.figure()
plt.bar(keys_ipv6[1:], data_ipv6[1:], color ='maroon', width = 0.4)
plt.xlabel("IPv6")
plt.ylabel("Percentage of packets")
plt.title("IPv6 protocol distribution when uploading a file")
plt.show()


# fig = plt.figure()
# plt.bar(keys_ipv4[1:], data_ipv4[1:], color ='maroon', width = 0.4)
# plt.xlabel("IPv4")
# plt.ylabel("Percentage of packets")
# plt.title("IPv4 protocol distribution when uploading a file")
# plt.show()


# fig = plt.figure(figsize=(10, 7))
# lab = ["IPv6", "IPv4"]
# plt.pie([data_ipv6[0], data_ipv4[0]], labels=lab)
# plt.title("IPv4 vs IPv6 use on Google Drive")
# # show plot
# plt.show()









