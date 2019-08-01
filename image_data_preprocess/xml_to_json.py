import xmltodict
import pprint
import json


def xml_to_json():

    for i in ['1','2','4','5','9','11','17','18']:

        with open("./art/"+i+".xml", 'r', encoding='utf8') as f:
            xmlString = f.read()

        print("xml input (xml_to_json.xml):")
        print(xmlString)

        jsonString = json.dumps(xmltodict.parse(xmlString), indent=4, ensure_ascii=False)

        print("\nJSON output(output.json):")
        print(jsonString)

        with open("./art_json/"+i+".json", 'w', encoding='utf8') as f:
            f.write(jsonString)


xml_to_json()
