import json
import time
import urllib.parse

import requests
import validators
from PySide6.QtCore import QThread, Signal


def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError as e:
        return False
    return True


auth_dir = "/cgi-bin/dologin/"
request_value_dir = "/cgi-bin/api.values.post/"
api_sys_operation = "/cgi-bin/api-sys_operation/"
api_get_phone_status = "/cgi-bin/api-get_phone_status/"
api_change_default_password = "/cgi-bin/api-change_default_password/"

URL_SERVER = "http://188.235.18.191:8071/api/history/add/"


def send_message_to_server(reset_phone: bool, fast_setting: bool, sip_user: str, ip_phone: str):
    try:
        requests.post(URL_SERVER, json={"reset_phone": reset_phone,
                                        "sip_user": sip_user,
                                        "fast_setting": fast_setting,
                                        "ip_phone": ip_phone}, timeout=3)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print(e)





if __name__ == '__main__':
    send_message_to_server(True, True, "123", "123")


class PhoneGXP1620SettingThread(QThread):
    status_operation = Signal(str)
    status_operation_error = Signal(str)
    setting_end = Signal(str)
    button_enable = Signal(bool)

    def __init__(self, parent=None):
        super(PhoneGXP1620SettingThread, self).__init__(parent)
        self.url_phone = None
        self.login_web = None
        self.password_web = None
        self.SIP_USER_ID = None
        self.SIP_USER_PASSWORD = None
        self.reset_phone_bool: bool = False
        self.fast_setting: bool = False

    def get_status_phone(self):
        timing = time.time()
        status_phone_api = urllib.parse.urljoin(self.url_phone, api_get_phone_status)
        count = 1
        count_success = 0
        while True:
            time.sleep(5)
            self.status_operation.emit(f'Пробую подключиться к телефону... Попытка: {count}')
            print(f'Пробую подключиться к телефону... Попытка: {count}')
            count += 1
            try:
                r = requests.post(status_phone_api, data=post_get_status_phone, timeout=5)
                print(r.text)
                if r.json()['response'] == "success":
                    count_success += 1
                    if count_success >= 2:
                        self.status_operation.emit(
                            f'Телефон перезагружен. время в секундах: {round((time.time() - timing), 2)}')
                        print(f'Телефон перезагружен time: {time.time() - timing}')
                        break
            except requests.exceptions.ConnectTimeout as error:
                print(error)
                pass

            except requests.exceptions.ReadTimeout as read_err:
                print(read_err)
                pass
            except requests.exceptions.ConnectionError as conn_err:
                print(conn_err)
                pass

    def reset_phone(self):
        reset_phone_url = urllib.parse.urljoin(self.url_phone, api_sys_operation)
        r = requests.post(reset_phone_url, data=post_reset_phone)
        print('Сбрасываю телефон к заводским настройкам')
        self.status_operation.emit('Сбрасываю телефон к заводским настройкам')
        self.get_status_phone()

    def set_url_phone(self, url_phone):
        self.url_phone = url_phone

    def set_fast_setting(self, fast_setting: bool):
        self.fast_setting = fast_setting

    def set_reset_phone(self, reset: bool):
        self.reset_phone_bool = reset

    def set_login_web(self, login_web):
        self.login_web = login_web

    def set_password_web(self, password_web):
        self.password_web = password_web

    def set_sip_user_id(self, sip_user_id):
        self.SIP_USER_ID = sip_user_id

    def set_sip_user_password(self, sip_user_password):
        self.SIP_USER_PASSWORD = sip_user_password

    def authorization(self):

        url = urllib.parse.urljoin(self.url_phone, auth_dir)
        if not validators.url(url):
            self.status_operation_error.emit(f'url phone is not valid {url}')
            return -1
        self.status_operation.emit(url)
        requ = None

        try:
            # r = requests.post(url, data={'username': self.login_web, 'password': self.password_web}, timeout=5)
            #
            # if r.status_code == 403:
            r = requests.post(url, data={'username': self.login_web, 'password': self.password_web}, timeout=10,
                              headers={'Referer': self.url_phone})

            print(r.json())

            if 'body' in r.json():
                print('body is true')
                if 'defaultAuth' in r.json()['body']:
                    print('defaultAuth is true')
                    if r.json()['body']['defaultAuth']:
                        url_edit_pass = urllib.parse.urljoin(self.url_phone, api_change_default_password)
                        post_account_edit_pass_adm['curAdmPwd'] = self.password_web
                        post_account_edit_pass_adm['newAdmPwd'] = '963258'
                        post_account_edit_pass_adm['Referer'] = self.url_phone
                        sid = r.json()["body"]['sid']
                        post_account_edit_pass_adm['sid'] = sid
                        headers = {
                            "Cookie": f'session-identity={str(sid)}; session-role=admin'
                        }
                        print(url_edit_pass)
                        print(post_account_edit_pass_adm)
                        edit_pass_adm_request = requests.post(url_edit_pass, data=post_account_edit_pass_adm, timeout=5,
                                                              headers=headers)
                        print(edit_pass_adm_request.text)
                        if edit_pass_adm_request.json()['response'] == 'success':
                            self.status_operation_error.emit(
                                f"Установлен новый пароль: {post_account_edit_pass_adm['newAdmPwd']}")
                        print('----------------------')

            print(r.text)
            requ = r

        except requests.exceptions.ConnectTimeout as error:
            self.status_operation_error.emit(f'ConnectTimeout {self.url_phone}')

        except requests.exceptions.ConnectionError as err:
            self.status_operation_error.emit(f'ConnectionError {self.url_phone}')

        except requests.exceptions.ReadTimeout as err:
            self.status_operation_error.emit(f'ReadTimeout {self.url_phone}')

        if requ is not None:
            if requ.status_code == 200:
                print(requ.json())
                if 'response' in requ.json():
                    if requ.json()['response'] == 'error':
                        print('Ошибка авторизации')
                        if 'body' in requ.json():
                            if requ.json()['body'] == 'locked':
                                self.status_operation_error.emit(
                                    'Слишком много не удачных попыток для входа... подождите')
                        self.status_operation_error.emit('Ошибка авторизации')
                        return -1
                print('Успешная авторизация')
                self.status_operation.emit('Успешная авторизация')
                sid = requ.json()["body"]['sid']
                self.status_operation.emit(f'sid: {sid} ID USER: {self.SIP_USER_ID}')
                return sid

        return -1

    def run(self):
        self.button_enable.emit(False)
        timing = time.time()
        sid = self.authorization()
        set_sid_to_all_dict(sid)
        print(self.reset_phone_bool)

        if self.reset_phone_bool is True:
            self.reset_phone()
            self.password_web = 'admin'
            sid = self.authorization()
            if sid == -1:
                return sid
            set_sid_to_all_dict(sid)

        if self.fast_setting and sid != -1:
            set_gen_setting(self.SIP_USER_ID, self.SIP_USER_PASSWORD)
            request_post = urllib.parse.urljoin(self.url_phone, request_value_dir)
            headers = {
                "Cookie": f'session-identity={str(sid)}; session-role=admin'
            }
            dict_all = {**post_network_setting,
                        **post_account__basic_setting,
                        **post_account__security_setting,
                        **post_account__audio_setting,
                        **post_account__call_setting,
                        **post_setting_gen_setting,
                        **post_setting_call_features,
                        **post_setting_date_time,
                        **post_display_lang,
                        **post_account_gen_setting}
            print(dict_all)
            fast_post = requests.post(request_post, data=dict_all, headers=headers)
            self.status_operation.emit(
                f'Быстрая настройка аккаунта /// time: {(time.time() - timing):.2f} {get_status_JSON(fast_post.json())}')
            self.setting_end.emit(f'Настройка телефона: {self.url_phone} ID USER: {self.SIP_USER_ID} завершена')
            self.setting_end.emit('===========================')

        if sid != -1 and not self.fast_setting:
            set_gen_setting(self.SIP_USER_ID, self.SIP_USER_PASSWORD)
            request_post = urllib.parse.urljoin(self.url_phone, request_value_dir)
            headers = {
                "Cookie": f'session-identity={str(sid)}; session-role=admin'
            }

            # r_post_account__basic_setting = requests.post(request_post, data=post_account__basic_setting,
            #                                               headers=headers)

            # self.get_status_phone()
            # sid = self.authorization()
            # set_sid_to_all_dict(sid)

            print(request_post)
            r_network_setting = requests.post(request_post, data=post_network_setting, headers=headers)

            print(r_network_setting.text)
            self.status_operation.emit(
                f'network_setting /// time: {(time.time() - timing):.2f} {get_status_JSON(r_network_setting.json())}')

            r_post_account__basic_setting = requests.post(request_post, data=post_account__basic_setting,
                                                          headers=headers)
            self.status_operation.emit(
                f'account basic setting /// time: {(time.time() - timing):.2f} {get_status_JSON(r_post_account__basic_setting.json())}')

            r_post_account__security_setting = requests.post(request_post, data=post_account__security_setting,
                                                             headers=headers)
            self.status_operation.emit(
                f'security setting /// time: {(time.time() - timing):.2f} {get_status_JSON(r_post_account__security_setting.json())}')

            r_post_account__audio_setting = requests.post(request_post, data=post_account__audio_setting,
                                                          headers=headers)
            self.status_operation.emit(
                f'audio setting /// time: {(time.time() - timing):.2f} {get_status_JSON(r_post_account__audio_setting.json())}')

            r_post_account__call_setting = requests.post(request_post, data=post_account__call_setting, headers=headers)
            self.status_operation.emit(
                f'account call setting time: {(time.time() - timing):.2f} {get_status_JSON(r_post_account__call_setting.json())}')

            r_post_setting_gen_setting = requests.post(request_post, data=post_setting_gen_setting, headers=headers)
            self.status_operation.emit(
                f'setting gen setting /// time: {(time.time() - timing):.2f} {get_status_JSON(r_post_setting_gen_setting.json())}')

            r_post_setting_call_features = requests.post(request_post, data=post_setting_call_features, headers=headers)
            self.status_operation.emit(
                f'call features /// time: {(time.time() - timing):.2f} {get_status_JSON(r_post_setting_call_features.json())}')

            r_post_setting_date_time = requests.post(request_post, data=post_setting_date_time, headers=headers)
            self.status_operation.emit(
                f'datetime /// time: {(time.time() - timing):.2f} {get_status_JSON(r_post_setting_date_time.json())}')

            r_post_display_lang = requests.post(request_post, data=post_display_lang, headers=headers)
            self.status_operation.emit(
                f'display lang /// time: {(time.time() - timing):.2f} {get_status_JSON(r_post_display_lang.json())}')

            r_post_account_gen_setting = requests.post(request_post, data=post_account_gen_setting, headers=headers)
            self.status_operation.emit(
                f'account gen setting /// time: {(time.time() - timing):.2f} {get_status_JSON(r_post_account_gen_setting.json())}')

            self.setting_end.emit(f'Настройка телефона: {self.url_phone} ID USER: {self.SIP_USER_ID} завершена')
            self.setting_end.emit('===========================')

        send_message_to_server(reset_phone=self.reset_phone_bool, fast_setting=self.fast_setting,
                               sip_user=self.SIP_USER_ID, ip_phone=self.url_phone)

        self.button_enable.emit(True)


post_account_gen_setting = {
    'P271': 1,  # Account Active
    'P270': '',  # Account Name
    'P35': '',  # SIP User ID
    'P36': '',  # Authenticate ID
    'P3': '',  # Name
    'P34': '',  # Authenticate Password
    'P47': 'cloudpbx.finist.com',  # SIP Server
    'P48': '79.143.26.155',  # Outbound Proxy
    'sid': '',  # Уникальный ключ
}

post_account__basic_setting = {
    'P63': 1,  # TEL URI
    'P32': 600,  # Register Expiration
    'P2305': 2,  # Register Expiration
    'sid': '',  # Уникальный ключ
}

post_account_edit_pass_adm = {
    'curAdmPwd': 'old_pass',  # TEL URI
    'newAdmPwd': 'new_pass',  # Register Expiration
    'Referer': '',
    'sid': '',  # Уникальный ключ
}

post_account__security_setting = {
    'P2311': 0,  # Check Domain Certificates
    'P2367': 0,  # Validate Certification Chain
    'P2306': 0,  # Validate Incoming Messages
    'P258': 0,  # Check SIP User ID for Incoming INVITE
    'P2347': 1,  # Accept Incoming SIP from Proxy Only
    'P2346': 0,  # Authenticate Incoming INVITE
    'sid': '',  # Уникальный ключ
}

post_account__audio_setting = {
    'P57': 8,  # Preferred Vocoder - choice 1
    'P58': 18,  # Preferred Vocoder - choice 2
    'sid': '',  # Уникальный ключ
}

post_account__call_setting = {
    'P129': 1,  # Anonymous Call Rejection
    'sid': '',  # Уникальный ключ
}

post_setting_gen_setting = {
    'P39': 16384,  # Local RTP Port
    'P78': 1,  # Use Random Port
    'sid': '',  # Уникальный ключ
}

post_setting_call_features = {
    'P1310': 1,  # Disable Direct IP Call
    'sid': '',  # Уникальный ключ
}

post_setting_date_time = {
    'P30': '192.168.81.8',  # NTP Server
    'P64': 'MSK-3',  # Time Zone
    'P102': 2,  # Date Display Format
    'P122': 1,  # Time Display Format
    'sid': '',  # Уникальный ключ
}

post_display_lang = {
    'P1362': 'ru',  # NTP Server
    'sid': '',  # Уникальный ключ
}

post_network_setting = {
    'P52': 2,  # NTP Server
    'sid': '',  # Уникальный ключ
}

post_reset_phone = {
    'request': 'RESET',  # СБРОС ТЕЛЕФОНА
    'sid': '',  # Уникальный ключ
}

post_get_status_phone = {
    'request': 'WEB',  # ТИП ПОДКЛЮЧЕНИЯ
}


def set_sid_to_all_dict(sid: str):
    post_account_gen_setting['sid'] = sid
    post_account__basic_setting['sid'] = sid
    post_account__security_setting['sid'] = sid
    post_account__audio_setting['sid'] = sid
    post_account__call_setting['sid'] = sid
    post_setting_gen_setting['sid'] = sid
    post_setting_call_features['sid'] = sid
    post_setting_date_time['sid'] = sid
    post_display_lang['sid'] = sid
    post_reset_phone['sid'] = sid
    post_network_setting['sid'] = sid


def set_gen_setting(SIP_ID, SIP_PASS):
    post_account_gen_setting['P270'] = SIP_ID
    post_account_gen_setting['P35'] = SIP_ID
    post_account_gen_setting['P36'] = SIP_ID
    post_account_gen_setting['P3'] = SIP_ID
    post_account_gen_setting['P34'] = SIP_PASS


def get_status_JSON(json):
    print(json)
    if json["response"] == "success":
        return "STATUS: OK"
    return "STATUS: ERROR"
