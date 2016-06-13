from mail_orm import Client

def process_message_hook(peer, mailfrom, rcpttos, data):
    print("Message processed.")
    print(mailfrom)
    if (Client.client_name in mailfrom):
        print("confirmed. email belongs to client")