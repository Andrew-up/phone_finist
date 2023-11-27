import ipaddress
import re
import sys
import time
import urllib.parse
from datetime import datetime

import pandas as pd
import requests
from PySide6.QtCore import QThread, Signal, Slot
from PySide6.QtWidgets import QApplication, QWidget, QCheckBox, QFileDialog, QMessageBox
from scapy.config import conf
from scapy.layers.inet import IP, TCP, ICMP
from scapy.sendrecv import sr1, srp1, srp

from ui.py.search_phones import Ui_Form

# from scapy import all


URL_SERVER = "http://188.235.18.191:8071/api/logging/add/"


def send_message_logging_to_server(action: str, info: str):
    try:
        requests.post(URL_SERVER, json={"action": action,
                                        "info": info}, timeout=3)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print(e)


city_info = {
    "name": "",
    "ip": ""
}
vrn = {"name": "vrn", "ip": ["192.168.36.0/24"]}
msk = {"name": "msk", "ip": ["192.168.99.0/24"]}
spb = {"name": "spb", "ip": ["192.168.120.0/24"]}
nn = {"name": "nn", "ip": ["192.168.152.0/24"]}
krd = {"name": "krd", "ip": ["192.168.22.0/23"]}
nvs = {"name": "novosibirsk", "ip": ["192.168.52.0/24"]}
stv = {"name": "stavropol", "ip": ["192.168.24.0/24"]}
tmb = {"name": "tambov", "ip": ["192.168.47.0/24"]}
rzn = {"name": "rzn", "ip": ["192.168.80.0/22", "192.168.94.0/24"]}
# rzn = {"name": "rzn", "ip": ["192.168.81.0", "192.168.82.0", "192.168.83.0", "192.168.94.0"]}
auth_dir = "/cgi-bin/dologin/"
# params_info = "Pphone_model:vendor_fullname:P35:P36:P3:P270:PAccountRegistered1:P404:P402:PAccountRegistered2"
params_info = "P35:Pphone_model:PAccountRegistered1:P67"
get_system_info_api = "/cgi-bin/api.values.get"


class PhoneSearchThread(QThread):
    total_hosts = Signal(int)
    current_host = Signal(int)
    current_city = Signal(str)
    error_message = Signal(str)
    append_to_log = Signal(str)
    enable_button = Signal(bool)
    search_count_phones = Signal(int)

    def __init__(self, parent=None):
        super(PhoneSearchThread, self).__init__(parent)
        self.list_ip = []
        self.phones_valid_list = []
        self.output_excel_path = ''
        self.pause = False
        self.temp_data = None

    def set_list_ip(self, list_ip):
        self.list_ip = list_ip

    def set_path(self, path):
        self.output_excel_path = path

    def AuthPhone(self, url, password='admin'):
        r = None
        sid = None
        r_status_code = 0
        phone_info = {
            "model": None,
            'SIP': None,
            "SIP_account_work": None,
            "ip": None,
            "mac": None,
            "info": None
        }
        ip = url.lstrip('http://')
        ip = ip.rstrip('/cgi-bin/dologin/')
        phone_info['ip'] = ip
        try:
            r = requests.post(url, data={'username': 'admin', 'password': password}, timeout=10,
                              headers={'Referer': url})
            r_status_code = r.status_code
            # print(r.headers.get('Content-Type'), url)
            server_headers = r.headers.get('Server')

            if server_headers:
                # print(server_headers)
                if re.match(r'^.*Grandstream.*$', server_headers):
                    phone_name = re.search(r'GXP.*\s', server_headers).group(0)
                    if phone_name:
                        phone_info['model'] = re.search(r'GXP.*\s', server_headers).group(0)



        except requests.exceptions.RequestException as e:  # This is the correct syntax
            pass
            # print(e)

        if r_status_code == 200 and re.match(r'^application/json.*$', r.headers.get('Content-Type')):
            if 'response' in r.json():
                if r.json()['response'] != 'error':
                    sid = r.json()["body"]['sid']
                elif password != '963258':
                    sid = self.AuthPhone(url, '963258')
                else:
                    phone_info['info'] = 'password not admin and not 963258'

        if not sid:
            if phone_info['model']:
                self.phones_valid_list.append(phone_info)
                return phone_info
        return sid

    def data_to_excel(self, data, path, row, sheet_name):
        new_df = pd.DataFrame(data, index=[0])
        try:
            with pd.ExcelWriter(path, engine="openpyxl", mode='a',
                                if_sheet_exists='overlay') as writer:
                new_df.to_excel(writer, sheet_name=sheet_name, index=False, startrow=row,
                                header=False)
                print('append data: ' + str(data))
                self.append_to_log.emit(f'Добавлено: {data["ip"]} - {data["SIP"]}')
            # self.pause = False
        except PermissionError as e:
            # print(e.errno)
            print(e.filename)
            # print(e.filename2)
            self.error_message.emit('закройте файл:\n' + e.filename)
            print('закройте файл:' + e.filename)
            self.temp_data = data
            self.pause = True

    def get_mac_and_hostname(self, ip):
        conf.verb = 0
        # packet = IP(dst=str(ip), frag=0) / ICMP()
        # send = sr1(packet, timeout=2)
        # send_message_logging_to_server(action='debug_send', info=str(packet))
        # if send:
        #
        #     send_message_logging_to_server(action='debug_send', info=str(send.show2(dump=True)))
        # else:
        #
        #     send_message_logging_to_server(action='debug_send', info=f'no device: {ip}')


        # Обработка полученного ответа
        # if send:
        try:
            # hostname = received_packet[ARP].psrc
            url = urllib.parse.urljoin('http://' + ip, auth_dir)
            sid = self.AuthPhone(url)
            if isinstance(sid, dict):
                return sid

            if isinstance(sid, str) and sid:
                headers = {
                    "Cookie": f'locale=en; session-identity={str(sid)}; session-role=admin',
                    "Referer": url,
                    "Origin": url,
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Connection": "keep-alive"
                }
                payload = {'request': params_info, "sid": sid}

                info_url = urllib.parse.urljoin('http://' + ip, get_system_info_api)
                get = requests.post(info_url, data=payload, headers=headers)
                if 'response' in get.json():
                    if get.json()['response'] == 'success' and 'body' in get.json():
                        body = get.json()['body']
                        # print(body)
                        # self.phones_valid_list.append()
                        return {
                            "model": body['Pphone_model'],
                            'SIP': body['P35'],
                            "SIP_account_work": f'{body["PAccountRegistered1"] == "1"}',
                            "ip": ip,
                            "mac": body['P67'],
                        }
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            print(e)

    def run(self):
        print('run')
        self.append_to_log.emit('run')
        self.enable_button.emit(False)
        send_message_logging_to_server(action='сканирование сети', info=str(self.list_ip))
        # network_obj = ipaddress.ip_network('192.168.80.0/22')
        # self.total_hosts.emit(network_obj.num_addresses-2)
        # for idx, ip in enumerate(network_obj.hosts()):
        #     print(idx+1, ip)
        #     time.sleep(0.1)
        #     self.current_host.emit(idx)
        # # return 0
        for i in self.list_ip:

            date = datetime.now().strftime("%Y_%m_%d")
            excel_path = self.output_excel_path + '/' + i['name'] + date + '_phones.xlsx'
            self.current_city.emit('сканируется город: ' + i['name'] + f'\nпуть: {excel_path}')
            count_data = 0
            df = pd.DataFrame(columns=['model', 'SIP', 'SIP_account_work', 'ip', 'mac'])
            df.to_excel(excel_path, index=False, sheet_name=i['name'])
            self.temp_data = None
            for j in i['ip']:
                network_obj = ipaddress.ip_network(j)
                self.total_hosts.emit(network_obj.num_addresses - 2)
                for idx, ip in enumerate(network_obj.hosts()):
                    self.current_host.emit(idx + 1)
                    # print(ip)
                    data = self.get_mac_and_hostname(str(ip))

                    if self.pause:
                        while self.pause:
                            time.sleep(1)
                            try:
                                open(excel_path, "r+")  # or "a+", whatever you need
                                self.pause = False
                            except IOError:
                                print("Could not open file! Please close Excel. Press Enter to retry.")

                    if self.temp_data:
                        # count_data += 1
                        print('temp data: ' + str(self.temp_data))
                        self.data_to_excel(self.temp_data, excel_path, count_data, i['name'])
                        self.temp_data = None

                    if data:
                        count_data += 1
                        self.data_to_excel(data, excel_path, count_data, i['name'])
                        self.search_count_phones.emit(count_data)
                    # print(ip, self.pause, str(self.temp_data))

        print('end')
        self.enable_button.emit(True)
        self.append_to_log.emit('Сканирование завершено')

        # df = df.T
        # print(df)


class SearchPhoneWidget(QWidget):
    def __init__(self, parent=None):
        super(SearchPhoneWidget, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.checkbox_all_city.clicked.connect(self.set_allcity)
        self.ui.pushButton_2.clicked.connect(self.on_start_scan)
        self.ui.groupBox.setTitle('Выберите город')
        self.list_ip = []
        self.init_checkbox_clicked()
        self.th = PhoneSearchThread()
        self.th.current_host.connect(self.edit_current_host)
        self.th.total_hosts.connect(self.set_total_host)
        self.th.current_city.connect(self.set_current_city)
        self.th.append_to_log.connect(self.append_to_text_edit)
        self.th.error_message.connect(self.show_error)
        self.th.enable_button.connect(self.enable_buttons)
        self.th.search_count_phones.connect(self.set_current_numbers_phone)
        self.ui.pushButton.clicked.connect(self.selectDirectory)
        self.output_excel_path = ''
        self.ui.pushButton_2.setEnabled(False)
        self.ui.textEdit.setReadOnly(True)
        self.set_current_numbers_phone(0)

    @Slot(int)
    def set_current_numbers_phone(self, number):
        self.ui.label_search_count.setText(str(number))

    @Slot(bool)
    def enable_buttons(self, enable_button):
        self.ui.pushButton.setEnabled(enable_button)
        self.ui.pushButton_2.setEnabled(enable_button)
        for i in self.ui.groupBox.children():
            if isinstance(i, QCheckBox):
                i.setEnabled(enable_button)

        self.ui.checkbox_Kazan.setEnabled(False)
        self.ui.checkbox_VelikiyNovgorod.setEnabled(False)
        self.ui.checkbox_Ekb.setEnabled(False)

    @Slot(str)
    def append_to_text_edit(self, text):
        # print(text)
        self.ui.textEdit.append(text)

    @Slot(str)
    def show_error(self, error_string):
        msgBox = QMessageBox()
        msgBox.setIcon(msgBox.Icon.Warning)
        msgBox.setText(error_string)
        msgBox.setWindowTitle("Ошибка")
        msgBox.exec()

    @Slot(int)
    def edit_current_host(self, number):
        self.ui.current_number.setText(str(number))

    @Slot(str)
    def set_current_city(self, city):
        self.ui.label_current_city.setText(city)

    @Slot(int)
    def set_total_host(self, number):
        self.ui.total_number.setText(str(number))

    def init_checkbox_clicked(self):
        self.ui.checkbox_voronezh.clicked.connect(lambda: self.add_city_to_list(vrn, self.ui.checkbox_voronezh))
        self.ui.checkbox_moscow.clicked.connect(lambda: self.add_city_to_list(msk, self.ui.checkbox_moscow))
        self.ui.checkbox_spb.clicked.connect(lambda: self.add_city_to_list(spb, self.ui.checkbox_spb))
        self.ui.checkbox_NN.clicked.connect(lambda: self.add_city_to_list(nn, self.ui.checkbox_NN))
        self.ui.checkbox_Krasnodar.clicked.connect(lambda: self.add_city_to_list(krd, self.ui.checkbox_Krasnodar))
        self.ui.checkbox_Tambov.clicked.connect(lambda: self.add_city_to_list(tmb, self.ui.checkbox_Tambov))
        self.ui.checkbox_Novosibirsk.clicked.connect(lambda: self.add_city_to_list(nvs, self.ui.checkbox_Novosibirsk))
        self.ui.checkbox_Stavropol.clicked.connect(lambda: self.add_city_to_list(stv, self.ui.checkbox_Stavropol))
        self.ui.checkbox_Razan.clicked.connect(lambda: self.add_city_to_list(rzn, self.ui.checkbox_Razan))

    def add_city_to_list(self, city: dict, checkbox: QCheckBox):
        if checkbox.isChecked():
            self.list_ip.append(city)
        else:
            self.list_ip = list(filter(lambda i: i['name'] != city['name'], self.list_ip))
        print(self.list_ip)

    def set_allcity(self):
        checked = self.ui.checkbox_all_city.isChecked()
        for i in self.ui.groupBox.children():
            if isinstance(i, QCheckBox):
                if checked and i != self.ui.checkbox_all_city:
                    i.click()
                if not checked:
                    if self.list_ip:
                        self.list_ip.clear()
                    i.setChecked(checked)

    def selectDirectory(self):
        selected_directory = QFileDialog.getExistingDirectory()
        # Use the selected directory...
        print('selected_directory:', selected_directory)
        self.output_excel_path = selected_directory
        if selected_directory:
            self.ui.pushButton_2.setEnabled(True)

    def on_start_scan(self):
        self.th.set_list_ip(self.list_ip)
        self.th.set_path(self.output_excel_path)
        self.th.start()
        # print(self.list_ip)

        # for i in self.list_ip:
        #     for j in i['ip']:
        #         for f in range(100, 141):
        #             ip = str(j).rstrip('0')+str(f)
        #             self.get_mac_and_hostname(ip)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SearchPhoneWidget()
    window.show()
    sys.exit(app.exec())
