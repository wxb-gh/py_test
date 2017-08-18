from ..platform import TextProcessor
@TextProcessor.plugin_register('plugin3')
class CleanMarkdownzidingyi(object):
    def process(self, text):
        return text.replace('++', '')
