import cv2
import numpy as np


def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def gaussian_blur(img, kernel_size=5):
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)


def canny(img, low_threshold=50, high_threshold=150):
    return cv2.Canny(img, low_threshold, high_threshold)


def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    if len(img.shape) > 2:
        channel_count = img.shape[2]
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    return cv2.bitwise_and(img, mask)


def average_slope_intercept(lines, y_min, y_max):
    left_lines = []
    right_lines = []
    for line in lines:
        for x1, y1, x2, y2 in line:
            if x1 == x2:
                continue
            slope = (y2 - y1) / (x2 - x1)
            intercept = y1 - slope * x1
            if slope < -0.3:
                left_lines.append((slope, intercept))
            elif slope > 0.3:
                right_lines.append((slope, intercept))

    def make_line(avg):
        slope, intercept = avg
        x1 = int((y_min - intercept) / slope)
        x2 = int((y_max - intercept) / slope)
        return [x1, y_min, x2, y_max]

    output = []
    if left_lines:
        left_avg = np.mean(left_lines, axis=0)
        output.append(make_line(left_avg))
    if right_lines:
        right_avg = np.mean(right_lines, axis=0)
        output.append(make_line(right_avg))
    return output


def draw_lines(img, lines, color=(0, 255, 0), thickness=8):
    if lines is None:
        return
    for line in lines:
        x1, y1, x2, y2 = line
        cv2.line(img, (x1, y1), (x2, y2), color, thickness)


def process_frame(frame):
    height, width = frame.shape[:2]
    gray = grayscale(frame)
    blur = gaussian_blur(gray, 5)
    edges = canny(blur, 50, 150)

    mask_vertices = np.array([
        [(0, height), (width * 0.48, height * 0.6), (width * 0.52, height * 0.6), (width, height)]
    ], dtype=np.int32)
    masked = region_of_interest(edges, mask_vertices)

    lines = cv2.HoughLinesP(masked, rho=1, theta=np.pi / 180, threshold=50, minLineLength=40, maxLineGap=150)
    line_img = np.zeros_like(frame)
    if lines is not None:
        averaged = average_slope_intercept(lines, int(height * 0.6), height)
        draw_lines(line_img, averaged)

    combo = cv2.addWeighted(frame, 0.8, line_img, 1.0, 0.0)
    return combo


if __name__ == "__main__":
    print("This module provides lane detection functions. Import and use process_frame().")
