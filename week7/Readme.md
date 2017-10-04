# Week 7
## Introduction
simple introduction week 7 setup

## Introducing Machine Learning
what is ML?
- Search Engines
- Image Recognition
- Voice Recognition
- Natural Language Processing
...etc

```
inputs -> [training data] -> outputs
```
'teach' machine ...

## Image Classification
![](https://github.com/genexu/cs50x2017/blob/master/week7/Screenshot-2016-fall-lectures-7-at-12m35s.png)

labeled training set
test point
minimal distance
learest neighbor classifier
![](https://github.com/genexu/cs50x2017/blob/master/week7/Screenshot-2016-fall-lectures-7-at-16m53s.png)

## flatland
https://www.youtube.com/watch?v=C8oiwnNlyE4

## lineland, flatland, spaceland, and beyond
![](https://github.com/genexu/cs50x2017/blob/master/week7/Screenshot-2016-fall-lectures-7-at-20m9s.png)
images <=> pixel

1d => b - a
2d => sqrt(a^2 + b^2)
3d => sqrt(a^2 + b^2 + c^2)
...
32d

## introducing Python
```
~$ python 
>>> x = 3
>>> y = 5
>>> x + y
8
>>> x = 'a'
>>> y = 'b'
>>> x + y
'ab'
```

```
>>> for i in [3, 5, 7]:
... 	print(i)
...
3
5
7
```

## Supervised Learning
classifying points

import python modules:
- numpy
- satpiotlib.pyplot

```
create training set, containing points and labels (colors):
x_train = np.array [...] point
y_train = np.array [...] color

we can think of x_train as a two demensional array

print(x_train[5,0])
print(x_train[5,1]

slicing
print(x_train[:, 0])
print(x_train[:, 1])

plt.figure()
plt.scatter(x.train[:, 0], x_train[:, 1], s = 170, color = t_train[:])
plt.show()

x_test = np.array [...] point
plt.scatter(x.train[:, 0], x_test[:, 1], s = 170, color = 'green')

np.sqrt(np.sum((x - y)**2)) ??
x = [1, 1]
y = [3, 4]
x - y = [-2, -3]
(x - y)**2 = [4, 9]
np.sum((x - y)**2) = 13
np.sqrt(np.sum((x - y)**2)) = 3.60

for loop each and compare dist each point with test point
```
## python for image classification
```
from sklearn import datasets
digits = datasets.load_digits()
```
...
how many data set <=> error rate ??

Note: The CIFAR-10 dataset
picture issue
- color?
- viewpoint?
...

## Deep Learning
- Feature Representation
3rd layer 'Object'
|
V
2nd layer 'Object parts'
|
V
1st layer 'Edges'
|
V
pixel

!!! TensorFlow !!!

## Deep learning in car
95% currect enough?
Tesla
[Video]

## Text Clustering
how to divivel text?
group unlabeled data?

spilt and map each string
=> Bags of words
![](https://github.com/genexu/cs50x2017/blob/master/week7/Screenshot-2016-fall-lectures-7-at-1h11m18s.png)

## Wran-Up
recap lesson  
[Video]

## Outro
[Video]
