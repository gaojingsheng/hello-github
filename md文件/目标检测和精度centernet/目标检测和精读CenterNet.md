# 目标检测和精读CenterNet

## 目标检测

**定义：**一种基于目标几何和统计特征的图像分割，它将目标的分割和识别合二为一，其准确性和实时性是整个系统的一项重要能力。尤其是在复杂场景中，需要对多个目标进行实时处理时，目标自动提取和识别就显得特别重要。

### 传统检测算法

滑动窗口对整幅图像进行遍历，穷举所有目标可能出现的位置，然后用SIFT忽然HOG等方法进行特征提取，最后对提取出来的特征用SVM和AdaBoost等进行分类。

### 深度学习检测算法思路

根据检测思路主要可分为One-Stage和Two-Stage的目标检测算法。目标检测任务可分为两个关键的子任务：目标分类和目标定位。目标分类判断所选区域是否有相关类别物体的出现，输出相关物体出现在所选区域的可能性。目标定位则是确定所选范围内物体的位置和范围，输出物体的中心和边界等，一般用bounging Box来表示。

### One-Stage

通过一个Stage直接产生物体的类别概率和位置坐标值，比较典型的算法有YOLO、SSD和CornerNet、CenterNet。

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200717142808871.png" alt="image-20200717142808871" style="zoom:67%;" />

#### loss

因为目标检测包括两个子任务，分为物体分类和物体定位，因为损失也主要包括分类损失和定位损失

其中yolo系列相比于SSD系列多了一个物体损失，就是判断对应区域是否为物体的损失。

### Two-Stage

第一个阶段首先产生候选区域（Region Proposals），包含目标大概的位置信息，然后第二个阶段对候选区域进行分类和位置精修，这类算法的典型代表有R-CNN，Fast R-CNN，Faster R-CNN等。

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200717150305348.png" alt="image-20200717150305348" style="zoom:67%;" />

## CenterNet

CenterNet可认为是基于CornerNet改进的，他们两都属于One-Stage方法，CornerNet是将要检测的BoundingBox改为了关键点，也就是一个目标框可以由两个点（左上角和右下角）来表示，直接预测这两个点就能生成相应的BoundingBox。而CenterNet则是检测中心点的位置再返回每个BoundingBox的长宽就能得到每个BoundingBox。对于3D目标，还会回归到3D位置、尺寸、方向甚至是姿态。

### 创新点

没有手动设置进行前景和后景分类，没有尺寸框。

每个目标只有一个正确的中心锚点。

使用了更大分辨率的输出特征图。只下采样额四倍512-128

### 和其他关键点估计方法对比

之前有CornerNet检测两个角和ExtremeNet检测最上，最下，最左，最右和中心点；这些网络需要金国一个关键点grouping阶段，只有一个关键点就不需要聚类了。

### 预处理

对于特征点通过高斯核分散到热力图上，中心点检测的loss如下

![center_focalloss](C:\Users\Administrator\Desktop\center_focalloss.png)

其中α和β都是超参数，不需要自己设置，选择设置为2和4

由于图像点是离散的，所以在下采样会产生偏差，加入L1 offsetloss来训练;为每个目标使用单一的尺寸预测，在中心点添加了LI sizeloss。

![image-20200717171234595](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200717171234595.png)

最终loss如上，超参数分别为0.1和1。

### 多任务

#### 3D检测

加入一个深度计算通道，也是用L1loss来训练深度估计器。

#### 人体姿态估计

估计K个人体关节带你热力图，然后为每个关节点分配给其最近的人。同时在loss中添加mask来五十那些不可见的关节点。

### 多结构

ResNet-18,ResNet-101,DLA-34,Hourglass-104。Hourglass网络较大，但通常会生成最好的关键点估计。

![image-20200717174801401](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200717174801401.png)