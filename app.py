from pathlib import Path
import json
import logging

DATA_FILE = Path("data.json")
CONFIG_FILE = Path("config.json")

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_config():
    try:
        return json.loads(CONFIG_FILE.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return {"currency": "PKR"}


def load_data():
    try:
        return json.loads(DATA_FILE.read_text())
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        logging.error("Invalid data.json file.")
        return []


def save_data(records):
    DATA_FILE.write_text(json.dumps(records, indent=2))


def add_sale(records):
    customer = input("Customer name: ").strip()
    product = input("Product: ").strip()

    if not customer or not product:
        print("Customer and product are required.")
        return

    try:
        amount = float(input("Amount: "))

        if amount <= 0:
            raise ValueError

    except ValueError:
        print("Please enter a valid positive amount.")
        return

    records.append({
        "customer": customer,
        "product": product,
        "amount": amount
    })

    save_data(records)
    logging.info("Sale added for %s", customer)

    print("Sale saved successfully.")


def show_summary(records, currency):
    total = sum(item["amount"] for item in records)

    print(f"\nSales records: {len(records)}")
    print(f"Total sales: {currency} {total:,.2f}")


def main():
    config = load_config()
    records = load_data()

    while True:
        print("\n=== Simple Sales Tracker ===")
        print("1. Add sale")
        print("2. View summary")
        print("3. View records")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_sale(records)

        elif choice == "2":
            show_summary(records, config["currency"])

        elif choice == "3":
            if not records:
                print("No records found.")
            else:
                for i, item in enumerate(records, 1):
                    print(
                        f"{i}. {item['customer']} | "
                        f"{item['product']} | "
                        f"{config['currency']} {item['amount']:,.2f}"
                    )

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()