BOT_NAME = 'creditofondiario'

SPIDER_MODULES = ['creditofondiario.spiders']
NEWSPIDER_MODULE = 'creditofondiario.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'creditofondiario.pipelines.CreditofondiarioPipeline': 100,

}