# RDF Library

__version__ = "2.1.0"

import sys
# TODO: what version of python does rdflib require??
assert sys.version_info >= (2,2,0), "rdflib requires python 2.2 or higher"
del sys

from rdflib.Triple import Triple

from rdflib.URIRef import URIRef
from rdflib.BNode import BNode
from rdflib.Literal import Literal
from rdflib.Namespace import Namespace

from rdflib.Graph import Graph
