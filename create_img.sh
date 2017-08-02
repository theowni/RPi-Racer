virtualenv venv -p python3
source venv/bin/activate
git clone https://github.com/theowni/RPI-Disk-Image-Decorator
cd RPI-Disk-Image-Decorator
bash setup.sh
cd src
# mount raspbian image 
python3 rpiem.py mount -p ../../raspbian.img
# setup WiFI
python3 rpiem.py run_playbook -f ../../playbooks/pi_as_router_playbook.yml -p ../../raspbian.img
# copy source codes to mounted drive
sudo cp -r ../../src/racer_soft /mnt/rpiem/
# install soft
python3 rpiem.py run_playbook -f ../../playbooks/install_soft_playbook.yml -p ../../raspbian.img
# umount raspbian image at finish
python3 rpiem.py umount
