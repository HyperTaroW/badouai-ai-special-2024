from tensorflow.keras.datasets import mnist
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()


#digit = test_images[0]
#plt.imshow(digit, cmap=plt.cm.binary)
#plt.show()

network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28*28,)))
network.add(layers.Dense(10, activation='softmax'))

network.compile(optimizer='rmsprop', loss='categorical_crossentropy',
               metrics=['accuracy'])

train_images = train_images.reshape((60000, 28*28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28*28))
test_images = test_images.astype('float32') / 255


train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

network.fit(train_images, train_labels, epochs=5, batch_size = 128)

test_loss, test_acc = network.evaluate(test_images, test_labels, verbose=1)
print(test_loss) 
print('test_acc', test_acc)

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
number=[]

test_images = test_images.reshape((10000, 28*28))
res = network.predict(test_images)
for j in range(9):
    for i in range(res[j].shape[0]):
        if (res[j][i] == 1):
            number.append(i)
            break
print("The numbers are:",number)
for i in range(9):
    plt.subplot(3,3,i+1)
    digit = test_images[i].reshape(28, 28)
    plt.imshow(digit,cmap=plt.cm.binary)
plt.show()

input("Press Enter to exit...")
