import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def _build_launch_actions(context):
    lidar_model = LaunchConfiguration('lidar_model').perform(context).strip().lower()
    serial_baudrate = LaunchConfiguration('serial_baudrate').perform(context).strip()

    model_to_baudrate = {
        'a1': '115200',
        'a2': '256000',
        'a3': '256000',
    }
    resolved_baudrate = serial_baudrate or model_to_baudrate.get(lidar_model, '115200')

    rviz_config = os.path.join(
        get_package_share_directory('rplidar_ros'),
        'rviz',
        'rplidar_ros.rviz',
    )

    rplidar_node = Node(
        package='rplidar_ros',
        executable='rplidar_node',
        name='rplidar_node',
        output='screen',
        parameters=[
            {
                'channel_type': 'serial',
                'serial_port': ParameterValue(
                    LaunchConfiguration('serial_port'), value_type=str
                ),
                'serial_baudrate': int(resolved_baudrate),
                'frame_id': ParameterValue(LaunchConfiguration('frame_id'), value_type=str),
                'inverted': ParameterValue(LaunchConfiguration('inverted'), value_type=bool),
                'angle_compensate': ParameterValue(
                    LaunchConfiguration('angle_compensate'), value_type=bool
                ),
                'scan_mode': ParameterValue(LaunchConfiguration('scan_mode'), value_type=str),
                'topic_name': 'scan',
            }
        ],
    )

    rviz_node = Node(
        condition=IfCondition(LaunchConfiguration('use_rviz')),
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config],
        output='screen',
    )

    return [rplidar_node, rviz_node]


def generate_launch_description():
    return LaunchDescription(
        [
            DeclareLaunchArgument(
                'use_rviz',
                default_value='True',
                description='Whether to start RViz for live scan visualization.',
            ),
            DeclareLaunchArgument(
                'lidar_model',
                default_value='a1',
                description='RPLIDAR model profile used to resolve the default baudrate.',
            ),
            DeclareLaunchArgument(
                'serial_port',
                default_value='/dev/ttyUSB0',
                description='Serial device path for the LiDAR.',
            ),
            DeclareLaunchArgument(
                'serial_baudrate',
                default_value='',
                description='Override serial baudrate. Empty uses the lidar_model default.',
            ),
            DeclareLaunchArgument(
                'frame_id',
                default_value='laser',
                description='LaserScan frame_id published on /scan.',
            ),
            DeclareLaunchArgument(
                'inverted',
                default_value='false',
                description='Whether to invert scan data.',
            ),
            DeclareLaunchArgument(
                'angle_compensate',
                default_value='true',
                description='Whether to enable angle compensation.',
            ),
            DeclareLaunchArgument(
                'scan_mode',
                default_value='Sensitivity',
                description='Scan mode requested from the RPLIDAR driver.',
            ),
            OpaqueFunction(function=_build_launch_actions),
        ]
    )
