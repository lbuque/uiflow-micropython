# SPDX-FileCopyrightText: 2024 M5Stack Technology CO LTD
#
# SPDX-License-Identifier: MIT

include("manifest_m5stack.py")
require("mip")
require("ntptime")
require("dht")
require("onewire")
include("$(MPY_DIR)/extmod/asyncio")
require("webrepl")
require("upysh")
require("ssl")

# freeze("$(MPY_DIR)/tools", ("upip.py", "upip_utarfile.py"))
# freeze("$(MPY_DIR)/ports/esp8266/modules", "ntptime.py")
# freeze("$(MPY_DIR)/drivers/dht", "dht.py")
# freeze("$(MPY_DIR)/drivers/onewire")
# include("$(MPY_DIR)/extmod/uasyncio/manifest.py")
# include("$(MPY_DIR)/extmod/webrepl/manifest.py")
