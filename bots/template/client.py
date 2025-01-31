from bots.base.base import BaseFarmer
from bots.base.utils import to_localtz_timestamp
from bots.iceberg.strings import HEADERS


class BotFarmer(BaseFarmer):
    name = "bot_username"
    extra_code = "ref_code"  # в случае если рефка вида https://t.me/bot_username?start=ref_code
    app_extra = "ref_code"  # в случае если рефка вида https://t.me/bot_username?action?param=ref_code (Тут пока не разобрался увы)
    initialization_data = {} # данные для передачи в инициатор, отличаются в зависимости от типа кнопки входа в бота

    def set_headers(self, *args, **kwargs):
        """ Установка заголовков """
        self.headers = HEADERS.copy()

    def authenticate(self, *args, **kwargs):
        """ Аутентифифкация, получения токена, выставление заголовков, заполнение шаблона запроса и тд... """
        raise NotImplementedError

    def set_start_time(self):
        """ 
        Метод выставляет время следующего захода фармера. 
        Например время когда закончится фарминг или накопятся тапы 
        """
        raise NotImplementedError

    def farm(self):
        """
        Основной метод, описывающий логику модуля. 
        Покупки, прокачки. Все здесь 
        """
        raise NotImplementedError
