import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
import math

BOUNDARY = {
    "xmin": -4.5,
    "xmax":  4.5,
    "ymin": -4.5,
    "ymax":  4.5,
}

class MowerController(Node):
    def __init__(self):
        super().__init__('mower_controller')

        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.create_subscription(Odometry, '/odom', self.odom_cb, 10)
        self.create_subscription(LaserScan, '/scan', self.scan_cb, 10)

        self.pose = None
        self.obstacle_close = False

        self.timer = self.create_timer(0.1, self.control_loop)

    def odom_cb(self, msg):
        self.pose = msg.pose.pose.position

    def scan_cb(self, msg):
        self.obstacle_close = any(r < 0.6 for r in msg.ranges if r > 0.0)

    def inside_boundary(self):
        if self.pose is None:
            return True
        return (
            BOUNDARY["xmin"] < self.pose.x < BOUNDARY["xmax"] and
            BOUNDARY["ymin"] < self.pose.y < BOUNDARY["ymax"]
        )


    def control_loop(self):

        cmd = Twist()

        if not self.inside_boundary():
            # Turn back into lawn
            cmd.angular.z = 0.8
        elif self.obstacle_close:
            # Obstacle avoidance
            cmd.angular.z = 0.6
        else:
            # Forward mowing motion
            cmd.linear.x = 0.4

        self.cmd_pub.publish(cmd)

def main():
    rclpy.init()
    node = MowerController()
    rclpy.spin(node)
    rclpy.shutdown()
