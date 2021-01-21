from kafka import KafkaConsumer, TopicPartition
from peewee import Model, CharField, IntegerField, DateTimeField,fn
import peewee
import logging
from multiprocessing import Process
ex_mysql = peewee.MySQLDatabase(
        "kafka",
        host="localhost",
        user="root",
        passwd="Levinh6112001;")


class BaseModel(Model):
    class Meta:
        database = ex_mysql

class Checkpoint(BaseModel):
    id = IntegerField(primary_key=True)
    final_offset = IntegerField()
    final_timestamp = IntegerField()
    time = DateTimeField()

    @classmethod
    def search_max(cls):
        data = cls.select(cls.time) \
        .where(cls.time == cls.select(fn.MAX(cls.time))).dicts()
        return [i for i in data]

class Data(BaseModel):
    id = IntegerField(primary_key=True)
    topic = CharField()
    partition = IntegerField()
    offset = IntegerField()
    timestamp = IntegerField()
    timestamp_type = IntegerField()

    @classmethod
    def search_max_offset(cls, partition):
        data = cls.select(cls.offset, cls.partition).where(cls.offset == cls.select(fn.MAX(cls.offset)).where(cls.partition == partition)).dicts()
        return [i for i in data]

class GetConsumer:
    def __init__(self,bootstrap_server,topicname):
        self.bootstrap_servers = bootstrap_server
        self.topicName = topicname
        self.consumer = KafkaConsumer(bootstrap_servers=self.bootstrap_servers)

    def run(self):
        a = self.consumer.partitions_for_topic(self.topicName)
        lst = []
        for i in a:
            lst.append(i)
        process_list =[]
        for i in lst:
            self.pattition = i
            self.topic = TopicPartition(self.topicName, i)
            self.consumer.assign([self.topic])
           # t1 = threading.Thread(target= self.consumers)
            t1 = Process(target= self.consumers,args=(i+1,))
            process_list.append(t1)
            t1.start()
        for i in process_list:
            i.join()


    def consumers(self, process):
        self.process = process
        max_offset = Data.search_max_offset(process-1)[-1]['offset']
        bulk = 1
        a = []
        logging.basicConfig(level=logging.INFO)
        self.consumer.seek(self.topic, offset=max_offset + 1)
        while True:
            poll = self.consumer.poll(timeout_ms=5000, max_records=1)
            for i , msgs in poll.items():
                a.append(msgs)
                offset = msgs[-1].offset
                partition = msgs[-1].partition
                logging.info('bulk={},offset={},partition={},process={}'.format(bulk,offset,partition,process))
                bulk += 1

            if bulk >10 :
                bulk = 1
                logging.info(a[-1][-1].offset)
                final_offset = a[-1][-1].offset
                final_timestamp = a[-1][-1].timestamp
                from datetime import datetime
                time = datetime.now()
                test = {'final_offset': final_offset, 'final_timestamp': final_timestamp, "time": time}
                Checkpoint.insert(test).execute()
                for i in range(0,len(a)):
                    offset = a[i][-1].offset
                    topic = a[i][-1].topic
                    partition = a[i][-1].partition
                    timestamp = a[i][-1].timestamp
                    timestamp_type = a[i][-1].timestamp_type
                    test = {'offset': offset, 'timestamp': timestamp, 'partition': partition, 'timestamp_type': timestamp_type,'topic': topic}
                    Data.insert(test).execute()
                import time
                time.sleep(3)


if __name__ == '__main__':
    x = GetConsumer('localhost:9092','newtopic')
    x.run()

"""
    def consumer1(self):
        bulk = 1
        a = []
        max_offset1 = Data.search_max_offset1()
        logging.basicConfig(level=logging.INFO)
        while True:
            poll = self.consumer2.poll(timeout_ms=5000, max_records=10)
            for i, msgs in poll.items():
                a.append(msgs)
                logging.info('bulk')
                logging.info(bulk)
                logging.info('offset')
                logging.info(msgs[-1].offset)
                bulk += 1
                logging.info('partition')
                logging.info(msgs[-1].partition)

            if bulk > 10 :
                bulk = 1
                logging.info(a[-1][-1].offset)
                final_offset = a[-1][-1].offset
                final_timestamp = a[-1][-1].timestamp
                from datetime import datetime
                time = datetime.now()
                test = {'final_offset': final_offset, 'final_timestamp': final_timestamp, "time": time}
                Checkpoint.insert(test).execute()
                for i in range(0, len(a)):
                    offset = a[i][-1].offset
                    topic = a[i][-1].topic
                    partition = a[i][-1].partition
                    timestamp = a[i][-1].timestamp
                    timestamp_type = a[i][-1].timestamp_type
                    test = {'offset': offset, 'timestamp': timestamp, 'partition': partition,'timestamp_type': timestamp_type, 'topic': topic}
                    Data.insert(test).execute()
                import time
                time.sleep(3)
"""



#while True :
 #   t1 = threading.Thread(target=consumer0)
    #t2 = threading.Thread(target=consumer1)
  #  t1.start()
    #t2.start()
   # t1.join()
    #t2.join()


"""
##   print(len(x))
while True:
    msg_poll = consumer.poll(timeout_ms=300000, max_records=10)
    #for i,x in six.iteritems(msg_poll):
    for i, x in msg_poll.items():
        h = 0
        while h <10:
            e = h
            offset = x[e].offset
            topic = x[e].topic
            partition = x[e].partition
            timestamp = x[e].timestamp
            timestamp_type = x[e].timestamp_type
            test = {'offset': offset, 'timestamp': timestamp, 'partition': partition, 'timestamp_type': timestamp_type,
                    'topic': topic}
            final_offset = x[e].offset
            final_timestamp = x[e].timestamp
            time = datetime.now()
            test1 = {'final_offset': final_offset, 'final_timestamp': final_timestamp, "time": time}
            print(x[e].offset)
            if len(x[e].value) < 10:
                x[e].offset = x[e+1].offset
                e = e + 1
            Data.insert(test).execute()
            h = h +1
            e = e + 1
            if h == 10:
                break

        Checkpoint.insert(test1).execute()
        print(test)
        import time
        time.sleep(5)

        h = 0
        a=[]
        #while h>=0:
        print(x[h].offset)
        print(len(x[h].value)
        print(h)
        a.append(x[h].offset)
        time.sleep(3)
        print(a)
    #print('ok')
    #time.sleep(3)

       #if len(x) == 10:
        #    final_offset = x[-1].offset
         #   final_timestamp = x[-1].timestamp
          #  time = datetime.now()
           # test = {'final_offset': final_offset, 'final_timestamp': final_timestamp, "time": time}
            #test1 = Checkpoint.get_or_none(final_offset=final_offset)
            #if test1 is None:
             #   Checkpoint.insert(test).execute()
            #print(x)
       # import time
        #time.sleep(3)



    for i,x in six.iteritems(msg_poll):
        if len(x) == 10:
            final_offset = x[-1].offset
            final_timestamp = x[-1].timestamp
            time = datetime.now()
            test = {'final_offset': final_offset, 'final_timestamp': final_timestamp, "time": time}
            test1 = Checkpoint.get_or_none(final_offset=final_offset)
            if test1 is None:
                Checkpoint.insert(test).execute()
            print(len(x))
        if len(x) ==10:
            for i in range(0, 9):
                if len(x[i].value >= 10):
                    offset = x[i].offset
                    topic = x[i].topic
                    partition = x[i].partition
                    timestamp = x[i].timestamp
                    timestamp_type = x[i].timestamp_type
                    test = {'offset': offset, 'timestamp': timestamp, 'partition': partition,'timestamp_type': timestamp_type, 'topic': topic}
                    Data.insert(test).execute()
        import time

        time.sleep(3)







#max_offset = Data.search_max()[0]['offset']



"""


