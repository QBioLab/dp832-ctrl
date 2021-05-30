Prerequirment:
```bash
sudo pip install pyusb
sudo pip install PyVISA pyvisia-py

Permission in linux:
Add usbtmc.rules to /etc/udev/rules.d/
```

```
# only for DPS832 premission, you can add more instruments after looking lsusb
SUBSYSTEM="usb", ACTION=="add", ATTRS{idVendor}=="1ab1", ATTRS{idProduct}=="0e11", MODE="0666"
```

