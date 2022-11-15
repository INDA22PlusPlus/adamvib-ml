from mnist import MNIST

mndata = MNIST('./mnist_data_files')
mndata.gz = True

images, labels = mndata.load_training()