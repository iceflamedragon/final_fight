# Nav2 SLAM Mode

This folder contains two entrypoints:

- A dedicated SLAM startup entrypoint for the TurtleBot3 Gazebo demo
- A minimal real-hardware RPLIDAR bringup entrypoint for `/scan` and RViz validation

## Launch SLAM mode

```bash
source /opt/ros/humble/setup.bash
ros2 launch /home/bing/nav2/getting_start/slam/launch/nav2_tb3_slam.launch.py
```

## Headless launch

```bash
source /opt/ros/humble/setup.bash
ros2 launch /home/bing/nav2/getting_start/slam/launch/nav2_tb3_slam.launch.py headless:=True use_rviz:=False
```

## How this mode differs from the original launcher

- `slam:=True` is forced, so Nav2 starts `slam_toolbox` instead of `map_server + amcl`.
- The same embedded TurtleBot3 world is reused, so we still avoid the Gazebo `/spawn_entity` timeout.
- There is no preloaded map file for localization. The map is built online from LiDAR and odometry.

## Typical workflow

1. Launch the SLAM stack.
2. Drive the robot around to build the map.
3. In RViz, watch the `/map` topic update live.
4. Save the finished map with:

```bash
source /opt/ros/humble/setup.bash
/home/bing/nav2/getting_start/slam/scripts/save_map.sh
```

You can also provide a custom output prefix:

```bash
source /opt/ros/humble/setup.bash
/home/bing/nav2/getting_start/slam/scripts/save_map.sh /tmp/my_tb3_map
```

## Launch Minimal RPLIDAR Bringup

Use the local wrapper script to start the real LiDAR driver from this project:

```bash
/home/bing/nav2/getting_start/slam/scripts/run_rplidar_minimal.sh
```

Disable RViz if you only want the driver:

```bash
/home/bing/nav2/getting_start/slam/scripts/run_rplidar_minimal.sh use_rviz:=False
```

You can also launch it directly:

```bash
source /opt/ros/humble/setup.bash
source /home/bing/nav2/getting_start/slam/rplidar/ros2_ws/install/setup.bash
ros2 launch /home/bing/nav2/getting_start/slam/launch/rplidar_minimal.launch.py
```

## RPLIDAR Parameters

The wrapper launch keeps a stable interface for local bringup:

- `use_rviz:=True|False`
- `lidar_model:=a1|a2|a3`
- `serial_port:=/dev/ttyUSB0`
- `serial_baudrate:=115200` or another explicit value
- `frame_id:=laser`
- `inverted:=false`
- `angle_compensate:=true`
- `scan_mode:=Sensitivity`

If `serial_baudrate` is omitted, the launch file resolves it from `lidar_model`:

- `a1 -> 115200`
- `a2 -> 256000`
- `a3 -> 256000`

Examples:

```bash
/home/bing/nav2/getting_start/slam/scripts/run_rplidar_minimal.sh lidar_model:=a2
```

```bash
/home/bing/nav2/getting_start/slam/scripts/run_rplidar_minimal.sh lidar_model:=a3 serial_baudrate:=256000 serial_port:=/dev/ttyUSB1
```

## Verify Real LiDAR Data

After the driver starts, verify that ROS 2 is receiving scans:

```bash
source /opt/ros/humble/setup.bash
source /home/bing/nav2/getting_start/slam/rplidar/ros2_ws/install/setup.bash
ros2 topic list | grep scan
ros2 topic echo /scan --once
```

Expected checks:

- `/scan` exists
- The message type is `sensor_msgs/msg/LaserScan`
- `header.frame_id` is `laser` by default, or your overridden `frame_id`
- RViz can use `laser` as the fixed frame for minimal visualization

## Current Limits

This minimal RPLIDAR entrypoint does not yet provide a full real-robot SLAM stack.

What it includes:

- Real RPLIDAR driver startup
- `/scan` publishing
- Optional RViz visualization

What it does not include yet:

- `odom -> base_link`
- `base_link -> laser` static transform
- `/cmd_vel`
- Real-robot Nav2 or `slam_toolbox` integration

To upgrade this into full real-hardware SLAM later, the expected interfaces are:

- `/scan`
- `odom -> base_link`
- `base_link -> laser`
- `/cmd_vel`
