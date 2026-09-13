# Mission 2

## Measurement Explanation

The estimated traveled path distance measurement differs from the start-to-end distance measurements because the odometry can't perfectly measure and adjust to curved motions.

## Motion Comparison

In the rotation live simulation, the live motion result is almost as I initially predicted because  the start-to-end distance is 0m matching with my prediction of the robot remaining in the same position, and the 20 degrees change matched my expectation of the robot turning left.

## Prediction Locks

{'straight': '2026-09-11T23:30:21.408170+00:00', 'rotation': '2026-09-12T00:15:22.988419+00:00', 'curve': '2026-09-12T00:28:28.817907+00:00', 'curve_modified': '2026-09-12T00:33:32.506748+00:00'}

## Predictions

{'straight': 'I predict that the robot will move forward 0.45m from its initial position.', 'rotation': "The robot's position will remain in place, while its direction will shift 1.5 radians to the left.", 'curve': 'I predict that the robot will move in a forward-right direction in an arc.', 'curve_modified': 'This path differs from the first curved trial because the robot will turn to the left due to the positive radian/s velocity, and a tighter curve due to the higher |turning speed|.'}

## Safety Explanation

The command guard checks every proposed instruction to make sure that it's reasonable within the current context before finalizing the instruction to the robot. The final zero command stops both the robot's velocity and angular turning to flag the completion of the task. The stale-command timeout sends out a stop command to stop the robot after 0.5s if the robot is in motion with no new instructions being received due to either no communication or program crashes. 

## Modified Settings

{'linear_x': 0.15, 'angular_z': 0.8, 'duration': 4.0}
