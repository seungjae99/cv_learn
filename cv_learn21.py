# line detection

import cv2 as cv
import numpy as np

# 이미지 읽기
img = cv.imread("road.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 블러링
blr = cv.GaussianBlur(gray, (5, 5), 0)  # 커널 사이즈와 sigma 값 조정

# 엣지 검출
edges = cv.Canny(blr, 100, 200)

# 이미지 크기 가져오기
height, width = edges.shape

# ROI (Region of Interest) 정의: 사다리꼴 모양의 범위만 detection하자
roi_vertices = np.array([[(int(width // 2), int(3 * height // 5)),   # 이미지의 왼쪽 중앙
                          (int(width // 2), int(3 * height // 5)), # 이미지의 오른쪽 중앙
                          (width, height),      # 이미지의 오른쪽 하단
                          (0, height)           # 이미지의 왼쪽 하단
                          ]], dtype=np.int32)

# 마스크 생성
mask = np.zeros_like(edges)
cv.fillPoly(mask, roi_vertices, 255)

# ROI 영역에 대해서만 엣지 이미지와 차선 검출 수행
roi_edges = cv.bitwise_and(edges, mask)

# 차선 검출(modify)
lines = cv.HoughLinesP(roi_edges, 1, np.pi / 180, 25, None, 20, 5)

# 원본 이미지에 차선 그리기
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

# 결과 이미지 표시
cv.imshow('Canny Edge', edges)
cv.imshow('ROI Edge Detection', roi_edges)
cv.imshow('Line Detection', img)

cv.waitKey(0)
cv.destroyAllWindows()

