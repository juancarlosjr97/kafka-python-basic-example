import argparse
from kafka import KafkaProducer

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="producer.py",
        description="Producer code for Apache Kafka",
        usage="%(prog)s [options]",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument("--topic", help="Topic")
    parser.add_argument("--message", help="Message")
    parser.add_argument("--server", help="Server")

    args = parser.parse_args()

    producer = KafkaProducer(bootstrap_servers=args.server)
    producer.send(args.topic, args.message.encode('ascii'))

    producer.flush()
