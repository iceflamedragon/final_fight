#!/usr/bin/env bash

set -eo pipefail

source /opt/ros/humble/setup.bash
set -u

output_prefix="${1:-/home/bing/nav2/getting_start/slam/maps/tb3_slam_map}"

mkdir -p "$(dirname "$output_prefix")"

ros2 run nav2_map_server map_saver_cli -f "$output_prefix"
