from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # 1. Path to Sim Launch (Gazebo World)
    sim_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('mower_sim'),'launch','sim.launch.py')
        )
    )

    # 2. Path to Mower Launch (Mower URDF)
    mower_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('mower_description'), 'launch', 'mower.launch.py')
        )
    )

    # 3. Path to Controller Node
    controller_node = Node(
        package='mower_control',
        executable='mower_controller',
        output='screen'
    )

    return LaunchDescription([
        sim_launch, 
        mower_launch,
        controller_node
    ])
