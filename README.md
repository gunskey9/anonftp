# EkoAnonFTP - Anonymous FTP Server Scanner

![EkoAnonFTP](https://example.com/path/to/logo.png)

EkoAnonFTP is a Python program designed to scan multiple FTP servers for anonymous login and check for visible files on those servers. It allows you to provide a list of IP addresses or hostnames in a file, and then it goes through each target and checks if anonymous login is allowed on port 21. If allowed, it also retrieves a list of visible files on the server.

## Prerequisites

Before running the EkoAnonFTP program, make sure you have the following installed:

- Python 3
- Python `ftplib` library
- Python `socket` library
- Python `tqdm` library
- figlet

You can install the required Python libraries using `pip`:

```bash
pip install ftplib tqdm
```

You also need to have the `figlet` program installed on your system. On Ubuntu, you can install it using:

```bash
sudo apt-get install figlet
```

## How to Use

1. Clone this repository or download the `ekoanonftp.py` file.

2. Ensure the IP addresses or hostnames are listed in a file (one per line) that you want to scan for anonymous FTP login. The file should have the following format:

   ```
   192.168.1.1
   example.com
   ftp.example.org
   ```

3. Open a terminal and navigate to the directory containing the `ekoanonftp.py` file.

4. To run the program, use the following command:

   ```bash
   python ekoanonftp.py
   ```

5. The program will prompt you to enter the file location containing the IPs or hostnames to scan. Type the path to the file and press Enter. Alternatively, you can type `q` and press Enter to quit the program.

6. The program will start scanning the FTP servers one by one and display the progress using a progress bar. If a server allows anonymous login, it will be listed, and if visible files are found, they will also be displayed.

## Disclaimer

This program is intended for educational and ethical purposes only. Unauthorized scanning of FTP servers is against the law and might lead to legal consequences. Always ensure that you have proper authorization before scanning any server.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Credits

This project was created by [Your Name](https://github.com/yourusername). Feel free to contribute to the project by submitting issues or pull requests.

## Contact

If you have any questions or suggestions regarding the EkoAnonFTP program, please feel free to contact us at [email@example.com](mailto:email@example.com).
