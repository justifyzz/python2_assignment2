import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://etherscan.io/accounts'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_ddlRecordsPerPage"]/option[4]').click();
page = driver.page_source
page_soup = soup(page, 'html.parser')

accounts = []
balances = []

address = []
for row in range(1, 101):
    address = driver.find_element(By.XPATH,
                                  '//*[@id="ContentPlaceHolder1_divTable"]/table/tbody/tr[' + str(row) + ']/td[2]')
    balance = driver.find_element(By.XPATH,
                                  '//*[@id="ContentPlaceHolder1_divTable"]/table/tbody/tr[' + str(row) + ']/td[4]')
    accounts.append(address.text)
    x = balance.text.replace("Ether", "")
    balances.append(float(x.replace(',', '')))


# Create your views here.
def home(request):
    return render(request, 'accounts/home.html', {})


def charts(request):
    return render(request, 'accounts/charts.html')


def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        data = {
            "labels": accounts,
            "default": balances
        }
        return Response(data)
