# Microphone Properties

## Energy Threshold
The energy threshold, also known as the "silence threshold," is a parameter used to detect the presence of audio signals above a certain energy level. It is used to determine when the microphone should start recording audio. If the ambient noise level is below the energy threshold, the microphone will not record any audio until it detects a sound that exceeds this threshold. Setting an appropriate energy threshold is essential to avoid capturing background noise unnecessarily and to trigger recording only when someone starts speaking.

## Sample Rate
The sample rate represents the number of audio samples recorded per second. It indicates how frequently the microphone captures audio data. A higher sample rate generally results in better audio quality but can require more computational resources. On the other hand, a lower sample rate may reduce audio quality but consumes fewer resources. The appropriate sample rate to use depends on the application and the desired balance between audio quality and efficiency.

## Adjust for Ambient Noise
Ambient noise refers to the background noise present in the environment while recording audio. The `adjust_for_ambient_noise()` method is used to calibrate the energy threshold for ambient noise. It captures a short segment of audio from the microphone and calculates the average energy level, which is then used to adjust the energy threshold. This calibration process helps improve the accuracy of speech recognition, especially in noisy environments.

## Non-Speaking Duration
The non-speaking duration is the period of silence required to consider the end of a spoken phrase. After the microphone starts recording due to detecting audio above the energy threshold, it continues to record until the specified duration of silence is detected. Setting an appropriate non-speaking duration is crucial to avoid cutting off spoken phrases prematurely and to ensure that the entire speech is captured.

## Timeout
The timeout represents the maximum time the `listen()` method waits for audio input from the microphone before raising a `TimeoutError`. This parameter is useful when you want to set a limit on how long the microphone should listen for speech. It prevents the program from hanging indefinitely if there is no audio input.

## Phrase Time Limit
The phrase time limit sets the maximum duration allowed for the speech recognition process. If the time taken for the speech recognition exceeds this limit, the recognition process is terminated, and an error may be raised. It is useful to set a time limit to control the response time of the speech recognition and to prevent the program from getting stuck during extended recognition attempts.
