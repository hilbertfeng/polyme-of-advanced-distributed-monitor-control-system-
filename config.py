# coding:utf-8
# setting config, setting system need to database arguments

# Task setting
TASK_NAME = 'spider'
# Task result of return name of tackid  in dict
TASK_ID = 'id'
# Whether to enable auto start extend the function , for example to run a task ,
# it is parse tack of more
IS_NEXT = True
# Module of task name and path
TASK_MODULE = 'tasks.spider'
# more errors count
MAX_ERROR_NUMS = 10
# more than max error sleep time
ERROR_SLEEP = 30 * 60
# redis queue database setting
# redis, one of a kind system (redis single) or is a redis cluster(cluster)
QUEUE_REDIS_TYPE = "single"
QUEUE_REDIS_HOST = "127.0.0.1"
QUEUE_REDIS_PORT = 6379
QUEUE_REDIS_DB = 0
QUEUE_REDIS_PWD = ''
QUEUE_REDIS_NODES =[{"host":"127.0.0.1","port":"7000"},{"host":"127.0.0.1", "port":"7001"},{"host":"1270.0.0.1","port":"7002"},{"host":"127.0.0.1","port":"7003"}]

# It is yes or no the task result of return to save, if save it is calling
# save function of task to data introduction
IS_SAVE = True

# deduplication setting
# Whether to enable the deduplication function
IS_FILTER = True
# deduplication style, redis collections(set) deduplication or bloom filter algorithm bloom deduplication
FILTER_TYPE = 'set'
FILTER_REDIS_TYPE = 'single'
FILTER_REDIS_HOST = '127.0.0.1'
FILTER_REDIS_PORT = 6379
FILTER_REDIS_DB = 0
FILTER_REDIS_PWD = ''
#redis cluster node
FILTER_REDIS_NODES = [{"host":"127.0.0.1","port":"7000"},{"host":"127.0.0.1","port":"7001"},{"host":"127.0.0.1","port":"7002"},{"host":"127.0.0.1","port":"7003"}]
# If usage BloomFilter algorithm deduplication is precast know amount of deduplication and error percent
CAPACITY = 100000000
ERROR_RATE = 0.00000001

# redis-task setting, only is one of a kind system ,not support cluster, it si save every node,
# worker for information is not have cluster
RTASK_REDIS_HOST = '127.0.0.1'
RTASK_REDIS_POST = 6379
RTASK_REDIS_DB = 0
# RTASK_REDIS_PWD = None
RTASK_REDIS_PWD = ''
# RPC remote connect port
RPC_PORT = 5555
# remote RPC control authenticate password
RPC_PWD = ''


