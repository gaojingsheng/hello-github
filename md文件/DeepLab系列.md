# DeepLab系列

## Deeplab v1

空洞卷积和CRF

#### 空洞卷积：dilated conv

在FCN之类的传统卷积操作一般是进行下采样（扩大感受野）再上采样（恢复到原来的尺寸）。在pooling的操作过程中会丢失一部分信息，于是就有了空洞卷积代替下采样和上采样，直接增大感受野。

![image-20200810161411655](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200810161411655.png)

#### CRF

在FCN粗分割的基础上，对得到的不同特征进行条件随机场处理，应该就是不同特征出现在一块的概率进行赋予一个权重。

## DeepLab V2

#### ASPP(空间金字塔)

由SPP的结构启发而来，SPP就是对不同尺寸大小的特征图生成固定大小的输出。ASPP通过获得不同rate下不同的空洞卷积所获得的特征，然后取像素点位置最大响应的结果

#### 基础特征网络由VGG变成了Resnet

## DeepLab V3

1、在ASPP的基础上进行串联，获得不同的感受野结果。

2、空洞卷积越大的时候，卷积的有效权重越小，在最后一层前加入average pooling来处理不同尺度的结果。

## DeepLab V3+

![image-20200810174600763](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200810174600763.png)

1、将不同尺度的encoder-decoder融合到deep lav v3

2、将空洞卷积变为深度空洞卷积（保持性能减少计算量）

下图为网络结构

![image-20200810175244750](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200810175244750.png)

# 遮挡问题

遮挡问题一般分为目标遮挡和非目标遮挡，在图像分割的问题上，只存在目标遮挡的情况。