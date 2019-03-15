# coding=UTF-8
# @Author:Hilbert
# @Datetime:2019-3-13 17:48:40
# @Version: 1.0
# @File: filter.py
# @Description: This is implements big data to deduplication

'''
usage deduplication filter, This is support two style deduplication


usage Redis database and bloom filter algorithm, this is had error rate,
the algorithm can apply big data to dedeplication

'''

import mmh3
import math

class BloomFilter():
    # built-in one hundred seeds
    SEEDS = [543, 460, 171, 876, 796, 607, 650, 81, 837, 545, 591, 946, 846, 521, 913, 636, 878, 735, 414, 372,
             344, 324, 223, 180, 327, 891, 798, 933, 493, 293, 836, 10, 6, 544, 924, 849, 438, 41, 862, 648, 338,
             465, 562, 693, 979, 52, 763, 103, 387, 374, 349, 94, 384, 680, 574, 480, 307, 580, 71, 535, 300, 53,
             481, 519, 644, 219, 686, 236, 424, 326, 244, 212, 909, 202, 951, 56, 812, 901, 926, 250, 507, 739, 371,
             63, 584, 154, 7, 284, 617, 332, 472, 140, 605, 262, 355, 526, 647, 923, 199, 518]

    # capacity si precast need to amount of deduplication
    # error_rate is error rate
    # conn expression redis connect client
    # key expression prefix of name in redis

    def __init__(self, conn=None, capacity=1000000000, error_rate=0.00000001, key='BloomFilter'):
        self.m = math.ceil(capacity*math.log2(math.e)*math.log2(1/error_rate))
        self.k = math.ceil(math.log1p(2)*self.m/capacity)
        self.mem = math.ceil(self.m/8/1024/1024)
        self.blocknum = math.ceil(self.mem/512)
        self.seeds = self.SEEDS[0:self.k]
        self.key = key
        self.N = 2**31-1
        self.redis = conn

    def add(self, value):
        name = self.key + "_" + str(ord(value[0])%self.blocknum)
        hashs = self.get_hashs(value)
        for hash in hashs:
            self.redis.setbit(name, hash, 1)

    # already return true unexists return false
    def is_exist(self, value):
        name = self.key + "_" + str(ord(value[0])%self.blocknum)
        hashs = self.get_hashs(value)
        exist = True
        for hash in hashs:
            exist = exist & self.redis.getbit(name, hash)
        return exist

    def get_hashs(self, value):
        hashs = list()
        for seed in self.seeds:
            hash = mmh3.hash(value, seed)
            if hash >= 0:
                hashs.append(hash)
            else:
                hashs.append(self.N - hash)

        return hashs

'''
usage redis set to deduplication, This will occupy most memory, This is apply bit data, 1 000 000 0 id 
probably occupy 8000 M memory 
'''

class RedisFilter():

    def __init__(self, conn=None, key='RedisFilter'):
        self.redis = conn
        self.key = key

    def add(self, value):
        self.redis.sadd(self.key, value)

    # if exist it is return true , if not exist return false
    def is_exist(self, value):
        return self.redis.sismember(self.key, value)

if __name__ == "__main__":
    import redis

    pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)
    client = redis.StrictRedis(connection_pool=pool)


    rf = RedisFilter(client)
    rf.add('test')
    rf.add('fadfdf')

    print(rf.is_exist('test'))
    print(rf.is_exist('tefsdfsdgst'))
    print(rf.is_exist('fadfdf'))


    ''' 
    import time

    start = time.time()
    bf = BloomFilter(conn=client)
    bf.add('test')
    bf.add('fff')
    print(bf.is_exist('te2st'))
    print(bf.is_exist('testa'))
    end = time.time()
    print(end-start)
    '''