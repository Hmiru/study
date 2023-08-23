
import numpy as np
from keras.models import load_model
import keras.utils as image
def image_input(image_path):
  # 1. 이미지 준비
  image_path = '/content/drive/MyDrive/IMG_0367.jpg'  # 테스트하려는 이미지 파일 경로
  img = image.load_img(image_path, target_size=(135, 240))  # 이미지 로드 및 크기 조정
  img_array = image.img_to_array(img)  # 이미지를 NumPy 배열로 변환
  img_array = np.expand_dims(img_array, axis=0)  # 배치 차원 추가

  mean=np.mean(img_array,axis=(0,1,2,3))
  std=np.std(img_array,axis=(0,1,2,3))
  img_array=(img_array-mean)/(std+1e-7)
  return img_array