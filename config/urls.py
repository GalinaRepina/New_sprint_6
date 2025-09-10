class AppConfig:
    BASE_DOMAIN = 'qa-scooter.praktikum-services.ru'
    PROTOCOL = 'https'
    DZEN_URL = 'https://dzen.ru/?yredirect=true'
    
    @property
    def base_url(self):
        return f'{self.PROTOCOL}://{self.BASE_DOMAIN}'
    
    @property
    def main_page(self):
        return f'{self.base_url}/'
    
    @property
    def order_page(self):
        return f'{self.base_url}/order'
    
    @property
    def order_status_page(self):
        return f'{self.base_url}/track'

# Создаем экземпляр конфигурации
app_config = AppConfig()