from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    urdf_path = os.path.join(
        get_package_share_directory('mower_description'),
        'urdf',
        'mower.urdf'
    )

    return LaunchDescription([
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-entity', 'mower',
                '-file', urdf_path,
                '-x', '1.8',
                '-y', '0.5',
                '-z', '0.5'
            ],
            output='screen'
        )
    ])
