
print("Hey bro How are you")
print("Check status")
print("Hello, I am Shubham For a new join in your team")


psycopg==3.3.4
psycopg-binary==3.3.4
typing_extensions==4.16.0
tzdata==2026.3


import csv
import psycopg
import os


HOST = "192.168.1.****"
PORT = 16432
DATABASE = "vanisetu_db"
USER = "postgres"
PASSWORD = "*****"

RECORDING_BASE_PATH = "/var/spool/asterisk/monitor/"
CSV_FILE_PATH = r"/var/opt/CDRDataMigration/CSV_To_Postgres/csvData-copy.txt"

MAPPER = {
    1: "src",
    2: "dst",
    3: "dcontext",
    4: "clid",
    5: "channel",
    6: "dstchannel",
    7: "lastapp",
    8: "lastdata",      
    9: "calldate",
    12: "duration",
    13: "billsec",      
    14: "disposition",
    16: "uniqueid"
}


try:
    conn = psycopg.connect(
        host=HOST,
        port=PORT,
        dbname=DATABASE,
        user=USER,
        password=PASSWORD
    )

    cursor = conn.cursor()

    print("Database Connected Successfully")

except Exception as e:
    print("Connection Error:", e)
    exit()



query = """
INSERT INTO public.cdr
(
    src,
    dst,
    dcontext,
    clid,
    channel,
    dstchannel,
    lastapp,
    lastdata,
    calldate,
    duration,
    billsec,
    disposition,
    uniqueid,
    linkedid,
    amaflags,
    recordingfile,
    ext_num 

)
VALUES
(
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s
)
"""



recordings = {}

def get_recording_path(base_path, calldate):
  
    year = calldate[:4]
    month = calldate[5:7]
    day = calldate[8:10]


    print(year, month, day)

    return os.path.join(base_path, year, month, day)



def find_recording_file(uniqueid, calldate):

  
    recording_path = get_recording_path(RECORDING_BASE_PATH, calldate)

    
    if not os.path.isdir(recording_path):
        return None

    for file_name in os.listdir(recording_path):

        
        if uniqueid in file_name:

            return os.path.join(recording_path, file_name)

    
    return None






count = 0

with open(CSV_FILE_PATH, "r", encoding="utf-8") as file:

    reader = csv.reader(file)

    for row in reader:
        data = {}
        for csv_index, db_column in MAPPER.items():
          data[db_column] = row[csv_index]

        if data["dcontext"] == "from-incoming":
         data["ext_num"] = data["dst"]

        elif data["dcontext"] == "from-outgoing":
         data["ext_num"] = data["src"]

        else:
         data["ext_num"] = None

        data["recordingfile"] = find_recording_file(
        data["uniqueid"],
        data["calldate"]
)



        values = (
            data[MAPPER[1]],
            data[MAPPER[2]],
            data[MAPPER[3]],
            data[MAPPER[4]],
            data[MAPPER[5]],
            data[MAPPER[6]],
            data[MAPPER[7]],
            data[MAPPER[8]],
            data[MAPPER[9]],
            data[MAPPER[12]],
            data[MAPPER[13]],
            data[MAPPER[14]],
            data[MAPPER[16]],
            data[MAPPER[16]],
            3,
            data["recordingfile"],
            data["ext_num"]
        )
        
        cursor.execute(query, values)
        conn.commit()
        print("Row Inserted Successfully")


        print(f"\n========== Row {count + 1} ==========")

        for key, value in data.items():
           print(f"{key} : {value}")

        count += 1

        if count == 1:
            break






