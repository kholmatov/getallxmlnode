#!/usr/bin/python
# -*- coding: utf-8 -*-
from lxml import etree
import sys,re, json
xml_file = sys.argv[1]
parser = etree.XMLParser(remove_blank_text=True)
tree = etree.parse(xml_file, parser)
root = tree.getroot()
xmlArray = []
xmlAttr = []
for child in root.iter():
    #print(tree.getpath(child))
    myNode = re.sub("[\[\d*\]]", '', tree.getpath(child))
    if myNode not in xmlArray:
        xmlArray.append(myNode)
        if child.keys():
                for attr in child.keys():
                    xmlAttr.append(str(myNode)+'/@'+str(attr))
myXml = {}
myXml['node'] = xmlArray
myXml['attr'] = xmlAttr
print(json.dumps(myXml,  sort_keys=True,indent=4, separators=(',', ': ')))
