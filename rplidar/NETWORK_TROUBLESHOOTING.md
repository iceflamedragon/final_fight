# RPLIDAR Troubleshooting

This file covers the most common failures after the package has already been built.

## No `/dev/ttyUSB0`

Check whether the USB serial device exists:

```bash
ls -l /dev/ttyUSB*
```

If nothing is listed:

- Replug the USB cable
- Try a different USB port
- Try a data-capable cable
- Check `dmesg | tail -n 50` right after reconnecting the device

## Permission denied on the serial port

Quick test:

```bash
sudo chmod 777 /dev/ttyUSB0
```

Better fix:

```bash
/home/bing/nav2/getting_start/rplidar/scripts/install_rplidar_udev_rules.sh
```

Then unplug and reconnect the LiDAR.

## `RESULT_OPERATION_TIMEOUT`

This usually means one of these is wrong:

- Wrong serial port
- Wrong baudrate
- Power is unstable
- The model-specific launch file does not match your hardware

Try the model-appropriate launch file first. Examples:

- A1 uses `115200`
- A2M7 uses `256000`
- A2M8 uses `115200`
- A3 uses `256000`
- S2 and S3 use `1000000`

You can also override baudrate manually:

```bash
ros2 launch rplidar_ros view_rplidar_a1_launch.py serial_port:=/dev/ttyUSB0 serial_baudrate:=115200
```

## RViz opens but no laser scan appears

Check that the node is publishing:

```bash
source /opt/ros/humble/setup.bash
source /home/bing/nav2/getting_start/rplidar/ros2_ws/install/setup.bash
ros2 topic list
ros2 topic echo /scan --once
```

If `/scan` exists but RViz is empty:

- Set RViz `Fixed Frame` to `laser`
- Make sure the `LaserScan` display topic is `/scan`
- Confirm `frame_id` matches the launch parameter

## `rplidar_ros` package not found

You probably forgot to source the workspace:

```bash
source /opt/ros/humble/setup.bash
source /home/bing/nav2/getting_start/rplidar/ros2_ws/install/setup.bash
```

Then re-check:

```bash
ros2 pkg prefix rplidar_ros
```

## S1 TCP connection does not work

Confirm network connectivity first:

```bash
ping -c 4 192.168.0.7
nc -vz 192.168.0.7 20108
```

If ping fails:

- Verify the LiDAR IP address
- Check whether your PC is on the same subnet
- Disable VPNs or restrictive firewall rules for the test

If the port check fails but ping works:

- Recheck the TCP port from the device manual
- Confirm the LiDAR is in the expected network mode

Launch example:

```bash
source /opt/ros/humble/setup.bash
source /home/bing/nav2/getting_start/rplidar/ros2_ws/install/setup.bash
ros2 launch rplidar_ros view_rplidar_s1_tcp_launch.py tcp_ip:=192.168.0.7 tcp_port:=20108
```

## Build succeeds but launch still fails

Rebuild cleanly:

```bash
rm -rf /home/bing/nav2/getting_start/rplidar/ros2_ws/build
rm -rf /home/bing/nav2/getting_start/rplidar/ros2_ws/install
rm -rf /home/bing/nav2/getting_start/rplidar/ros2_ws/log
source /opt/ros/humble/setup.bash
cd /home/bing/nav2/getting_start/rplidar/ros2_ws
colcon build --symlink-install
```

This is safe for the local workspace and does not touch system ROS packages.
