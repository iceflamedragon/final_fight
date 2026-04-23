# RPLIDAR Getting Started

This folder turns the official `rplidar_ros` tutorial into a local ROS 2 Humble workspace that is already set up on this machine.

## What is already done

- Created a workspace at `/home/bing/nav2/getting_start/rplidar/ros2_ws`
- Cloned the official `ros2` branch of `https://github.com/Slamtec/rplidar_ros.git`
- Built the package successfully with `colcon build --symlink-install`
- Verified that ROS 2 can discover `rplidar_ros`
- Verified that launch files such as `view_rplidar_a1_launch.py` and `rplidar_a1_launch.py` load correctly

Build verification was completed on `2026-04-23`.

## Important note about hardware

No live LiDAR device was attached during setup. At setup time, this machine did not expose `/dev/ttyUSB0` or `/dev/rplidar`, so the package build and launch arguments were verified, but live scan data was not tested.

## Quick start

For RPLIDAR A1 with RViz:

```bash
source /opt/ros/humble/setup.bash
source /home/bing/nav2/getting_start/rplidar/ros2_ws/install/setup.bash
ros2 launch rplidar_ros view_rplidar_a1_launch.py
```

For RPLIDAR A1 without RViz:

```bash
source /opt/ros/humble/setup.bash
source /home/bing/nav2/getting_start/rplidar/ros2_ws/install/setup.bash
ros2 launch rplidar_ros rplidar_a1_launch.py
```

If your device is not on `/dev/ttyUSB0`, override it explicitly:

```bash
ros2 launch rplidar_ros view_rplidar_a1_launch.py serial_port:=/dev/ttyUSB1
```

## Local helper scripts

- `scripts/build_rplidar_ws.sh`
- `scripts/run_rplidar_a1.sh`
- `scripts/run_rplidar_a1_view.sh`
- `scripts/check_rplidar_topics.sh`
- `scripts/install_rplidar_udev_rules.sh`

Example:

```bash
/home/bing/nav2/getting_start/rplidar/scripts/run_rplidar_a1_view.sh
```

## Common launch files

- `view_rplidar_a1_launch.py`: A1, serial, default baudrate `115200`
- `view_rplidar_a2m7_launch.py`: A2M7, serial, default baudrate `256000`
- `view_rplidar_a2m8_launch.py`: A2M8, serial, default baudrate `115200`
- `view_rplidar_a2m12_launch.py`: A2M12, serial, default baudrate `256000`
- `view_rplidar_a3_launch.py`: A3, serial, default baudrate `256000`
- `view_rplidar_s1_launch.py`: S1, serial, default baudrate `256000`
- `view_rplidar_s1_tcp_launch.py`: S1, TCP, default target `192.168.0.7:20108`
- `view_rplidar_s2_launch.py`: S2, serial, default baudrate `1000000`
- `view_rplidar_s2e_launch.py`: S2E
- `view_rplidar_s3_launch.py`: S3, serial, default baudrate `1000000`
- `view_rplidar_t1_launch.py`: T1
- `view_rplidar_c1_launch.py`: C1, serial, default baudrate `460800`

## Where to look next

- Detailed setup: [setup_guide.md](/home/bing/nav2/getting_start/rplidar/setup_guide.md)
- Troubleshooting: [NETWORK_TROUBLESHOOTING.md](/home/bing/nav2/getting_start/rplidar/NETWORK_TROUBLESHOOTING.md)
- Example dependency manifest: [DEMO_package.xml](/home/bing/nav2/getting_start/rplidar/DEMO_package.xml)
