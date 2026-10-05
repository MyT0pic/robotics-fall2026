# mission_1 Submission

- Name: Oscar Pan
- Section: (not provided)

## Explanations

### prediction

With too little Kp, I predict that the arm will slowly or maybe not even able to raise the arm at all to a certain position. Additionally, if the Kd is too low, then the arm will not be able to slowly come to a rest or hold onto a specific position with the elbow oscillating around a position.

### tuning_analysis

For both the shoulder and elbow controllers, the Kp is decreased to 1.1 and Kd is decreased to 0.5. Based on the visual, the shoulder joint constantly overshoots and undershoots in its oscillations which matches with my initial prediction of oscillation movement of the arm. As for the elbow joint, it also exhibits the same behavior as predicted. The gravity compensation seems to make the Kp and Kd component of the PID controller a lot more aggressive.