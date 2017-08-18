# -*- coding:utf-8 -*-
"""架构"""

# 平台
class TextProcessor(object):
    PLUGINS = {}

    @classmethod
    def plugin_register(cls, plugin_name):
        def wrapper(plugin):
            cls.PLUGINS.update({plugin_name:plugin})
        return wrapper


# 插件
@TextProcessor.plugin_register('plugin1')
class CleanMarkdownBolds(object):
    pass


processor = TextProcessor()
print(processor.PLUGINS)
