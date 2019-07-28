import xmltodict
import pprint
import json


def xml_to_json():
    with open("./image_data/1.xml", 'r', encoding='utf8') as f:
        xmlString = f.read()

    print("xml input (xml_to_json.xml):")
    print(xmlString)

    jsonString = json.dumps(xmltodict.parse(xmlString), indent=4, ensure_ascii=False)

    print("\nJSON output(output.json):")
    print(jsonString)

    with open("./xml_to_json.json", 'w', encoding='utf8') as f:
        f.write(jsonString)


