# 链家网二手房房价预测模型
SJTU-IS303-数据挖掘 课程设计

商进秩 519030910174

贾睿辰 519030910164

## 项目简介
本项目采用链家网2022年6月17日爬取的二手房数据建立模型，预测上海地区二手房房价。

## 项目目录
```
base
│  main.py                  // 主程序入口
│  requirements.txt
│ 
├─data
│      count_fitment.png    // 测试图形
│      ershoufang.csv       // 爬取的原始数据
│      model_count.png      // 测试图形
│      rawdata.csv          // 原始数据备份
│      res.csv              // 预处理得到的结果
│      spider.py            // 爬虫文件
│      test.csv             // 测试文件
│      
├─pretreatment
│  │  address.py            // 处理属性address
│  │  direction.py          // 处理属性direction
│  │  fitment.py            // 处理属性fitment
│  │  model.py              // 处理属性model
│  │  overview.py           // 浏览csv相关信息
│  │  pretreat.py           // 预处理函数入口
│  │  transform.py          // 字符串数字化
│  │  
│  └─__pycache__
│          
├─train
│  │  train.py              // 训练函数入口
│  │  
│  └─__pycache__
│          
└─venv
```

## 启动方法
运行main.py文件即可启动