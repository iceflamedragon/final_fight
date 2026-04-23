#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
RPLIDAR_WS="${PROJECT_DIR}/rplidar/ros2_ws"

source /opt/ros/humble/setup.bash
source "${RPLIDAR_WS}/install/setup.bash"

ros2 launch "${PROJECT_DIR}/launch/rplidar_minimal.launch.py" "$@"
