set(GDAL_EXTRA_DRIVERS_SOURCES
    entrypoint.cpp
    ogr_geo_utils.cpp
    bna/ogrbnadatasource.cpp
    bna/ogrbnadriver.cpp
    bna/ogrbnalayer.cpp
    bna/ogrbnaparser.cpp
    aeronavfaa/ograeronavfaadriver.cpp
    aeronavfaa/ograeronavfaadatasource.cpp
    aeronavfaa/ograeronavfaalayer.cpp
    htf/ogrhtfdriver.cpp
    htf/ogrhtfdatasource.cpp
    htf/ogrhtflayer.cpp
    openair/ogropenairdriver.cpp
    openair/ogropenairdatasource.cpp
    openair/ogropenairlayer.cpp
    openair/ogropenairlabellayer.cpp
    segukooa/ogrsegukooadriver.cpp
    segukooa/ogrsegukooadatasource.cpp
    segukooa/ogrsegukooalayer.cpp
    segy/ogrsegydriver.cpp
    segy/ogrsegydatasource.cpp
    segy/ogrsegylayer.cpp
)

add_library(gdal_legacy SHARED ${GDAL_EXTRA_DRIVERS_SOURCES})

set_target_properties(gdal_legacy PROPERTIES PREFIX "")
set_target_properties(gdal_legacy PROPERTIES OUTPUT_NAME "gdal_LEGACY")

target_include_directories(gdal_legacy PRIVATE ${CMAKE_SOURCE_DIR}/src ${GDAL_INCLUDE_DIR})
target_link_libraries(gdal_legacy PUBLIC ${GDAL_LIBRARY})

install(TARGETS gdal_legacy DESTINATION lib/gdalplugins)
