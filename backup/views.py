from django.shortcuts import render, redirect, HttpResponse
from decorators import login_required
import subprocess
from .models import Snapshot
import smtplib
import ssl
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from backend.settings import SMTP, PORT, SENDER, PASSWORD


@login_required(login_url='login')
def backups(request):
    page_title = "Backups"
    snapshots = Snapshot.objects.all()

    context = {'page_title': page_title, 'snapshots': snapshots}
    return render(request, 'backup/backup.html', context)


@login_required(login_url='login')
def backup(request):
    snap = Snapshot.objects.create()
    subprocess.call(['backup/utils/backup.sh', f'{snap.uuid}'])
    snap.file = f"backups/{snap.uuid}.json"
    snap.save()
    return redirect('backups')


@login_required(login_url='login')
def restore(request, slug):
    snap = Snapshot.objects.get(uuid=slug)
    subprocess.call(['backup/utils/restore.sh', f'{snap.uuid}'])
    return redirect('/')


@login_required(login_url='login')
def confirmSnapshot(request, slug):
    snap = Snapshot.objects.get(uuid=slug)
    page_title = "Confirmation"
    sender = "snapshot"

    context = {'page_title': page_title, 'snap': snap, 'sender': sender}
    return render(request, 'base/confirm.html', context)


@login_required(login_url='login')
def delBackup(request, slug):
    snap = Snapshot.objects.get(uuid=slug)
    snap.delete()
    return redirect('backups')


def sendBackup(request, slug):
    snap = Snapshot.objects.get(uuid=slug)
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y")

    smtp = SMTP
    port = PORT
    sender = SENDER
    password = PASSWORD

    subject = f"Backup: {date_time}"
    receiver = 'marbrume.alias@gmail.com'
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject

    with open(rf'./static/{snap.file}', "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {snap.uuid}.json",
    )

    message.attach(part)
    text = message.as_string()

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp, port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, text)

    return redirect('backups')
