#!/usr/bin/env python3

import rospy
import cv2

class Camera_node:
    def __init__(self):
        rospy.init_node('camera', anonymous=False)
        self.vid = cv2.VideoCapture(0)

        # Define output video properties
        self.frame_width = int(self.vid.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.fps = 30
        self.codec = cv2.VideoWriter_fourcc(*'H264')
        self.output_file = 'output.mp4'
        self.video_writer = cv2.VideoWriter(self.output_file, self.codec, self.fps, (self.frame_width, self.frame_height))

    def main_control(self):
        while True:
            ret, frame = self.vid.read()

            self.video_writer.write(frame)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        self.vid.release()
        self.video_writer.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    CN = Camera_node()
    r = rospy.Rate(60)
    while not rospy.is_shutdown():
        CN.main_control()
        r.sleep()


