cmake_minimum_required(VERSION 3.16...3.27)

#----------------------------------------------------------------------------
# Project definition
#----------------------------------------------------------------------------

project(Geantpy)

#----------------------------------------------------------------------------
# Find Geant4 package
#----------------------------------------------------------------------------

find_package(Geant4 REQUIRED ui_all vis_all)

#----------------------------------------------------------------------------
# Include Geant4 use file
#----------------------------------------------------------------------------

include(${Geant4_USE_FILE})

#----------------------------------------------------------------------------
# Project include directories
#----------------------------------------------------------------------------

include_directories(${PROJECT_SOURCE_DIR}/include)

#----------------------------------------------------------------------------
# Locate source and header files
#----------------------------------------------------------------------------

file(GLOB GEANTPY_SOURCES
    ${PROJECT_SOURCE_DIR}/src/*.cc
)

file(GLOB GEANTPY_HEADERS
    ${PROJECT_SOURCE_DIR}/include/*.hh
)

#----------------------------------------------------------------------------
# Create executable
#----------------------------------------------------------------------------

add_executable(geantpy
    geantpy.cc
    ${GEANTPY_SOURCES}
    ${GEANTPY_HEADERS}
)

#----------------------------------------------------------------------------
# Link Geant4 libraries
#----------------------------------------------------------------------------

target_link_libraries(geantpy
    ${Geant4_LIBRARIES}
)

#----------------------------------------------------------------------------
# Copy macro files into build directory
#----------------------------------------------------------------------------

set(GEANTPY_MACROS
    macros/run.mac
)

foreach(_macro ${GEANTPY_MACROS})

    configure_file(
        ${PROJECT_SOURCE_DIR}/${_macro}
        ${PROJECT_BINARY_DIR}/${_macro}
        COPYONLY
    )

endforeach()

#----------------------------------------------------------------------------
# Optional: install target
#----------------------------------------------------------------------------

install(TARGETS geantpy DESTINATION bin)