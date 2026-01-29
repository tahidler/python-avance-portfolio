from typing import List, Dict, Any
import xml.etree.ElementTree as ET


def _element_to_dict(elem: ET.Element) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    for child in list(elem):
        text = (child.text or "").strip()
        data[child.tag] = text
    return data


def parse_xml(path: str) -> List[Dict[str, Any]]:
    """Parser un XML simple en une liste de dictionnaires."""
    tree = ET.parse(path)
    root = tree.getroot()
    return [_element_to_dict(child) for child in list(root)]
