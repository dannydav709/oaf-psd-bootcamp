from abc import ABC, abstractmethod
import requests

class AbstractDataService(ABC):
    @abstractmethod
    def fetch_data(self):
        pass

class APICallingService(AbstractDataService):
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        response = requests.get(self.url)
        if response.ok:
            return response.json()
        else:
            return None

class DataServiceFactory:
    def create_data_service(self, url) -> AbstractDataService:
        return APICallingService(url)

class DataSourceHandler:
    def __init__(self, data_service: AbstractDataService):
        self.data_service = data_service

    def handle_data(self):
        data = self.data_service.fetch_data()
        if data is not None:
            # print(data)  # Or any other processing
            return data
        else:
            print("Failed to fetch data.")

def main():
    factory = DataServiceFactory()
    data_service = factory.create_data_service("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41"
                                               "&hourly=temperature_2m")
    data_handler = DataSourceHandler(data_service)
    print(data_handler.handle_data())

if __name__ == "__main__":
    main()
