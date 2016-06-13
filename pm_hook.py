from mail_orm import Client


def process_message_hook(peer, mailfrom, rcpttos, data):
    print("Message processed.")
    print(mailfrom)
    for c in Client.__table__.columns:
        print(c)

    for c in Client.__table__.foreign_keys:
        print(c)

    print(Client.log_me())
