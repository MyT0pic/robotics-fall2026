#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PointStamped
import tf2_ros
from tf2_geometry_msgs import do_transform_point


class CameraPointToBaseLink(Node):
    def __init__(self):
        super().__init__('camera_point_to_base_link')

        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(
            self.tf_buffer, self
        )

        self.point_sub = self.create_subscription(
            PointStamped,
            '/hallway_camera/point',
            self.point_callback,
            10
        )

        self.point_pub = self.create_publisher(
            PointStamped,
            '/point_base_link',
            10
        )

    def point_callback(self, point_camera: PointStamped):
        try:
            # Look up the transform from the point's frame
            # (e.g. hallway_camera_optical_frame) to base_link.
            transform = self.tf_buffer.lookup_transform(
                'base_link',
                point_camera.header.frame_id,
                tf2_ros.Time(
                    seconds=0,
                    nanoseconds=0
                )
            )

            # Transform the point into base_link.
            point_base = do_transform_point(
                point_camera,
                transform
            )

            self.point_pub.publish(point_base)

            self.get_logger().info(
                f'Point in base_link: '
                f'x={point_base.point.x:.3f}, '
                f'y={point_base.point.y:.3f}, '
                f'z={point_base.point.z:.3f}'
            )

        except (
            tf2_ros.LookupException,
            tf2_ros.ConnectivityException,
            tf2_ros.ExtrapolationException
        ) as e:
            self.get_logger().warn(
                f'Could not transform point to base_link: {e}'
            )


def main(args=None):
    rclpy.init(args=args)

    node = CameraPointToBaseLink()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
