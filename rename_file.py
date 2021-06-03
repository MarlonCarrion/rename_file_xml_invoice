import os
import xml.etree.ElementTree as ET

path = 'D:/Escritorio/ORTIZ CORNEJO JOSE PATRICIO/2021/Archivo Digital/05 Mayo/Factura xml/'

with os.scandir(path) as ficheros:
    for fichero in ficheros:
        name_file = fichero.name
        tree = ET.parse(path+name_file)
        root = tree.getroot()
        for child in root:
            if child.tag =='comprobante':
                comprobante = child.text
                c = ET.fromstring(comprobante)
                for x in range(len(c)):
                    if c[x].tag == 'infoTributaria':
                        for i in c[x]:
                            if i.tag == 'secuencial':
                                new = path+i.text
                                old = path+name_file
                                os.renames(old, new)