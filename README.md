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

