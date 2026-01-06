from launch import LaunchDescription
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    mower_sim_dir = get_package_share_directory('mower_sim')
    world_path = os.path.join(mower_sim_dir, 'worlds', 'lawn.world')

    return LaunchDescription([
        ExecuteProcess(
            cmd=[
                'gazebo',
                '--verbose',
                world_path,
                '-s', 'libgazebo_ros_factory.so'
            ],
            output='screen'
        ),
    ])
