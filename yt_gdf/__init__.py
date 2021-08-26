from .data_structures import GDFDataset, GDFGrid, GDFHierarchy
from .fields import GDFFieldInfo
from .io import IOHandlerGDFHDF5
from yt.utilities.object_registries import output_type_registry

add_gdf_field = GDFFieldInfo.add_field

output_type_registry["GDFDataset"] = GDFDataset
