from webdav3.client import Client
import os

# Cofigure connection with host server



client = Client(options)

def sync_clipboard(data):
    #Sending clipboard to Nextcloud services
    local_clipboard = "clipboard.txt"
    with open(local_clipboard, "w", encoding = "utf-8") as file:
        file.write(data)

    #Sending 
    try: 
        client.upload_sync(remote_path = "remote_clipboard.txt", local_path = local_clipboard)
        print("Succesfully sent!\n")
    except Exception as e:
        print(f"Error {e}") 
    finally: 
        if os.path.exists(local_clipboard):
            os.remove(local_clipboard)

def get_remote_clipboard():
    try:
        client.download_sync(remote_path = "remote_clipboard.txt", local_path = "temp_clipboard.txt")
        with open("temp_clipboard.txt", "r", encoding = "utf-8" ) as file:
            clipboard_data = file.read()
        os.remove("temp_clipboard.txt")
        return clipboard_data
    except Exception:
        return None

#Test
if __name__ == "__main__":
    sync_clipboard("My data")
    print(f"Data from cloud: {get_remote_clipboard()}")




