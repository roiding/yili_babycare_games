<p align="center"><img src="https://github.com/roiding/yili_babycare_games/actions/workflows/docker.yml/badge.svg"/></p>

****

## 冰墩墩-伊利积分游戏

为了方便自己不再需要用postman一次次的做游戏，写了个简易版的游戏脚本



本程序需要一定的网络基础才能实施，主要是需要用户获取到自己的Authorization值（鉴权值，懂得应该都懂把）



用户进入小程序注册完后，想办法抓包（此处懂得自懂，为了避免麻烦，我就不科普了，方法多种多样）自己的请求，获得Authorization值后执行脚本即可







<p style="font-size:200%;color:red">不是专门写python的，就是为了图省事，边百度各种函数用法边写的，写的烂别喷</p>



<p style="font-size:300%;color:blue">有大能的话，可以帮忙把Authorization自动获取也做个补充</p>

### 已更新Docker版本

### 已更新库存监控

* AUTHORIZATION 为游戏权限
* SENDKEY为大哥们的[Server酱](https://sct.ftqq.com/)的SendKey，懂得都懂，我就不说咋生成了
  * 两个可以都写 也可以只用其中一个功能


```bash
docker run -d -e AUTHORIZATION=XXXX -e SENDKEY=XXXX ghcr.io/roiding/yili-babycare-game:latest
```

