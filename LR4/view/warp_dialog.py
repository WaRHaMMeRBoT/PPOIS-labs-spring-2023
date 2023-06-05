from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField


class WarpDialog:
    def __init__(self, controller) -> None:
        self._controller = controller

    def build_dialog(self) -> MDDialog:
        return MDDialog(
            title="Information",
            type="custom",
            content_cls=MDBoxLayout(
                MDTextField(
                    id='size',
                    hint_text="Field Size",
                    font_size='10',
                    max_text_length=2,
                    helper_text_mode="on_error"
                ),
                orientation="vertical",
                spacing="15dp",
                size_hint_y=None,
                height="50dp"
            ),
            buttons=[
                MDFlatButton(
                    text="Cancel",
                    theme_text_color="Custom",
                    on_release=lambda event: self._close_dialog(),
                ),
                MDFlatButton(
                    text="Continue",
                    theme_text_color="Custom",
                    on_release=lambda event: self._warp(),
                ),
            ],
        )

    def _close_dialog(self) -> None:
        self._controller.close_dialog()

    def _warp(self) -> None:
        self._controller.warp()