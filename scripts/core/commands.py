import os
import subprocess
import pyperclip
from .config import update_config

# Login configuration command
def cmd_init_setup():
    print("Welcome to BridgeBoard setup\n")

    # Gathering data
    new_data = {
        "webdav_hostname":  input("Enter server link (Recommended Nexctould based tools): "),
        "webdav_logi":      input("Enter login: "),
        "webdav_password":  input("Enter password: ")
    }

    # Saving config
    update_config(new_data)
    print("Configuration saved succesfully!")

# NOTE these are for later recofiguration 
def notify(title, message):
    # Native macOS notifications (no extra packages needed)
    os.system(f"osascript -e 'display notification \"{message}\" with title \"{title}\"'")

def cmd_login():
    ensure_config()
    editor = os.environ.get('EDITOR', 'nano')
    print(f"Opening config file in {editor}...")
    subprocess.call([editor, str(CONFIG_FILE)])

def cmd_send():
    text = pyperclip.paste()
    if not text.strip():
        print("Clipboard is empty.")
        return

    print("Sending clipboard to cloud...")
    cloud = CloudClient()
    if cloud.upload(text):
        print("Success: Clipboard sent.")
        notify("CloudBridge", "Clipboard sent to the cloud.")
    else:
        print("Failed to send clipboard.")

def cmd_get():
    print("Fetching clipboard from cloud...")
    cloud = CloudClient()
    text = cloud.download()
    
    if text:
        pyperclip.copy(text)
        print("Success: Clipboard updated.")
        notify("CloudBridge", "New clipboard received.")
    else:
        print("Failed to fetch clipboard or cloud is empty.")
