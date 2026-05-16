import argparse
import sys
import time

import cv2

from src.lanedetector import process_frame


def open_video(source):
    try:
        src = int(source)
    except Exception:
        src = source
    return cv2.VideoCapture(src)


def main():
    parser = argparse.ArgumentParser(description="Run lane detection on webcam or video file")
    parser.add_argument("--source", "-s", default="0", help="Video source (0 for webcam or path to file)")
    parser.add_argument("--output", "-o", help="Optional output video file path")
    args = parser.parse_args()

    cap = open_video(args.source)
    if not cap.isOpened():
        print("Unable to open source:", args.source)
        sys.exit(1)

    writer = None
    if args.output:
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        fps = cap.get(cv2.CAP_PROP_FPS) or 20.0
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        writer = cv2.VideoWriter(args.output, fourcc, fps, (width, height))

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            out = process_frame(frame)
            cv2.imshow("Lane Detection", out)
            if writer:
                writer.write(out)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        if writer:
            writer.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
