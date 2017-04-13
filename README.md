# Syringe Pump
This repository contains the design files and software for an open-source syringe pump

## DIY Bill of Materials
1. Mechanical Parts
    1. 3x 400by500mm 4.5mm tall Acrylic Sheets - [Recomended Supplier](http://uk.rs-online.com/web/p/solid-plastic-sheets/0824525/) in the UK or worldwide using Part Number for [RS Components](http://rs-online.com): 824-525
    2. SFU1605 250mm Ballscrew with corresponding BF12 and BK12 Support bearings. These can easily be found on ebay.
    3. LM8UU Linear Ball Bearings - 8mm Shaft
    4. 8mm Stainless Steel Rods
    
2. Electrical Parts
    1. 12V Power Supply
    2. Stepper Motor driver: TB6600 or similar
    3. Arduino Uno
    4. USB Cable


## Design and DIY Guidelines
The file `Syringe_Pump__Master_12_4_17_LASER_CUT_4.5mm_acrylic.AI` contains the Adobe Illustrator design for laser cutting 3 pieces of **400by500mm** 4.5mm (5mm) thick Acrylic/Plexiglass which can then be used to build the remaining mechanical parts of the syringe

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
4. Navigate to this repository and run
```
pyuic5 mainwindow.ui>mainwindow_auto.py
python pump_control.py
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
4. Navigate to this repository and run
```
pyuic5 mainwindow.ui>mainwindow_auto.py
python pump_control.py
```

###### MacOS
1. Install Python (current latest version is 3.6)
    * You are going to need a package installer like [Homebrew](https://brew.sh) - Follow the instructions if you don not have it
    * One you have installed `Homebrew` you can run it to install python. This should install pip3 (pip for the python3 homebrew package) - Its called pip3 to avoid issues with python2.7
  ```
  brew install python3
  ```
    
2. Install `pyserial` using `pip`
```
sudo pip3 install pyserial
```
3. Install `PyQt5` using `pip`
```
sudo pip3 install PyQt5
```
4. Navigate to this repository and run
```
pyuic5 mainwindow.ui>mainwindow_auto.py
python pump_control.py
```
