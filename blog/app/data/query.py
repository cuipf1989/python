#!/usr/bin/python
# coding=utf-8

from .common import *
from ..proto import gm_pb2
from .. import tcp_connect


def list_server():
    req = gm_pb2.GMGetAllServerListReq()
    header = Interact.make_header(req.DESCRIPTOR.full_name)
    tcp_connect.send(Interact.encode(header, req))


def register_num(server_id=0):
    req = gm_pb2.GMGetServerRegisterNumberReq()
    header = Interact.make_header(req.DESCRIPTOR.full_name)
    if server_id != 0:
        req.server_ids.append(server_id)
    tcp_connect.send(Interact.encode(header, req))


def online_status(server_id=0):
    req = gm_pb2.GMGetOnlineInSwitchReq()
    header = Interact.make_header(req.DESCRIPTOR.full_name)
    if server_id != 0:
        req.server_ids.append(server_id)
    tcp_connect.send(Interact.encode(header, req))


def query_user(uid, channel=0):
    req = gm_pb2.GMQueryUserReq()
    header = Interact.make_header(req.DESCRIPTOR.full_name)
    req.players.uid = uid
    req.players.channel = channel
    tcp_connect.send(Interact.encode(header, req))

@staticmethod
def tunnel():
    req = gm_pb2.GMGetTunnelServerInfoReq()
    header = Interact.make_header(req.DESCRIPTOR.full_name)
    tcp_connect.send(Interact.encode(header, req))


def query_online(uid, channel=0):
    req = gm_pb2.GMQueryUserOnlineReq()
    header = Interact.make_header(req.DESCRIPTOR.full_name)
    info = req.players.add()
    info.uid = uid
    info.channel = channel
    tcp_connect.send(Interact.encode(header, req))


def query_user_info(server_id):
    req = gm_pb2.GMQueryAllUserBaseInfoOnlineReq()
    header = Interact.make_header(req.DESCRIPTOR.full_name)
    req.server_id = server_id
    tcp_connect.send(Interact.encode(header, req))


def kick_user(uid, channel=0):
    req = gm_pb2.GMKickUserReq()
    header = Interact.make_header(req.DESCRIPTOR.full_name)
    req.uid = uid
    req.channel = channel
    tcp_connect.send(Interact.encode(header, req))


def user_detail(uid, channel=0):
    req = gm_pb2.GMQueryOnlineUserInfoReq()
    header = Interact.make_header(req.DESCRIPTOR.full_name)
    req.uid = uid
    req.channel = channel
    tcp_connect.send(Interact.encode(header, req))





def push(msg, server_ids):
    req = gm_pb2.GMPushMessageReq()
    header = Interact.make_header(req.DESCRIPTOR.full_name)
    req.push_message = msg
    if len(server_ids) != 0:
        for item in server_ids:
            req.server_ids.append(int(item))
    tcp_connect.send(Interact.encode(header, req))


def all_room(server_id):
    req = gm_pb2.GMGetAllServerRoomReq()
    header = Interact.make_header(req.DESCRIPTOR.full_name)
    req.server_id = server_id
    tcp_connect.send(Interact.encode(header, req))


def room_info(server_id, room_id):
    req = gm_pb2.GMGetRoomInfoReq()
    header = Interact.make_header(req.DESCRIPTOR.full_name)
    req.server_id = server_id
    req.room_id = room_id
    tcp_connect.send(Interact.encode(header, req))


def craft_info(uid, channel=0):
    req = gm_pb2.GMGetPlayerCraftInfoReq()
    header = Interact.make_header(req.DESCRIPTOR.full_name)
    req.uid = uid
    req.channel = channel
    tcp_connect.send(Interact.encode(header, req))


def friend_list(uid, channel=0):
    req = gm_pb2.GMGetFriendListReq()
    header = Interact.make_header(req.DESCRIPTOR.full_name)
    req.uid = uid
    req.channel = channel
    tcp_connect.send(Interact.encode(header, req))


def black_list(uid, channel=0):
    req = gm_pb2.GMGetBlackListReq()
    header = Interact.make_header(req.DESCRIPTOR.full_name)
    req.uid = uid
    req.channel = channel
    tcp_connect.send(Interact.encode(header, req))


def push_list(uid, channel=0):
    req = gm_pb2.GMGetPushListReq()
    header = Interact.make_header(req.DESCRIPTOR.full_name)
    req.uid = uid
    req.channel = channel
    tcp_connect.send(Interact.encode(header, req))


def send_mail(mail_info):
    req = gm_pb2.GMSendMailReq()
    header = Interact.make_header(req.DESCRIPTOR.full_name)
    mail = req.mail_content
    mail.gm_uid = common.gid
    mail.addressee_type = mail_info.receive_type
    if mail_info.receive_type == 1:
        for item in mail_info.online_ids:
            mail.online_ids.append(item)
    elif mail_info.receive_type == 2:
        index = 0
        for item in mail_info.uids:
            mail.uids.append(item[0])
            mail.channels.append(item[1])
            index += 1
    mail.online_ids.append(mail_info.online_id)
    mail.sender = mail_info.sender.Interact.encode('utf-8')
    mail.title = mail_info.title.Interact.encode('utf-8')
    mail.content = mail_info.content.Interact.encode('utf-8')
    mail.valid_time = mail_info.valid_time
    mail.is_destroy = mail_info.is_destory
    mail.show_priority = (gm_pb2.MailContent.Normal if mail_info.priority == 0
                          else gm_pb2.MailContent.Top)
    mail.is_popping = mail_info.is_popping
    mail.delayed_time = mail_info.delayed_time
    for item in mail_info.attachments:
        attachment = mail.attachment_list.add()
        attachment.id = item[0]
        attachment.count = item[1]
    if len(mail.attachment_list) != 0:
        mail.mail_type = 1
    else:
        mail.mail_type = 0
    print(req)
    tcp_connect.send(Interact.encode(header, req))


def unsend_mail():
    req = gm_pb2.GMQueryUnsendMailReq()
    header = Interact.make_header(req.DESCRIPTOR.full_name)
    tcp_connect.send(Interact.encode(header, req))


def del_unsend_mail(mail_id):
    req = gm_pb2.GMDeleteUnsendMailReq()
    header = Interact.make_header(req.DESCRIPTOR.full_name)
    req.mail_ids.append(mail_id)
    tcp_connect.send(Interact.encode(header, req))


