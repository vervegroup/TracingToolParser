import json
import pathlib
import csv
import pandas as pd
currentPath = pathlib.Path(__file__).parent.resolve()
json_filename = 'tracingResult.json'
json_filepath = str(currentPath) + '/' + json_filename


with open(json_filepath, encoding='utf-8') as f:
    json_data = json.load(f)

for (k, v) in json_data.items():
    if k == "data":
        final_json = list(v)

table={'App Name':[], "Inventory Type":[], "Bundle":[], 'Publisher Name':[], 'Publisher Id':[], "Content Genre":[], "Device Type":[]}

for i in final_json:
    try:
        bid_req=json.loads(i['spans'][3]['logs'][0]['fields'][1]['value'])
        if "app" in bid_req:
            inventorytype="In App"
            appname = bid_req["app"]["name"]
            bundle= bid_req["app"]["bundle"] 
            PublisherName= bid_req["app"]["publisher"]["name"]        
            Publisherid= bid_req["app"]["publisher"]["id"]          
            DeviceType=bid_req["device"]["devicetype"]           
            if "content" in bid_req["app"]:
                if "genre" in bid_req["app"]["content"]:
                    contentGenre=bid_req["app"]["content"]["genre"]                   
                else:
                    contentGenre="No genre passed by the publisher"            
            else:
                contentGenre="content object missing"
            table["App Name"].append(appname)
            table["Inventory Type"].append(inventorytype)
            table["Bundle"].append(bundle)   
            table["Publisher Name"].append(PublisherName)
            table["Publisher Id"].append(Publisherid)
            table["Content Genre"].append(contentGenre)
            table["Device Type"].append(DeviceType)
        if "site" in bid_req:
            # print("hello")
            inventorytype="Mobile Web"
            appname = bid_req["site"]["name"]
            bundle= bid_req["site"]["domain"]
            PublisherName= bid_req["site"]["publisher"]["name"]
            Publisherid= bid_req["site"]["publisher"]["id"]
            DeviceType=bid_req["device"]["devicetype"]
            if "content" in bid_req["site"]:
                if "genre" in bid_req["site"]["content"]:
                    contentGenre=bid_req["site"]["content"]["genre"]
                else:
                    contentGenre="No genre passed by the publisher"
            else:
                contentGenre="content object missing"
            table["App Name"].append(appname)
            table["Inventory Type"].append(inventorytype)
            table["Bundle"].append(bundle)   
            table["Publisher Name"].append(PublisherName)
            table["Publisher Id"].append(Publisherid)
            table["Content Genre"].append(contentGenre)
            table["Device Type"].append(DeviceType)
            # print(bundle)
            # print(PublisherName)
            # print(Publisherid)
            # print(appname)
    except Exception:
        print("no bid req sent to a DSP (ATC)")  

new= pd.DataFrame(table)
new.to_csv('Tracing Configuration.csv', index=False)  
        
     
     
   


