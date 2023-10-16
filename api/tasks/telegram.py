from pyrogram import Client, filters
from pyrogram.errors.exceptions import bad_request_400

session = 'AgGGgLIArg0q_KYai1Jl418H33qm5vtWJhnDOOp_YYn8r3SZDdB7Hg4ATHy2j6A3ReaGrw6IkTJJE6PZRj236aIDI5nm-s432RE06FWomypKjHf8rR5X9XHu-wdycKXH6zNtx6G7OWDf_vAAkF0KaWb3ahkF5uTu0IPRC7iVuXzjg2vCpkoIH5pxwsxLl-pUbJOH0b983Y3WUvRCrA57wYgMAVfVgPZJqVA0-Ej60-lvXEMlIRom6bgoziiwnbCuEcCXNL-gXIr5bFw4q7ZC5Uguo-gMWhWy-t5lhVTYnrS7fQEFcrdB0knkMECUAZsqFNLoMJmMlPcs_iHaBcSIZMIZAGSmSwAAAAF0BHO9AA'

app = Client(
    'my_account',
    api_id='25591986',
    api_hash='f9632825859749739ad681048b157a00',
    phone_number='+79957814060',
    session_string=session
)


def check_user_in_channel_task(channel_id: str, user_id: str):
    with app:
        #s = app.export_session_string()
        #print(s)
        #print(channel_id)
        for member in app.get_chat_members(channel_id):
            if user_id == str(member.user.id):
                #print('DONE')
                return True
        return False

#check_user_in_channel_task('test_chan222', '495363986')
