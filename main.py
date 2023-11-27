# This is a sample Python script.


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
URL_HOME = "http://192.168.36.141"

SIP_ID = '256'
SIP_PASS = 'CXL5qjsFcWe6'










def print_hi(name):
    timing = time.time()
    # reset_phone()
    # Use a breakpoint in the code line below to debug your script.
    sid = authorization()

    if sid:
        print('Авторизация успешна')

        set_sid_to_all_dict(sid)
        reset_phone()
        # return 0
        sid = authorization()



        set_sid_to_all_dict(sid)

        post_account_gen_setting['P270'] = SIP_ID
        post_account_gen_setting['P35'] = SIP_ID
        post_account_gen_setting['P36'] = SIP_ID
        post_account_gen_setting['P3'] = SIP_ID
        post_account_gen_setting['P34'] = SIP_PASS

        print(f'sid: {sid} ID USER: {SIP_ID}')


        request_post = urllib.parse.urljoin(URL_HOME, request_value_dir)

        r_network_setting = requests.post(request_post, data=post_network_setting)
        print(f'network_setting /// time: {time.time() - timing} {get_status_JSON(r_network_setting.json())}')

        r_post_account__basic_setting = requests.post(request_post, data=post_account__basic_setting)
        print(f'account basic setting /// time: {time.time() - timing} {get_status_JSON(r_post_account__basic_setting.json())}')

        r_post_account__security_setting = requests.post(request_post, data=post_account__security_setting)
        print(f'security setting /// time: {time.time() - timing} {get_status_JSON(r_post_account__security_setting.json())}')

        r_post_account__audio_setting = requests.post(request_post, data=post_account__audio_setting)
        print(f'audio setting /// time: {time.time() - timing} {get_status_JSON(r_post_account__audio_setting.json())}')

        r_post_account__call_setting = requests.post(request_post, data=post_account__call_setting)
        print(f'account call setting time: {time.time() - timing} {get_status_JSON(r_post_account__call_setting.json())}')

        r_post_setting_gen_setting = requests.post(request_post, data=post_setting_gen_setting)
        print(f'setting gen setting /// time: {time.time() - timing} {get_status_JSON(r_post_setting_gen_setting.json())}')

        r_post_setting_call_features = requests.post(request_post, data=post_setting_call_features)
        print(f'call features /// time: {time.time() - timing} {get_status_JSON(r_post_setting_call_features.json())}')

        r_post_setting_date_time = requests.post(request_post, data=post_setting_date_time)
        print(f'datetime /// time: {time.time() - timing} {get_status_JSON(r_post_setting_date_time.json())}')

        r_post_display_lang = requests.post(request_post, data=post_display_lang)
        print(f'display lang /// time: {time.time() - timing} {get_status_JSON(r_post_display_lang.json())}')

        r_post_account_gen_setting = requests.post(request_post, data=post_account_gen_setting)
        print(f'account gen setting /// time: {time.time() - timing} {get_status_JSON(r_post_account_gen_setting.json())}')




    print('Настройка закончена')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
