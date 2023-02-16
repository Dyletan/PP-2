import json
f = open("C:\PP 2\lab_4\Json\sample_data.json")
dic = json.load(f)
print("Interface Status")
print("================================================================================")
print("DN" + ' '*46+"Description"+' '*10+"Speed   MTU  ")
print('-'*47+" "+'-'*20+' '+"-"*7+' '+"-"*4)
for x in dic["imdata"]:
    for key, value in x.items():
        print('{:47} {:20} {:7} {:4}'.format(value["attributes"]["dn"], value["attributes"]["descr"], value["attributes"]["speed"], value["attributes"]["mtu"]))
        