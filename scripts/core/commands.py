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

