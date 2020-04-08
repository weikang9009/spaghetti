__version__ = "1.4.2.post2"
"""
:mod:`spaghetti` --- Spatial Graphs: Networks, Topology, & Inference
====================================================================

"""
from .network import Network, PointPattern, SimulatedPointPattern
from .network import extract_component, spanning_tree
from .network import element_as_gdf, regular_lattice
