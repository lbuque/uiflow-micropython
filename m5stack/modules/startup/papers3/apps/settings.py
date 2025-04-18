# SPDX-FileCopyrightText: 2024 M5Stack Technology CO LTD
#
# SPDX-License-Identifier: MIT

from .. import app_base
import M5
import widgets
import esp32


class SettingsApp(app_base.AppBase):
    def __init__(self, icos: dict, data=None) -> None:
        self._lcd = icos
        self._wifi = data
        super().__init__()

    def on_install(self):
        self.descriptor = app_base.Descriptor(x=493, y=164, w=48, h=181)

    def on_launch(self):
        self.get_data()

    def on_view(self):
        self._lcd.drawImage("/system/papers3/config.png", 0, 0)

        self._ssid_label = widgets.Label(
            "ssid",
            87,
            630,
            w=333,
            font_align=widgets.Label.LEFT_ALIGNED,
            fg_color=0x000000,
            bg_color=0xE3E3E3,
            font=M5.Lcd.FONTS.DejaVu24,
            parent=self._lcd,
        )
        self._ssid_label.set_long_mode(widgets.Label.LONG_DOT)
        self._ssid_label.set_text(self.ssid)

        self._server_label = widgets.Label(
            "server",
            87,
            747,
            w=333,
            font_align=widgets.Label.LEFT_ALIGNED,
            fg_color=0x000000,
            bg_color=0xE3E3E3,
            font=M5.Lcd.FONTS.DejaVu24,
            parent=self._lcd,
        )
        self._server_label.set_long_mode(widgets.Label.LONG_DOT)
        self._server_label.set_text(self.server)

    def on_ready(self):
        pass

    def on_hide(self):
        pass

    def on_exit(self):
        pass

    async def _click_event_handler(self, x, y, fw):
        pass

    async def _kb_event_handler(self, event, fw):
        pass

    def get_data(self):
        self.nvs = esp32.NVS("uiflow")
        self.ssid = self.nvs.get_str("ssid0")
        self.psk = self.nvs.get_str("pswd0")
        self.server = self.nvs.get_str("server")
        self.ssid_tmp = self.ssid
        self.psk_tmp = self.psk
        self.server_tmp = self.server
