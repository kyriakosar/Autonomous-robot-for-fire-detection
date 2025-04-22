# talos-project
Fire detection mobile robot using ros2 and gazebo

## Folder Structure
- `models` folder contains the respective models that have to be copied under the `.gazebo/models` folder
- `src` folder contains the source code and the launch files for the project

## Dependencies
- ROS2 - humble
- Gazebo 11
- Ubuntu 20.04
- Python 3.10

## Installation
### Install ROS2
Follow the instructions on the [ROS2 installation page](https://docs.ros.org/en/rolling/Installation/Alternatives/Ubuntu-Development-Setup.html).

### Install Gazebo
Follow the instructions on the [Gazebo installation page](http://gazebosim.org/tutorials?tut=install_ubuntu).


### Exececuting the project
After installing the prerequisite dependencies, execute the following commands in the terminal to run the project
```
cd path/to/talos-project
```
```
colcon build
```
```
source path/to/project/install/setup.bash
```
```
ros2 launch yolobot_gazebo gazebo_launch.py
```

### Executing the fire detection mechanism
After executing the above commands, open a new terminal and execute the following commands
```
cd path/to/talos-project/src/yolobot_recognition/scripts
python ros_recognition_yolo.py
```

## Video of the implementation
https://github.com/t8140140/talos-project/assets/15681263/8a96e4f3-48ad-4b51-9b8e-1a91fc2dcaf8

## Reference
* Using and modifying the scripts for ROS2 control from this tutorial: https://www.youtube.com/watch?v=XqibXP4lwgA&ab_channel=robotmania
* Using the [re-trained weights for the fire detection from here: https://github.com/spacewalk01/yolov5-fire-detection/tree/main
