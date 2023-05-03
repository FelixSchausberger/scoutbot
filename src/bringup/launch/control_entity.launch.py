import os
from ament_index_python.packages import get_package_share_directory
import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    monoped_config = launch.substitutions.LaunchConfiguration(
        "monoped_config",
        default=os.path.join(
            get_package_share_directory("description"),
            "config",
            "monoped.yaml",
        ),
    )

    robot_state_publisher = launch_ros.actions.Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        name="robot_state_publisher_monoped",
        parameters=[
            {"publish_frequency": 30.0},
            {"ignore_timestamp": True},
            {"tf_prefix": "monoped"},
        ],
        remappings=[("/joint_states", "/monoped/joint_states")],
    )

    controller_spawner = launch_ros.actions.Node(
        package="controller_manager",
        executable="spawner",
        name="controller_spawner",
        arguments=[
            "--namespace=/monoped",
            "joint_state_controller",
            "haa_joint_position_controller",
            "hfe_joint_position_controller",
            "kfe_joint_position_controller",
            "--shutdown-timeout",
            "3",
        ],
    )

    return launch.LaunchDescription(
        [
            launch.actions.DeclareLaunchArgument(
                "monoped_config",
                default_value=monoped_config,
                description="Path to the monoped YAML config file",
            ),
            launch.actions.ExecuteProcess(
                cmd=["ros2", "param", "load", "/description", monoped_config],
                output="screen",
            ),
            robot_state_publisher,
            controller_spawner,
        ]
    )
