# Micro:Bits-webapp

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Configuration](#configuration)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)


<!-- ABOUT THE PROJECT -->
## About The Project

![product-screenshot]

Micro:Bits webapp is a app where you can connect multiple Micro:Bit to a system where you can monitor temperature and light level. 
It was built as project for a custommer in the fall 2020 at Bleking Institution of Technology (BTH).

It's main purpos is to monitor and guard temperatures and light levels in the room where you placed the Micro:Bit.

The system supports:
* Room visualization with Micro:Bits placements
* Temperature- and light-readings from Micro:bit in real-time
* E-mail notifications when levels outside allowed intervals
* Simple display of historic data (high/low per day)
* Authorization for configuration

### Built With
* [Flask](https://flask.palletsprojects.com/)
* [PySerial](https://pypi.org/project/pyserial/)
* [BBC Micro:Bit](https://microbit.org/)



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Dependencies
Below is the dependencies in Python for this app listed:
- click==7.1.2
- pytest==6.0.2
- Werkzeug==1.0.1
- Flask==1.1.2
- websockets==8.1
- pyserial==3.4


### Installation

Installation instructions are writen for Windows Powershell.

1. Clone the repo
```sh
git clone https://github.com/your_username_/Project-Name.git
```
2. Install dependencies
```sh
pip install click pytest Werkzeug Flask websockets pyserial
```
3. Config what ports you are using for Micro:Bits (Pre-configured for Windows ports COM1 - COM10)<br>
("./microbit-module/config.json")
```JSON
{
    "ports":["COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", "COM10"]
}
```
4. Configure e-mail credentials ("./microbit-module/mailmodule/cred-template.json")
```JSON
{
    "name":"Microbit-Monitoring System (No reply)",
    "e-mail":"example@email.com",
    "password":"Enter password here",
    "port": Enter port here, eg gmails: 587
}
```
5. Change name on ".\creds-template.json" to "cred.json"
```sh
Rename-Item -Path ".\microbit-module\mailmodule\cred-template.json" -NewName "cred.json"
```
6. Connect Micro:bits by USB
7. Flash instructions to Micro:Bits (Assuming that the micro:bit is connected to d:\\)
```sh
Copy-Item ".\microbit-module\microbit-instructions.hex" -Destination "d:\"
```
8. Initialize Database
```sh
init.ps1
```
9. Run application
```sh
run.ps1
```

<!-- USAGE EXAMPLES -->
## Configuration

When newly installed the system has to be configurated with new rooms, positioning of microbits.
When initilized the system generates a user with credentials:
```
Username: admin
Password: admin
```
![after-init]
1. Sign in by pressing login in the top-right corner and entering credentials.
2. Click the "New room"-link in the left column.
3. Give your new room a description and mesurements
![new-room]
4. Click "Edit" at the top-right corner of the room-visualization box.
5. Add desired microbit to the room in the right box
![add-mb]
6. By clicking the name of the Micro:Bit you enter configuration for the Micro:Bit where you enable e-mail notifications and placement of the Micro:bit
![config-mb]
7. Submit changes and the app is up and running!
![done]

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Isac Svensson - isac.m.svensson@gmail.com

Project Link: [https://github.com/IsacSvensson/Micro-Bits-webapp](https://github.com/IsacSvensson/Micro-Bits-webapp)

<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-screenshot]: Img/screendump.PNG
[after-init]: Img/newly-init.png
[new-room]: Img/new-room.png
[add-mb]: Img/add-mb.png
[config-mb]: Img/config-mb.png
[done]: Img/done.png