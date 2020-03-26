import os
from pathlib import Path
os.environ['XML_DEBUG_CATALOG'] = 'TRUE'
from lxml import etree

gmi_schema = Path(__file__).parent / 'gmd' / 'iso19115' / 'gmi' / '1.0' / 'gmi.xsd'
catalog = Path(__file__).parent / 'gmd' / 'catalog.xml'

os.environ['XML_CATALOG_FILES'] = str(catalog)
xmlschema_doc = etree.parse(str(gmi_schema))
xmlschema = etree.XMLSchema(xmlschema_doc)


def assert_valid_inspire_metadata(my_xml_file):
    doc = etree.parse(my_xml_file)
    xmlschema.assertValid(doc)
