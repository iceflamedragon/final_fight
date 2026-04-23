import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    project_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    base_launch = os.path.join(project_dir, 'launch', 'nav2_tb3_getting_started.launch.py')

    namespace = LaunchConfiguration('namespace')
    use_namespace = LaunchConfiguration('use_namespace')
    use_sim_time = LaunchConfiguration('use_sim_time')
    nav2_params_file = LaunchConfiguration('nav2_params_file')
    autostart = LaunchConfiguration('autostart')
    use_composition = LaunchConfiguration('use_composition')
    use_respawn = LaunchConfiguration('use_respawn')
    use_simulator = LaunchConfiguration('use_simulator')
    use_robot_state_pub = LaunchConfiguration('use_robot_state_pub')
    use_rviz = LaunchConfiguration('use_rviz')
    headless = LaunchConfiguration('headless')
    world = LaunchConfiguration('world')
    rviz_config_file = LaunchConfiguration('rviz_config_file')

    declare_namespace_cmd = DeclareLaunchArgument(
        'namespace', default_value='', description='Top-level namespace'
    )
    declare_use_namespace_cmd = DeclareLaunchArgument(
        'use_namespace', default_value='false', description='Whether to apply a namespace'
    )
    declare_use_sim_time_cmd = DeclareLaunchArgument(
        'use_sim_time', default_value='true', description='Use simulation clock if true'
    )
    declare_params_file_cmd = DeclareLaunchArgument(
        'nav2_params_file',
        default_value='/opt/ros/humble/share/nav2_bringup/params/nav2_params.yaml',
        description='Full path to the ROS2 parameters file to use',
    )
    declare_autostart_cmd = DeclareLaunchArgument(
        'autostart', default_value='true', description='Automatically startup the nav2 stack'
    )
    declare_use_composition_cmd = DeclareLaunchArgument(
        'use_composition', default_value='True', description='Whether to use composed bringup'
    )
    declare_use_respawn_cmd = DeclareLaunchArgument(
        'use_respawn',
        default_value='False',
        description='Whether to respawn if a node crashes when composition is disabled',
    )
    declare_use_simulator_cmd = DeclareLaunchArgument(
        'use_simulator', default_value='True', description='Whether to start the simulator'
    )
    declare_use_robot_state_pub_cmd = DeclareLaunchArgument(
        'use_robot_state_pub',
        default_value='True',
        description='Whether to start the robot state publisher',
    )
    declare_use_rviz_cmd = DeclareLaunchArgument(
        'use_rviz', default_value='True', description='Whether to start RVIZ'
    )
    declare_headless_cmd = DeclareLaunchArgument(
        'headless', default_value='False', description='Whether to skip gzclient'
    )
    declare_world_cmd = DeclareLaunchArgument(
        'world',
        default_value=os.path.join(project_dir, 'worlds', 'tb3_world_embedded.world'),
        description='Full path to the world file to load',
    )
    declare_rviz_config_file_cmd = DeclareLaunchArgument(
        'rviz_config_file',
        default_value='/opt/ros/humble/share/nav2_bringup/rviz/nav2_default_view.rviz',
        description='Full path to the RVIZ config file to use',
    )

    slam_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(base_launch),
        launch_arguments={
            'namespace': namespace,
            'use_namespace': use_namespace,
            'slam': 'True',
            'map': '',
            'use_sim_time': use_sim_time,
            'params_file': nav2_params_file,
            'autostart': autostart,
            'use_composition': use_composition,
            'use_respawn': use_respawn,
            'use_simulator': use_simulator,
            'use_robot_state_pub': use_robot_state_pub,
            'use_rviz': use_rviz,
            'headless': headless,
            'world': world,
            'rviz_config_file': rviz_config_file,
        }.items(),
    )

    ld = LaunchDescription()
    ld.add_action(declare_namespace_cmd)
    ld.add_action(declare_use_namespace_cmd)
    ld.add_action(declare_use_sim_time_cmd)
    ld.add_action(declare_params_file_cmd)
    ld.add_action(declare_autostart_cmd)
    ld.add_action(declare_use_composition_cmd)
    ld.add_action(declare_use_respawn_cmd)
    ld.add_action(declare_use_simulator_cmd)
    ld.add_action(declare_use_robot_state_pub_cmd)
    ld.add_action(declare_use_rviz_cmd)
    ld.add_action(declare_headless_cmd)
    ld.add_action(declare_world_cmd)
    ld.add_action(declare_rviz_config_file_cmd)
    ld.add_action(slam_launch)

    return ld
