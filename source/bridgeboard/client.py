from webdav3.client import Client
import os
from .config import get_config

class ClientCloud:
    def __init__(self):
        conf = get_config()
        options = {
            "webdav_hostname":  conf.get("webdav_hostname", ""),
            "webdav_login":     conf.get("webdav_login", ""),
            "webdav_password":  conf.get("webdav_password", "")
        }
        self.client = Client(options)
        self.remote_path = "clipboard_sync.txt"
    
    def upload(self, text):
        tmp_file = "tmp_upload.txt"
        with open(tmp_file, "w", encoding = "utf-8") as file:
            file.write(text)
        try: 
            self.client.upload_sync(remote_path = self.remote_path, local_path = tmp_file)
            return True
        except Exception as e:
            print(f"Error {e}")
        finally: 
            if os.path.exists(tmp_file):
                os.remove(tmp_file)

# NOTE 
def download(self):
        tmp_file = "tmp_down.txt"
        try:
            self.client.download_sync(remote_path=self.remote_path, local_path=tmp_file)
            with open(tmp_file, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            print(f"[Error] Download failed: {e}")
            return None
        finally:
            if os.path.exists(tmp_file):
                os.remove(tmp_file)