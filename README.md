# pheeno_arduino
Instead of locating all the files for the Arduino/Teensy within the `pheeno_ros` package, I have created a separate repository containing all the Arduino code. This repository is **strongly suggested** to be used with [PlatformIO](https://platformio.org/); however, it can be used with original [Arduino](https://www.arduino.cc/) client.

## Installation
To install, just clone this directory into your home (`~/`) directory. This code works on both ROS Indigo and ROS Kinetic.

```bash
$ git clone https://github.com/acslaboratory/pheeno_arduino.git
```

## Setup

### Creating `ros_lib` files.
For ROS to work with arduino (and other) microcontrollers, libraries were created to interface a computer with a microcontroller thorugh serial connection. These libraries **must** be installed to use the `pheeno_arduino` files. To install these libraries, ROS Indigo or Kinetic must be installed and their respective ROS repositories accessable. Then install the relavent packages depending on your ROS version:

**ROS Indigo**
```bash
$ sudo apt-get install \
  ros-indigo-rosserial ros-indigo-rosserial-client \
  ros-indigo-rosserial-python ros-indigo-rosserial-arduino
```

**ROS Kinetic**
```bash
$ sudo apt-get install \
  ros-kinetic-rosserial ros-kinetic-rosserial-client \
  ros-kinetic-rosserial-python ros-kinetic-rosserial-arduino
```

Once installed, source the ROS `setup.bash` file to access the newly installed packages.

```bash
$ source /opt/ros/indigo/setup.bash   # For ROS Indigo
$ source /opt/ros/kinetic/setup.bash  # For ROS Kinetic
```

Finally, `cd` into the `lib/` folder of this respository, and run the following command to generate the `ros_lib` files required for using ROS with a microcontroller.

```bash
$ cd lib/
$ rosrun rosserial_arduino make_libraries.py .
```

### Copying `lib` Files to Project Folder/s
Once the directory is cloned, use the `file_setup.py` file that copies the `lib/` folder into all PlatformIO project directory in the folder **OR** to a specific PlatformIO project directory. For example, in the first case the code would be:

```bash
$ python file_setup.py --all
```

or

```bash
$ python file_setup.py -a
```

To copy the files to a specific folder (the `ros` directory would be used as an example), you would do this:

```bash
$ python file_setup.py --file ros
```

or

```bash
$ python file_setup.py -f ros
```

### Running PlatformIO with the Code
Begin by changing directory (`cd`) into the code you want to upload into the microcontroller and initialize PlatformIO. The example will use the `ros` project folder.

```bash
$ cd ros/
$ platformio init --board teensy31
```

**NOTE**: The `--board` option can be changed to the one that you are using. It should be noted, however, that the Pheeno uses a Teensy 3.2 whose PlatformIO option is specified by `--board teensy31`.
    
Finally, run (compile) and upload the code:

```bash
$ platformio run --target upload
```
