cmake_minimum_required(VERSION 3.22)

# Gather all .c files in App/Src
file(GLOB APP_SOURCES
    Src/*.c
)

add_library(app STATIC ${APP_SOURCES})

# Inherit include paths from the stm32cubemx target
target_link_libraries(app
    PUBLIC stm32cubemx
)

# Add the include path for headers
target_include_directories(app PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/Src
)
