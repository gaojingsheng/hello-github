# CenterNet

CenterNet检测的是中心点，然后返回每个bounding box的长宽就能得到结果，不再策略搜索所有的bounding box。

## Loss

借鉴到十二骨骼点的检测，我们只需要借鉴检测中心点的部分，该文中使用的loss是一种修正的focal loss，**focal loss**本身就是从二分类的交叉熵损失修改而来。

![center_focalloss](C:\Users\Administrator\Desktop\center_focalloss.png)

其中α和β都是超参数，不需要自己设置，选择设置为2和4

## Realize pytorch

在pytorch中使用eq可以返回[[False False...True...False]...]可以作为索引

##### 骨骼节点的heatmap也是最大值为1的高斯核，所以可以无缝衔接这个loss。

## Other ways

可以考虑openpose人体骨骼点提取的方法