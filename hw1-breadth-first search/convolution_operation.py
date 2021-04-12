import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def convolution2D(image2D, kernel3x3):

  padding = 0
  strides = 1
  xKernShape = kernel3x3.shape[0]
  yKernShape = kernel3x3.shape[1]
  xImgShape = image2D.shape[0]
  yImgShape = image2D.shape[1]

  # Shape of Output Convolution
  xOutput = int(xImgShape - xKernShape)
  yOutput = int(yImgShape - yKernShape)
  convolved2D = np.zeros((xOutput, yOutput))
  convolved2D = np.zeros((len(image2D) - 2, len(image2D) - 2))

  # Iterate through image
  for y in range(image2D.shape[1]):
    # Exit Convolution
    if y > image2D.shape[1] - yKernShape:
      break
    # Only Convolve if y has gone down by the specified Strides
    if y % strides == 0:
      for x in range(image2D.shape[0]):
        # Go to next row once kernel is out of bounds
        if x > image2D.shape[0] - xKernShape:
          break
        try:
          # Only Convolve if x has moved by the specified Strides
          if x % strides == 0:
            convolved2D[x, y] = (kernel3x3 * image2D[x: x + xKernShape, y: y + yKernShape]).sum()
        except:
          break


  return convolved2D

image2D = np.loadtxt('my-cat.csv', delimiter=',')
sns.heatmap(image2D, cmap='gray')
plt.title('Original image - Size = ' + str(image2D.shape))
plt.show()

edge_detect_filter_3x3 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

for i in range(2):
  convolved_image = convolution2D(image2D, edge_detect_filter_3x3)
  sns.heatmap(convolved_image, cmap='gray')
  plt.title('Convolution iteration ' + str(i) + ' - Size = ' + str(convolved_image.shape))
  plt.show()
  image2D = convolved_image