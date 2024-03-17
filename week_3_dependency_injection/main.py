from abc import ABC, abstractmethod

class WeatherService:
    def __init__(self):
        pass


class API_Factory(ABC):
    @abstractmethod
    def fetch_data(self, url):
        """Will return an object that is an API"""

class WeatherAPI(API_Factory):
    def fetch_data(self, url):



def main():
    pass

if __name__ == "__main__":
    main()


