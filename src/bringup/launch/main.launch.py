import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    # Set default values for arguments
    default_robot_name = "monoped"
    default_urdf_file = os.path.join(
        get_package_share_directory("description"), "urdf", "monoped.urdf"
    )
    default_world_file = os.path.join(
        get_package_share_directory("gazebo"),
        "worlds",
        "customizable_gravity.world",
    )

    # Declare launch arguments
    robot_name = LaunchConfiguration("robot_name", default=default_robot_name)
    urdf_file = LaunchConfiguration("urdf_file", default=default_urdf_file)
    world_file = LaunchConfiguration("world_file", default=default_world_file)

    # Create the launch description
    ld = LaunchDescription()

    # Include gazebo world launch file
    gazebo_world_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("bringup"),
                "launch",
                "load_world.launch.py",
            )
        ),
        launch_arguments=[("world_file", world_file)],
    )
    ld.add_action(gazebo_world_launch)

    # Include spawn entity launch file
    spawn_entity_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("bringup"),
                "launch",
                "spawn_entity.launch.py",
            )
        ),
        launch_arguments=[
            ("robot_name", robot_name),
            ("urdf_file", urdf_file),
        ],
    )
    ld.add_action(spawn_entity_launch)

    return ld
