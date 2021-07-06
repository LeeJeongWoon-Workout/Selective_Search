cand_rects = [cand['rect'] for cand in regions if cand['size'] > 10000]

'''
-----------------------------------
bbox의 크기가 1000인 것들만을 분류한다.'''


green_rgb = (125, 255, 51)
img_rgb_copy = img_rgb.copy()
for rect in cand_rects:
    
    left = rect[0] #좌상단 x 좌표
    top = rect[1]  #좌상단 y 좌표
    # rect[2], rect[3]은 너비와 높이이므로 우하단 좌표를 구하기 위해 좌상단 좌표에 각각을 더함. 
    right = left + rect[2] #우상단 x 좌표에서 너비를 더해야 한다.
    bottom = top + rect[3] #우상단 y 좌표에서 height를 더해야 한다.
    
    img_rgb_copy = cv2.rectangle(img_rgb_copy, (left, top), (right, bottom), color=green_rgb, thickness=2)
    
plt.figure(figsize=(8, 8))
plt.imshow(img_rgb_copy)
plt.show()
