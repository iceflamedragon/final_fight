# Nav2 SLAM Mode

This folder contains a dedicated SLAM startup entrypoint for the TurtleBot3 Gazebo demo.

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
