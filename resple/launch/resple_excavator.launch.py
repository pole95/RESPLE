from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    config = PathJoinSubstitution(
        [FindPackageShare("resple"), "config", "resple_excavator.yaml"]
    )
    sim_time = ParameterValue(LaunchConfiguration("use_sim_time"), value_type=bool)
    return LaunchDescription([
        DeclareLaunchArgument("use_sim_time", default_value="false"),
        Node(package="resple", executable="RESPLE", name="RESPLE",
             parameters=[config, {"use_sim_time": sim_time}], output="screen"),
        Node(package="resple", executable="Mapping", name="Mapping",
             parameters=[config, {"use_sim_time": sim_time}], output="screen"),
    ])
