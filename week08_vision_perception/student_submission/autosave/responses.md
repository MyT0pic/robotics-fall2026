# Lab 7 saved answers

## mission_1.diagnosis
Take the test case dim_1 for example, the detector fails to box on the mug because after the masking shows a majority of blacks pixels around the cup, and the contour table shows candidate 15, surface of the table, shows the largest of white pixels which is most likely due to a combination of high contrast and lack of brightness in the preprocessing phase. While in the test case occluded_1, the detector fails to box the mug because it's due to the nonexistence of smoothing within the preprocessing that cause the contours table to fail to identify any candidates at all.

## mission_1.limitations
During practice, the contrast parameter has been increased to 1.5x. As a result, in a relatively bright scene, there's less small clusters of white pixels after masking because fewer pixels fail to pass the minimum 40 value threshold. In a dark or dim environment, just the contrasts alone, less pixels on the cup will pass the threshold masking which makes the detector more likely to fail to box the mug within the scene.
