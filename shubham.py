print("HELLO")

print("Master change")


# Local Environment Settings
SECRET_KEY=local-dev-key-ashram-trust-shree-hari-mahadev-mandir-2026-xyz-local
DEBUG=True
ALLOWED_HOSTS=*
TIME_ZONE=Asia/Kolkata

BACKUP_EVERY_DAYS=7
BACKUP_ENTRY_TRIGGER=20
KEEP_BACKUPS=5
BACKUP_DIR=backup_data
# ASK_OWNER: Q4 Owner will set the production passphrase
BACKUP_PASSPHRASE=DevPassphrase123#

# ASK_OWNER: Q2 Google Sheet service account credentials
GOOGLE_SERVICE_ACCOUNT_JSON=
# ASK_OWNER: Q2 Google Sheet ID
GOOGLE_SHEET_ID=
# ASK_OWNER: Q3 Google Drive Folder ID
GOOGLE_DRIVE_FOLDER_ID=





# Django Configuration
SECRET_KEY=change-this-to-a-very-secure-random-secret-key-for-production
DEBUG=False
ALLOWED_HOSTS=127.0.0.1,localhost,192.168.1.100

# Timezone
TIME_ZONE=Asia/Kolkata

# Backup Configuration
BACKUP_EVERY_DAYS=7
BACKUP_ENTRY_TRIGGER=20
KEEP_BACKUPS=5
BACKUP_DIR=backup_data
# ASK_OWNER: Q4 Passphrase chosen by owner for AES-256 backup encryption
BACKUP_PASSPHRASE=

# Google Sheet & Drive Sync (Leave empty until owner provides)
# ASK_OWNER: Q2 Path to service account JSON credentials
GOOGLE_SERVICE_ACCOUNT_JSON=
# ASK_OWNER: Q2 Google Sheet ID or URL
GOOGLE_SHEET_ID=
# ASK_OWNER: Q3 Google Drive folder ID for uploads
GOOGLE_DRIVE_FOLDER_ID=
