# RPLIDAR Setup Guide

This guide mirrors the official `rplidar_ros` tutorial, but uses the local paths that already exist on this machine.

## 1. Prerequisites

Required tools:

- ROS 2 Humble at `/opt/ros/humble`
- `colcon`
- `git`

These were present during validation.

## 2. Workspace layout

The local workspace is:

```bash
/home/bing/nav2/getting_start/rplidar/ros2_ws
```

The package source is:

```bash
/home/bing/nav2/getting_start/rplidar/ros2_ws/src/rplidar_ros
```

## 3. Clone the official package

If you need to recreate the setup from scratch:

```bash
mkdir -p /home/bing/nav2/getting_start/rplidar/ros2_ws/src
cd /home/bing/nav2/getting_start/rplidar/ros2_ws/src
git clone -b ros2 https://github.com/Slamtec/rplidar_ros.git
```

## 4. Build the workspace

```bash
cd /home/bing/nav2/getting_start/rplidar/ros2_ws
source /opt/ros/humble/setup.bash
colcon build --symlink-install
```

Local shortcut:

```bash
/home/bing/nav2/getting_start/rplidar/scripts/build_rplidar_ws.sh
```

## 5. Source the environment

```bash
source /opt/ros/humble/setup.bash
source /home/bing/nav2/getting_start/rplidar/ros2_ws/install/setup.bash
```

Optional persistent setup:

```bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
echo "source /home/bing/nav2/getting_start/rplidar/ros2_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

## 6. Grant access to the serial device

The official tutorial mentions two approaches.

Temporary test only:

```bash
sudo chmod 777 /dev/ttyUSB0
```

Better long-term option with udev rules:

```bash
/home/bing/nav2/getting_start/rplidar/scripts/install_rplidar_udev_rules.sh
```

After the udev rule is installed, reconnect the LiDAR and check:

```bash
ls -l /dev/rplidar
ls -l /dev/ttyUSB*
```

## 7. Start the node

### A1 with RViz

```bash
source /opt/ros/humble/setup.bash
source /home/bing/nav2/getting_start/rplidar/ros2_ws/install/setup.bash
ros2 launch rplidar_ros view_rplidar_a1_launch.py
```

### A1 without RViz

```bash
source /opt/ros/humble/setup.bash
source /home/bing/nav2/getting_start/rplidar/ros2_ws/install/setup.bash
ros2 launch rplidar_ros rplidar_a1_launch.py
```

### A1 local shortcuts

```bash
/home/bing/nav2/getting_start/rplidar/scripts/run_rplidar_a1.sh
/home/bing/nav2/getting_start/rplidar/scripts/run_rplidar_a1_view.sh
```

## 8. Override launch parameters

If your serial path or frame name is different:

```bash
ros2 launch rplidar_ros view_rplidar_a1_launch.py \
  serial_port:=/dev/ttyUSB1 \
  frame_id:=laser \
  inverted:=false \
  angle_compensate:=true
```

You can inspect launch arguments without running the node:

```bash
source /opt/ros/humble/setup.bash
source /home/bing/nav2/getting_start/rplidar/ros2_ws/install/setup.bash
ros2 launch rplidar_ros view_rplidar_a1_launch.py --show-args
```

## 9. Choose the correct launch file for your model

Serial launch defaults from the official package:

- A1: `view_rplidar_a1_launch.py`, baudrate `115200`
- A2M7: `view_rplidar_a2m7_launch.py`, baudrate `256000`
- A2M8: `view_rplidar_a2m8_launch.py`, baudrate `115200`
- A2M12: `view_rplidar_a2m12_launch.py`, baudrate `256000`
- A3: `view_rplidar_a3_launch.py`, baudrate `256000`
- S1: `view_rplidar_s1_launch.py`, baudrate `256000`
- S2: `view_rplidar_s2_launch.py`, baudrate `1000000`
- S3: `view_rplidar_s3_launch.py`, baudrate `1000000`
- C1: `view_rplidar_c1_launch.py`, baudrate `460800`

S1 TCP launch:

```bash
ros2 launch rplidar_ros view_rplidar_s1_tcp_launch.py tcp_ip:=192.168.0.7 tcp_port:=20108
```

## 10. Verify the package

Check that ROS 2 can see the package:

```bash
source /opt/ros/humble/setup.bash
source /home/bing/nav2/getting_start/rplidar/ros2_ws/install/setup.bash
ros2 pkg prefix rplidar_ros
ros2 pkg executables rplidar_ros
```

Check runtime topics after the device is connected:

```bash
/home/bing/nav2/getting_start/rplidar/scripts/check_rplidar_topics.sh
```

Expected topics usually include:

- `/scan`
- `/parameter_events`
- `/rosout`

## 11. Expected hardware caveat on this machine

The software side of the tutorial is complete, but hardware validation is still pending because no serial LiDAR device was attached during setup. If you connect the sensor later and the node fails to start, begin with [NETWORK_TROUBLESHOOTING.md](/home/bing/nav2/getting_start/rplidar/NETWORK_TROUBLESHOOTING.md).
