import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    # Set default values for arguments
    default_world_file = os.path.join(
        get_package_share_directory("gazebo"),
        "worlds",
        "customizable_gravity.world",
    )

    # Declare launch arguments
    world_file = LaunchConfiguration("world_file", default=default_world_file)

    # Add launch file to launch the world
    gazebo_world_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("gazebo_ros"), "launch", "gazebo.launch.py"
            )
        ),
        launch_arguments=[("world", world_file)],
    )

    # Create the launch description and populate
    ld = LaunchDescription()

    ld.add_action(DeclareLaunchArgument("world_file", default_value=default_world_file))

    ld.add_action(gazebo_world_launch)

    return ld
