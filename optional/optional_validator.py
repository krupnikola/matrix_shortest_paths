import xmlschema


def is_valid_xml(xml_file):
    schema = xmlschema.XMLSchema('resources/map_schema.xsd')
    return schema.is_valid(xml_file)