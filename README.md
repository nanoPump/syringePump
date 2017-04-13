# Syringe Pump
This repository contains the design files and software for an open-source syringe pump

## DIY Bill of Materials

## Design and DIY Guidelines
The file `Syringe_Pump__Master_12_4_17_LASER_CUT_4.5mm_acrylic.AI` contains the Adobe Illustrator design for laser cutting a piece of **by** 4.5mm Acrylic/Plexiglass

## Arduino | Control Board Software Installation

## Installing the GUI
###### Windows
1. Install Python (32/64Bit depending on your system)
   * You can get the latest version from [here](https://www.python.org/downloads/windows/)
   * Make sure `pip` is also included in the binary installers - This should be the default since version 3.4
2. Install `pyserial` using `pip`
```
sudo pip install pyserial
```
3. Install `PyQt5` using `pip`
```
sudo pip install PyQt5
```

###### Linux
1. Install Python (current latest version is 3.6)
```
sudo apt-get install python3.6
```

2. Install `pyserial` using `pip`
```
sudo pip install pyserial
```
3. Install `PyQt5` using `pip`
```
sudo pip install PyQt5
```

###### MacOS
1. Install Python (current latest version is 3.6)
    * You are going to need a package installer like [Homebrew](https://brew.sh) - Follow the instructions if you don not have it
    * One you have installed `Homebrew` you can run
  ```
  brew install python3
  ```
    * This should install pip3 (pip for the python3 homebrew package) - Its called pip3 to avoid issues with python2.7
    
2. Install `pyserial` using `pip`
```
sudo pip3 install pyserial
```
3. Install `PyQt5` using `pip`
```
sudo pip3 install PyQt5
```
