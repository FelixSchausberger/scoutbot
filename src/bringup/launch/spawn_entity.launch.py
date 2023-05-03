import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    # Set default values for arguments
    default_robot_name = "monoped"
    default_urdf_file = os.path.join(
        get_package_share_directory("description"), "urdf", "monoped.urdf"
    )

    # Declare launch arguments
    robot_name = LaunchConfiguration("robot_name", default=default_robot_name)
    urdf_file = LaunchConfiguration("urdf_file", default=default_urdf_file)

    # Add robot spawn node
    robot_spawn_node = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        namespace="/monoped",
        arguments=[
            "-robot_namespace",
            robot_name,
            "-entity",
            robot_name,
            "-file",
            urdf_file,
            "-x",
            "0",
            "-y",
            "0",
            "-z",
            "1",
        ],
        output="screen",
    )

    # Create the launch description and populate
    ld = LaunchDescription()

    ld.add_action(DeclareLaunchArgument("robot_name", default_value=default_robot_name))
    ld.add_action(DeclareLaunchArgument("urdf_file", default_value=default_urdf_file))

    ld.add_action(robot_spawn_node)

    return ld
