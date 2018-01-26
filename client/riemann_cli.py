import random

import bernhard


def get_service_name():
    service_list = [
        'cpu',
        'memory',
        'disk usage',
        'swap']

    return random.choice(service_list)


def get_event_value():
    value_list = [
        10,
        50,
        75,
        80,
        85,
        90,
        95]

    return random.choice(value_list)


def get_hostname():
    hostname_list = [
        'web001',
        'web002',
        'db001',
        'db002']

    return random.choice(hostname_list)


def main():
    client = bernhard.Client(host='127.0.0.1',
                             port=5555)
    event_service = get_service_name()
    event_value = get_event_value()
    event_hostname = get_hostname()

    print('host: {}, service: {}, metric: {}'.format(
        event_hostname,
        event_service,
        str(event_value)))

    client.send({'host': event_hostname,
                 'service': event_service,
                 'description': 'blah',
                 'state': 'ok',
                 'ttl': 25,
                 'metric': str(event_value)})


if __name__ == '__main__':
    main()
