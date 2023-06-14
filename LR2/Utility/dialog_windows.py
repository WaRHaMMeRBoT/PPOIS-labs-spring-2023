import os
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


class DialogContent(BoxLayout):
    pass


class InputDialogContent(DialogContent):
    pass


class FilterDialogContent(DialogContent):
    pass


class DeleteDialogContent(DialogContent):
    pass


class UploadDialogContent(DialogContent):
    pass


class SaveDialogContent(DialogContent):
    pass


class DialogWindow(MDDialog):
    def __init__(self, **kwargs):
        super().__init__(
            title=kwargs["title"],
            type="custom",
            content_cls=kwargs["content_cls"],
            buttons=[
                MDFlatButton(
                    text="OK",
                    theme_text_color="Custom",
                    on_release=self.close
                ),
            ],
        )
        self.mode = kwargs["mode"]
        self.controller = kwargs["controller"]
        self.model = kwargs["model"]

    def close(self, obj):
        self.dismiss()


class InputWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
            title="New record: ",
            content_cls=InputDialogContent(),
            mode="input",
            controller=kwargs["controller"],
            model=kwargs["model"]
        )

    def close(self, obj):
        self.dismiss()
        self.controller.close_dialog(
            [
                self.content_cls.ids.input_name.text,
                self.content_cls.ids.input_date_of_birth.text,
                self.content_cls.ids.input_date_of_last_visit.text,
                self.content_cls.ids.input_veterinary_name.text,
                self.content_cls.ids.input_diagnosis.text,
            ]
        )


class FilterWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
            title="Filter records: ",
            content_cls=FilterDialogContent(),
            mode="filter",
            controller=kwargs["controller"],
            model=kwargs["model"]
        )

    def close(self, obj):
        self.dismiss()
        self.controller.close_dialog(
            [
                self.content_cls.ids.filter_name.text,
                self.content_cls.ids.filter_date_of_birth.text,
                self.content_cls.ids.filter_date_of_last_visit.text,
                self.content_cls.ids.filter_veterinary_name.text,
                self.content_cls.ids.filter_diagnosis.text,
            ]
        )


class DeleteWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
            title="Delete record: ",
            content_cls=DeleteDialogContent(),
            mode="delete",
            controller=kwargs["controller"],
            model=kwargs["model"]
        )

    def close(self, obj):
        self.dismiss()
        self.controller.close_dialog(
            [
                self.content_cls.ids.delete_name.text,
                self.content_cls.ids.delete_date_of_birth.text,
                self.content_cls.ids.delete_date_of_last_visit.text,
                self.content_cls.ids.delete_veterinary_name.text,
                self.content_cls.ids.delete_diagnosis.text,
            ]
        )


class SaveWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
            title="Saving: ",
            content_cls=SaveDialogContent(),
            mode="save",
            controller=kwargs["controller"],
            model=kwargs["model"]
        )

    def close(self, obj):
        self.dismiss()
        self.controller.close_dialog(self.content_cls.ids.save_path.text)


class UploadWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
            title="Upload: ",
            content_cls=UploadDialogContent(),
            mode="upload",
            controller=kwargs["controller"],
            model=kwargs["model"]
        )

    def close(self, obj):
        self.dismiss()
        self.controller.close_dialog(self.content_cls.ids.upload_path.text)


Builder.load_file(os.path.join(os.path.dirname(__file__), "dialog_windows.kv"))
