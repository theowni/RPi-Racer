# Overview
This project aims to build remote controlled (via WiFI and PC gamepad) Raspberry Pi car.

# Installation on Raspberry
1. Download latest Raspbian Jessie and name it raspbian.img
2. Run:
```sh
sudo bash create_img.sh
```
3. sudo dd if=raspbian.img of=/dev/your_sd_card bs=8M

# Using
1. Connect to Raspberry Pi WiFI access point
2. Connect gamepad to PC
3. Run controller:
```sh
cd src/racer_controller
sudo bash setup/install.sh
sudo python3 run.py
```
4. Controll it!

# Demo
Soon, there will be demo

# Construction
![alt text](https://raw.githubusercontent.com/theowni/rpi-racer/master/hard_docs/electronic_overview.png "Electronics")

# Milestons
* prototype working code (checked) 
* make working easy-deployment (checked)
* at-boot-start controller server
