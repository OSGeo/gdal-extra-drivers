gdal-extra-drivers
==================

This repository contains legacy drivers for [GDAL/OGR](https://gdal.org), which
are built as a GDAL plugin.
They used to be included in the GDAL core library in versions prior to 3.3, but
they have been removed due to lack of interest to maintain them and because of
their marginal values for the majority of users.

They are known to work with GDAL 3.3. Compatibility with older or later versions
is not guaranteed.

This repository is *not* maintained. Users are on their own, unless someone
steps up to maintain it.

### Included drivers

* [AeronavFAA](doc/aeronavfaa.rst)
* [BNA](doc/bna.rst)
* [BPG](doc/bpg.rst) (not included in build system)
* [E00Grid](doc/e00grid.rst)
* [EPSILON](doc/epsilon.rst) (not included in build system)
* [HTF](doc/htf.rst)
* [IGNFHeightASCIIGrid](doc/ignfheightasciigrid.rst)
* [NTv1](doc/ntv1.rst)
* [OpenAir](doc/openair.rst)
* [SEGUKOOA](doc/segukooa.rst)
* [SEGY](doc/segy.rst)
* [SUA](doc/sua.rst)
* [XPlane](doc/xplane.rst)

### Other drivers

The following drivers, removed in GDAL 3.5, are available in the ``not_integrated_in_build``
directory. As the name indicates it, you will have some work to get them built.

* [ARCGen](not_integrated_in_build/arcgen/arcgen.rst)
* [ArcObjects](not_integrated_in_build/arcobjects/ao.rst)
* [Cloudant](not_integrated_in_build/cloudant/cloudant.rst)
* [CouchDB](not_integrated_in_build/couchdb/couchdb.rst)
* [DB2](not_integrated_in_build/db2/db2.rst)
* [DODS](not_integrated_in_build/dods/dods.rst)
* [FME](not_integrated_in_build/fme/fme.rst)
* [FujiBAS](not_integrated_in_build/fujibas/fujibas.rst)
* [Geomedia](not_integrated_in_build/geomedia/geomedia.rst)
* [GMT raster](not_integrated_in_build/gmt_raster/gmt.rst)
* [GTM](not_integrated_in_build/gtm/gtm.rst)
* [IDA](not_integrated_in_build/ida/ida.rst)
* [Ingres](not_integrated_in_build/ingres/ingres.rst)
* [Intergraph raster](not_integrated_in_build/ingr/intergraphraster.rst)
* [Jasper JPEG2000](not_integrated_in_build/jpeg2000/jpeg2000.rst)
* [JpegLS](not_integrated_in_build/jpegls/jpegls.rst)
* [MDB](not_integrated_in_build/mdb/mdb.rst)
* [MongoDB (pre v3)](not_integrated_in_build/mongodb_old/mongodb.rst)
* [MrSID Lidar](not_integrated_in_build/mrsid_lidar/mg4lidar.rst)
* [OGR_DODS](not_integrated_in_build/ogr_dods/dods.rst)
* [Rasdaman](not_integrated_in_build/rasdaman/rasdaman.rst)
* REC
* [WALK](not_integrated_in_build/walk/walk.rst)

### Build requirements

GDAL 3.3 headers and development library.

### How to build

```shell
mkdir _build
cd _build
cmake ..
make install
```

A gdal_LEGACY.so plugin is installed in ${PREFIX}/lib/gdalplugins

### License

X/MIT. See [LICENSE.TXT](LICENSE.TXT)

