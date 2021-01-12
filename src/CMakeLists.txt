set(GDAL_EXTRA_DRIVERS_SOURCES
    entrypoint.cpp
    bna/ogrbnadatasource.cpp
    bna/ogrbnadriver.cpp
    bna/ogrbnalayer.cpp
    bna/ogrbnaparser.cpp
)

add_library(gdal_legacy SHARED ${GDAL_EXTRA_DRIVERS_SOURCES})

set_target_properties(gdal_legacy PROPERTIES PREFIX "")
set_target_properties(gdal_legacy PROPERTIES OUTPUT_NAME "gdal_LEGACY")

target_include_directories(gdal_legacy PRIVATE ${GDAL_INCLUDE_DIR})
target_link_libraries(gdal_legacy PUBLIC ${GDAL_LIBRARY})

install(TARGETS gdal_legacy DESTINATION lib/gdalplugins)
