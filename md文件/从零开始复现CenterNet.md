# 从零开始复现CenterNet

## 准备数据集

### COCO数据集

目前为止有语义分割的最大数据集，提供的类别有80 类，有超过33 万张图片，其中20 万张有标注，整个数据集中个体的数目超过150 万个。



python test.py ctdet --exp_id coco_dla --keep_res --load_model ../models/ctdet_coco_dla_2x.pth

![image-20200721125908794](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200721125908794.png)



#### 目前训练

CUDA_VISIBLE_DEVICES=6

python main.py ctdet --exp_id coco_dla --batch_size 4 --master_batch 15 --lr 1.25e-4  --gpus 6



### Pascal VOC数据集

首先在tools文件夹中bash get_pascal_voc.sh

http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar

http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCdevkit_18-May-2011.tar

### KITTI数据集



## 代码细节

