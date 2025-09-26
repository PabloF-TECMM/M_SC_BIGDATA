import csv
import logging
import os
from faker import Faker
import random
from datetime import datetime

# Create data using faker
def create_data(locale: str = "es_MX") -> Faker:
    return Faker(locale)

# Generate a single record
def generate_record(fake: Faker) -> list:
    return [
        fake.name(),
        fake.user_name(),
        fake.email(),
        fake.ssn(),
        fake.date_of_birth(),
        fake.address(),
        fake.phone_number(),
        fake.mac_address(),
        fake.ipv4(),
        fake.iban(),
        fake.date_time_this_year(),
        random.randint(1, 500),  # session_duration
        random.uniform(1.0, 100.0),  # download_speed
        random.uniform(1.0, 100.0),  # upload_speed
        random.randint(100, 10000)  # consumed_traffic
    ]

# Write records to CSV
def write_to_csv(file_path: str, rows: int) -> None:
    fake = create_data("es_MX")

    headers = [
        "person_name", "user_name", "email", "personal_number", "birth_date", "address",
        "phone", "mac_address", "ip_address", "iban", "accessed_at",
        "session_duration", "download_speed", "upload_speed", "consumed_traffic"
    ]

    # Asegurar que la carpeta exista
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for _ in range(rows):
            writer.writerow(generate_record(fake))
    logging.info(f"Written {rows} records to the CSV file.")

# Batch processing
def batch_process(output_file: str, batch_size: int, num_batches: int) -> None:
    for i in range(num_batches):
        records = batch_size
        write_to_csv(f"{output_file}/batch_{datetime.now().date()}.csv", records)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    logging.info(f"Started batch processing for {datetime.now().date()}.")

    output_file = "chapter_2/work_2/data_2"
    batch_size = 100
    num_batches = 1

    batch_process(output_file, batch_size, num_batches)