<<<<<<< HEAD
# Tip Cloud 
Tip Cloud is productivicty service which helps maitain consistenst performance while working across various apps, programs and devices maitaing privacy. 

Note: 
Tip Cloud is currently in early-stage development. Core logic is implemented; UI and production-ready scaling are in progress. Target V1 Launch: May 2026.

=======
# BridgeBoard

BridgeBoard is cross-platform CLI tool for suncing your clipboard between devices using WebDAV. 

## Features
 - Your data stays on your own webdav server
 - Works on linux/macOS
 - Send and get latest text from your clipborad via simple and  intuitive commands 
 - Get text on demand from cloud clipboard 


## Installation 
**(Debian/Ubuntu based)** ensure you have installed   clipboard manager ```xclip``` installed: 
```bash
sudo apt update && sudo apt install xclip -y 
```
Install via **pip**:
```bash
git clone https://github.com/Kaccet158/BridgeBoard.git
cd BridgeBoard
pip install -e 
```
*If your using newer versions of distro you might to install via ```pip install -e --break-system-packages```*\

**macOS** ensure if you have installed python if not install via ```Homebrew```:
```zsh
brew install python3
```
Install **via pip**:
```zsh
git clone https://github.com/Kaccet158/BridgeBoard.git
cd BridgeBoard
pip install .
```
## Usage 
 - First time login with your nextcloud provider via ```bb login```
 ```bash
Welcome to BridgeBoard setup

Enter server link (Nexctould based tools): #Your server adress
Enter login:                               #Your login
Enter password:                            #App password not   the actuall account password

Configuration saved succesfully!
 ```
 - For deeper configuration of server use ```bb config```
 - To sent latest text from local clipboard ```bb send``` and to get remote clipboard ```bb get```

### Note
> BridgeBoard is currently in early-stage development.
>>>>>>> feature/pythonCLI-extended_config
