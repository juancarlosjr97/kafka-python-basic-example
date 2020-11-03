import argparse
from kafka import KafkaConsumer


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="consumer.py",
        description="Consumer code for Apache Kafka",
        usage="%(prog)s [options]",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument("--topic", help="Topic")

    args = parser.parse_args()

    consumer = KafkaConsumer(args.topic)
    for msg in consumer:
        print(msg)
