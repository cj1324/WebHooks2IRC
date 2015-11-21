## WebHooks2IRC

[![Build Status](https://travis-ci.org/cj1324/WebHooks2IRC.svg?branch=develop)](https://travis-ci.org/cj1324/WebHooks2IRC)

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

+ GitLab-CI 相关hooks支持.
+ 彩色化输出内容到IRC。
+ 通过 GitLab API 获取推送内容中部分 id 的名称
+ 支持发送私聊消息。
+ 相关BUG修正
+ 相关测试用例
+ Dockerfile编写

# CHANGELOG

+ v0.1.1 2015-11-21
  + 一些BUG修复
  + 关键测试用例编写。
  + travis-ci 集成
  + 发布 v0.1.1

+ v0.1.0 2015-11-21
  + 模版渲染异常处理
  + 加入完整的模版
  + 发布 v0.1.0

+ v0.1.0 2015-11-20
  + irc 通讯
  + mako 渲染消息
  + 相关模块规范化.
  + 整个流程走通

+ v0.1.0 2015-11-19
  + 主体框架搭建
  + bottle 提供web服务

# LICENSE

+  BSD 2-clause "Simplified" License
