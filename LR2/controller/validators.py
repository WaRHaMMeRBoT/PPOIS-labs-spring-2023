from typing import Optional


class Validator:

    @staticmethod
    def validate_name(name: Optional[str]) -> bool:
        if name in ('', None):
            return True
        if not 0 < len(name) <= 100:
            return False
        if not name[0].isalpha():
            return False
        for i in name:
            if not (i.isalpha() or i == "-"):
                return False
        if not name == name.capitalize():
            return False
        return True

    @staticmethod
    def validate_group_number(group_number: Optional[str]) -> bool:
        if group_number in ('', None):
            return True
        if not 0 < len(group_number) <= 10:
            return False
        for i in group_number:
            if not i.isdigit():
                return False
        return True

    @staticmethod
    def validate_hours_amount(hours: int) -> bool:
        if hours is None:
            return True
        if hours < 0:
            return False
        if hours > 32000:
            return False
        return True