from abc import ABC, abstractmethod
import requests
from dataclasses import dataclass

# @dataclass
class API_Factory():
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        response = requests.get(self.url)
        if 200 <= response.status_code <= 299:
            data = response.json()
        else:
            data = None
        return data


class Weather_API(API_Factory):
    # def __init__(self, url):
    #     self.url = url
    def __init__(self, url="https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m"):
        super().__init__(url)


def main():
    open_meteo = Weather_API()
    print(open_meteo.fetch_data())


if __name__ == "__main__":
    main()


