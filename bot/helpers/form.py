"""
FORM STATE MANAGER
Digunakan untuk mengelola input user (order flow)
"""

USER_FORMS = {}


def start_form(user_id: int, form_name: str, data=None):
    """
    Mulai form baru
    """
    USER_FORMS[user_id] = {
        "form": form_name,
        "step": 0,
        "data": data or {}
    }


def next_step(user_id: int):
    """
    Lanjut ke step berikutnya
    """
    if user_id in USER_FORMS:
        USER_FORMS[user_id]["step"] += 1


def set_data(user_id: int, key: str, value):
    """
    Simpan data form
    """
    if user_id in USER_FORMS:
        USER_FORMS[user_id]["data"][key] = value

def set_state(user_id: int, form_name: str, data=None):
    start_form(user_id, form_name, data)

def get_state(user_id: int):
    return get_form(user_id)

def clear_state(user_id: int):
    end_form(user_id)


def get_form(user_id: int):
    """
    Ambil state form user
    """
    return USER_FORMS.get(user_id)


def end_form(user_id: int):
    """
    Hapus form setelah selesai / batal
    """
    USER_FORMS.pop(user_id, None)

