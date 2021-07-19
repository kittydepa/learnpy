.. nrf_connectmobil:

Upgrade with nRF Connect for mobile
#########################

Before the DFU, you must prepare your device by replacing the existing bootloader with one that uses your own public key. (These instructions are missing for nRF Connect for Desktop as well.)

-	Build a new bootloader by compiling the Bootloader project using either Keil μVision or GCC. Program the compiled bootlaoder onto the device. Remember to program the Softdevice as well for the OTA-DFU to function properly.
-	Before you build, you must copy the public_key.c file from where you generated it to <InstallFolder>\project\bootloader_secure\dfu_public_key.c.
