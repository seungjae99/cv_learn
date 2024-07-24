import cv2 as cv

# 이미지 읽기
img = cv.imread('porsche.png')

# 이미지가 제대로 읽혔는지 확인
if img is None:
    print("이미지를 읽어올 수 없습니다.")
else:
    # 자를 범위 지정 (y_start:y_end, x_start:x_end)
    y_start, y_end = 370, 900  # 세로 범위
    x_start, x_end = 70, 1850  # 가로 범위
    
    # 이미지 자르기
    img_cropped = img[y_start:y_end, x_start:x_end]
    
    # 잘린 이미지 저장
    cv.imwrite('porsche_cropped.png', img_cropped)
    
    # 잘린 이미지 출력
    cv.imshow('Cropped Image', img_cropped)
    cv.waitKey(0)
    cv.destroyAllWindows()