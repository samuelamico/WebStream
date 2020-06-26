# WebStream

The project aims to simulate in a cluster of VMs (3 VMs) the process of streaming accesses to a web page with two events being produced: one of them informs the website and the system that the user log in and the other case the information of ( only for user that register on the site).


- [x] Strat a little explanation
- [X] Describe the Kafka SetUp
- [ ] Describe the Producer 
- [ ] Describe the Consumer
- [ ] Describe the Streaming Data Storage 
- [ ] More to come ...

## Install Zookeeper:
![alt text](https://zookeeper.apache.org/images/zookeeper_small.gif "ZooKeeper")


Apache Kafka uses Zookeeper to store metadata about the Kafka cluster, as well as
consumer client details. To install zookeeper the pre-requisit is the Java installed:

```bash
sudo apt install openjdk-8-jdk
java -version
```

To installs Zookeeper Sigle-Node server with a basic configuration in /usr/local/zookeeper, storing its data in /var/lib/zookeeper:

{VERSION} = zookeeper-3.4.14
{FILE} = zookeeper-3.4.14.tar.gz

```bash
sudo wget http://mirror.cc.columbia.edu/pub/software/apache/zookeeper/{VERSION}/{FILE}
#
tar -zxf {FILE}
mv zookeeper-3.4.6 /usr/local/zookeeper
mkdir -p /var/lib/zookeeper
cp  /usr/local/zookeeper/conf/zoo_sample.cfg  /usr/local/zookeeper/conf/zoo.cfg 
export JAVA_HOME={/usr/path/JAVA_VERSION}
```

To start zookeep: /usr/local/zookeeper/bin/zkServer.sh start
Or you can use my ./start_server.sh file.

## Install Kafka:
With Zookeeper, now you can install Apache Kafka. The
current release of Kafka can be downloaded at http://kafka.apache.org/down
loads.html.

```bash
tar -zxf kafka_2.{VERSION}.tgz
mv kafka_2.{VERSION} /usr/local/kafka
mkdir /tmp/kafka-logs
/usr/local/kafka/bin/kafka-server-start.sh -daemon
/usr/local/kafka/config/server.properties
```

To start Kafka you can use my ./start_topics.sh file

## Cluster single-node:

 https://boristyukin.com/connecting-to-kafka-on-virtualbox-from-windows/