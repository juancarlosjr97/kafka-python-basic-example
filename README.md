# Kafka Basic Example Python

These are the instructions to run Kafka on a macOS.

## Prerequisites

We need to have installed the following services:

- [Homebrew](https://brew.sh/)
- [Python 3 or above](https://www.python.org/)

### Installation

1. Install Java 8 SDK using homebrew

```
brew cask install homebrew/cask-versions/adoptopenjdk8
```

2. Install Kafka using homebre

```
brew install kafka
```

3. Python Environment

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Start Zookeeper and Kafka as a service

```
brew services start zookeeper
brew services start kafka
```

## Stop Zookeeper and Kafka as a service

```
brew services stop zookeeper
brew services stop kafka
```

## Creating a topic on Kafka

```
kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic ${TOPIC_NAME}
```

## Start Consumer

The virtual environment needs to be activated.

```
python consumer.py --topic=TOPIC
```

## Send a message a Producer

The virtual environment needs to be activated.

```
python producer.py --topic=TOPIC --message=MESSAGE --server=SERVER
```
