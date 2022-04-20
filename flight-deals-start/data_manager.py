import requests


class DataManager:
    SHEETY_ENDPOINT = "ENDPOINT"
    SHEETY_USERS = "ENDPOINT"

    def __init__(self):
        self.__sheet_data = {}
        self.__sheet_emails = {}
        self.__user_data = {}
        self.get_sheet_data()
        self.get_user_emails()

    def get_sheet_data(self):
        """
        This will use the sheety api to return to
        :return: sheet data dictionary
        """
        response = requests.get(url=self.SHEETY_ENDPOINT)
        response.raise_for_status()
        self.__sheet_data = response.json()

    def update_row(self, row_id, row_data):
        response = requests.put(url=f"{self.SHEETY_ENDPOINT}/{row_id}", json=row_data)

    def get_user_emails(self):
        response = requests.get(self.SHEETY_USERS)
        data = response.json()
        self.__user_data = data["users"]

    @property
    def user_data(self):
        return self.__user_data

    @user_data.setter
    def user_data(self, value):
        self.__user_data = value

    @property
    def sheet_data(self):
        return self.__sheet_data

    @sheet_data.setter
    def sheet_data(self, value):
        self.__sheet_data = value

    @sheet_data.deleter
    def sheet_data(self):
        del self.__sheet_data
