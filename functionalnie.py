import os
import json
import shutil
from datetime import datetime

PROFILE_FILE = "progression_profiles.json"
BACKUP_DIR = "backups"

def calculate_arithmetic_member(a1, d, n):
    return a1 + d * (n - 1)

def calculate_geometric_member(b1, q, n):
    return b1 * (q ** (n - 1))

def save_profile(name, p_type, first_member, step):
    profiles = load_all_profiles()
    profiles[name] = {
        "type": p_type,
        "first_member": first_member,
        "step": step,
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    try:
        with open(PROFILE_FILE, "w", encoding="utf-8") as f:
            json.dump(profiles, f, ensure_ascii=False, indent=4)
        return True
    except Exception:
        return False

def load_all_profiles():
    if not os.path.exists(PROFILE_FILE):
        return {}
    try:
        with open(PROFILE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def create_backup():
    if not os.path.exists(PROFILE_FILE):
        return False, "Рабочий файл профилей не обнаружен."
    if not os.path.exists(BACKUP_DIR):
        try:
            os.makedirs(BACKUP_DIR)
        except Exception as e:
            return False, f"Не удалось создать директорию архива: {e}"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"profiles_backup_{timestamp}.json"
    backup_path = os.path.join(BACKUP_DIR, backup_filename)
    try:
        shutil.copy2(PROFILE_FILE, backup_path)
        return True, backup_path
    except Exception as e:
        return False, str(e)

def restore_backup():
    if not os.path.exists(BACKUP_DIR) or not os.listdir(BACKUP_DIR):
        return False, "Локальный архив пуст. Точки восстановления не найдены."
    backups = [f for f in os.listdir(BACKUP_DIR) if f.startswith("profiles_backup_")]
    if not backups:
        return False, "Подходящие файлы резервных копий отсутствуют."
    latest_backup = os.path.join(BACKUP_DIR, sorted(backups)[-1])
    try:
        shutil.copy2(latest_backup, PROFILE_FILE)
        return True, latest_backup
    except Exception as e:
        return False, str(e)


