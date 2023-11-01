# 该代码已不再更新，更多功能请转 https://github.com/Jv0id/telegram-wikipedia 


# Groupwiki


适用于Telegram群的维基百科搜索机器人

在Telegram群中，可以透过:

```
江泽民
```

语法进行搜索维基百科。

# 安装

```bash
pip3 install -r requirements.txt
cp config.example.py config.py
```

修改`config.py`中的`TOKEN`字段为你的机器人的Token

然后运行机器人:

```bash
python3 bot.py
```

另外，你可以透过`pm2`来守护本进程，只需在专案目录执行:

```bash
pm2 start
```

即可看到一个名为`groupwiki`的任务

## License
[MIT](https://choosealicense.com/licenses/mit/)
