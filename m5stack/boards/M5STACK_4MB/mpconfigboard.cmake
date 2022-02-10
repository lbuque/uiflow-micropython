set(SDKCONFIG_DEFAULTS
    ./boards/sdkconfig.base
    ./boards/sdkconfig.flash_4mb
    ./boards/sdkconfig.ble
    ./boards/sdkconfig.240mhz
    ./boards/sdkconfig.disable_iram
)

if(NOT MICROPY_FROZEN_MANIFEST)
    set(MICROPY_FROZEN_MANIFEST ${CMAKE_SOURCE_DIR}/boards/manifest.py)
endif()
