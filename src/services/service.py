import asyncio
import logging

from bs4 import BeautifulSoup
from aiohttp import ClientSession
from src.config import nice_headers
import re


async def get_async_client():
    async with ClientSession() as session:
        yield session


class Service:

    def __init__(self):
        self.phone_pattern = r'(?:"\+7|\b8)?\s*[\(]?\d{3}[\)]?\s*\d{3}[-]?\d{2}[-]?\d{2}\b'

    async def _extract_number(self, url: str):

        # Получаем HTML-код страницы
        async with ClientSession() as client:
            async with client.get(url, headers=nice_headers) as response:
                html = await response.text()

        file_name = url.replace('/', '', ).replace("https:", "").split('.')[0]
        # Записываем HTML-код в файл
        with open(f'src/backend/sites/{file_name}.html', 'w+') as file:
            file.write(html)

        # Извлекаем текст из HTML-кода
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text()

        # Находим номера телефонов в тексте
        numbers = set(re.findall(self.phone_pattern, html))

        # Очищаем номера от лишних символов
        cleaned_numbers = []
        for number in numbers:
            cleaned_number = ''.join(filter(str.isdigit, number))
            if len(cleaned_number) >= 10 and cleaned_number[0] in ['7', '8', '"', "'", '+', '4']:
                cleaned_numbers.append(cleaned_number)

        # Приводим номера к единому формату
        url_numbers = {
            'site': url
        }
        normalized_numbers = []
        for number in cleaned_numbers:
            if number.startswith('7'):
                normalized_numbers.append(number.replace('7', '8', 1))
            elif number.startswith('4'):
                normalized_numbers.append(number.replace('4', '84', 1))
            else:
                normalized_numbers.append(number)
        url_numbers['numbers'] = normalized_numbers
        return url_numbers

    async def extract_numbers(self, urls_list):
        tasks = [self._extract_number(url) for url in urls_list]
        result = await asyncio.gather(*tasks)
        return result