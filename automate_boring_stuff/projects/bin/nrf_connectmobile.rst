.. nrf_connectmobil:

Upgrade with nRF Connect for mobile
#########################

Before the DFU, you must prepare your device by replacing the existing bootloader with one that uses your own public key. (These instructions are missing for nRF Connect for Desktop as well.)

-	Build a new bootloader by compiling the Bootloader project using either Keil μVision or GCC. Program the compiled bootlaoder onto the device. Remember to program the Softdevice as well for the OTA-DFU to function properly.
-	Before you build, you must copy the public_key.c file from where you generated it to <InstallFolder>\project\bootloader_secure\dfu_public_key.c.

The following procedure involves using a phone or tablet with nRF Connect for mobile installed to run DFU. 
1.	Transfer the zip package that will be used for DFU to your phone.
#	Power on the device. Open nRFConnect on your phone.
#	Tap Scan. From the available discovered devices, connect to your device. 

Note:
The discovered devices list is not automatically refreshed when they stop advertising. Whenever you have problems connecting to a device from the list, try refreshing the list.

4. Expand the Secure DFU Service section. There are two icons to the right of the DUF Control Point area.
a.	The icon to the right turns notifications on/off. Make sure they are enabled (the icon must be crossed)
#	Tap the icon to the left to put the device into bootloader (DFU) mode. Tap OK when prompted to reset the device to bootloader. 

<IMAGE 1> <IMAGE 2>

Activating DFU mode.

Note!
The device now enters DFU mode. Go to the Scanner tab and run a new scan. A device with the same name but “DFU” added appears in the list of discovered devices

5. Connect to the new device. Click the DFU icon.
<IMAGE 3>
Running DFU.

6. Select Distribution packet (ZIP) and navigate to the package that you previously uploaded to your mobile.
<IMAGE 4>
Uploading the ZIP file.

7. The package is now uploaded to the device.
