#!/usr/bin/env python
import time
import requests
import sys


class HttpPing:

    def __init__(self, url):
        self.url = url
        self.status = []
        self.time = []
        self.count = 0

    def ping(self):
        try:
            before = time.time()
            status_code = requests.get(self.url).status_code
            after = time.time()
            time_diff = (after - before) * 1000
            self.count += 1
            self.status.append(status_code)
            self.time.append(time_diff)
            return f'Count: {self.count} Status code: {status_code} time: {time_diff:.2f}ms'
        except requests.exceptions.RequestException as e:
            return f'Error: {e}'

    def get_min_time(self):
        return min(self.time)

    def get_max_time(self):
        return max(self.time)

    def get_avg_time(self):
        return (sum(self.time)/len(self.time))

    def get_success_rate(self):
        return (self.status.count(200)/len(self.status)*100)

    def get_requests_count(self):
        return self.count


def main():
    url = f'https://{sys.argv[1]}'
    h = HttpPing(url)
    try:
        while True:
            print(h.ping())
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass
    finally:
        print(
            f'\rMin: {h.get_min_time():.2f}ms | max: {h.get_max_time():.2f}ms | avg: {h.get_avg_time():.2f}ms')
        print(
            f'Total requests: {h.count} success rate: {h.get_success_rate():.2f}%')


if __name__ == "__main__":
    main()
