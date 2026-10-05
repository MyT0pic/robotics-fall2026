# mission_2 Submission

- Name: Oscar Pan
- Section: (not provided)

## Explanations

### prediction

If the forward pod scale is too large, then the robot will overestimate the actual traveled distance in the x-direction. Meanwhile, if the strafe pod scale is too small, then the robot will underestimate the distance traveled in the y-direction.

### calibration_analysis

I predicted that the forward pod scale being too large would lead to overestimation of the traveled distance which would requires the distance measurement per tick to be decreased lightly to reduce the error for the y-direction. While, the strafe pod scale being too small would lead to a underestimation of the traveled distance which would requires the distance measurement per tick to be increased lightly to reduce the error for the x-direction. The sideways pod is necessary to measure distance traveled in the x-direction. Even after tuning and calibrating, there still exists some drift because it's difficult to find the tuning needed to reduce the error as much as possible, but even then, there's environmental factor and friction involved which can lead to some drift or error in odometry measurements.