import random
import csv
import logging
import uuid
from faker import Faker
from datetime import date, datetime, timedelta
import polars as pl

# Configura logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler()]
)

def create_data(locale: str) -> Faker:
    logging.info(f"Created synthetic data for {locale.split('_')[-1]} country code.")
    return Faker(locale)

def generate_record(fake: Faker) -> list:
    """Genera un único registro de usuario falso compatible con tu tabla."""
    person_name = fake.name()
    user_name = person_name.replace(" ", "").lower()
    email = f"{user_name}@{fake.free_email_domain()}"
    personal_number = random.randint(10000000000, 99999999999)  # numeric
    birth_date = fake.date_of_birth()  # string
    address = fake.address().replace("\n", ", ")
    phone_number = fake.phone_number()
    mac_address = fake.mac_address()
    ip_address = fake.ipv4()
    iban = fake.iban()
    accessed_at = fake.time()  # HH:MM:SS
    session_duration = random.randint(0, 36000)
    download_speed = random.randint(0, 1000)
    upload_speed = random.randint(0, 800)
    consumed_traffic = random.randint(0, 2_000_000)
    unique_id_val = str(uuid.uuid4())

    return [
        person_name,
        user_name,
        email,
        personal_number,
        str(birth_date),
        address,
        phone_number,
        mac_address,
        ip_address,
        iban,
        accessed_at,
        session_duration,
        download_speed,
        upload_speed,
        consumed_traffic,
        unique_id_val
    ]

def write_to_csv(file_path: str, rows: int) -> None:
    fake = create_data("es_MX")
    headers = [
        "person_name", "user_name", "email", "personal_number", "birth_date",
        "address", "phone", "mac_address", "ip_address", "iban",
        "accessed_at", "session_duration", "download_speed",
        "upload_speed", "consumed_traffic", "unique_id"
    ]
    with open(file_path, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(headers)
        for _ in range(rows):
            writer.writerow(generate_record(fake))
    logging.info(f"Written {rows} records to the CSV file.")

def add_id(file_name: str) -> None:
    """Añade UUID único a cada fila (opcional, ya lo agregamos en generate_record)."""
    pass  # ya se incluye en generate_record

def update_datetime(file_name: str, run: str) -> None:
    """Actualiza la columna 'accessed_at' si quieres modificar la fecha."""
    if run != "next":
        return
    df = pl.read_csv(file_name)
    current_time = datetime.now().replace(microsecond=0)
    yesterday_time = str(current_time - timedelta(days=1))
    df = df.with_columns(pl.lit(yesterday_time).alias("accessed_at"))
    df.write_csv(file_name)
    logging.info("Updated accessed timestamp.")

if __name__ == "__main__":
    logging.info(f"Started batch processing for {date.today()}.")
    output_file = f"data/batch_{date.today()}.csv"

    if str(date.today()) == "2024-09-14":
        records = 300_372
        run_type = "first"
    else:
        records = random.randint(0, 1_101)
        run_type = "next"

    write_to_csv(output_file, records)
    update_datetime(output_file, run_type)

    logging.info(f"Finished batch processing {date.today()}.")
