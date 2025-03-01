import requests
import time
from colorama import Fore, Style, init
from rich.progress import Progress
from tabulate import tabulate

init(autoreset=True)  # Inisialisasi colorama agar warna otomatis reset

def check_api_status(url):
    try:
        with Progress() as progress:
            task = progress.add_task(f"[cyan]Mengecek {url}...[/]", total=10)
            for _ in range(10):
                time.sleep(0.1)
                progress.update(task, advance=1)
        
        response = requests.get(url, timeout=5)
        status = "UP" if response.status_code == 200 else "DOWN"
        color = Fore.GREEN if status == "UP" else Fore.RED
        return [url, response.status_code, f"{color}{status}{Style.RESET_ALL}"]
    except requests.exceptions.RequestException:
        return [url, "N/A", f"{Fore.RED}DOWN{Style.RESET_ALL}"]

def main():
    print(Fore.YELLOW + "\n=== REST API STATUS CHECKER ===\n" + Style.RESET_ALL)
    results = []
    
    while True:
        url = input(Fore.CYAN + "Masukkan URL API (atau ketik 'exit' untuk keluar): " + Style.RESET_ALL)
        if url.lower() == 'exit':
            break
        results.append(check_api_status(url))
        
        print("\n" + tabulate(results, headers=["URL", "Status Code", "Status"], tablefmt="fancy_grid"))
        print("\n")

    print(Fore.YELLOW + "Terima kasih telah menggunakan REST API Status Checker!" + Style.RESET_ALL)
    print(Fore.YELLOW + "Tool By 'Noval @2025' Please Dont Remove This Credit" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
