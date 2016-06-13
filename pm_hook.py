from mail_orm import Client

def process_message_hook(peer, mailfrom, rcpttos, data):
    print("Message processed.")
    print(mailfrom)
    for email in Client.client_email:
        if (email in mailfrom):
            print("confirmed. email belongs to client")