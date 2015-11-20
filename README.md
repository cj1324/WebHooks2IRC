## WebHooks2IRC

GitLab Web Hooks to IRC

实现GitLab Web Hooks的推送的数据进行模版渲染，然后发送到指定的IRC频道

# USAGE

+ 配置 settings.py
+ 安装相关的依赖库(推荐virtualenv)
+ 运行 Bottle 提供的web服务
+ 在 GitLab 中配置对应Hooks地址
+ 测试 Web Hooks
+ 确认 IRC 是否收到对应消息。

# FUTURE

+ 相关BUG修正
+ 编写各类 Event 模版.
+ 相关测试用例
+ Dockerfile编写
+ 发布 v0.1.0

# CHANGELOG

+ v0.1.0 2015-11-21
  + irc 通讯
  + mako 渲染消息
  + 相关模块规范化.
  + 整个流程走通

+ v0.1.0 2015-11-20
  + 主体框架搭建
  + bottle 提供web服务

# LICENSE

+  BSD 2-clause "Simplified" License
