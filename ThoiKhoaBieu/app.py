from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import webbrowser


PROJECT_DIR = Path(__file__).resolve().parent
HOST = "127.0.0.1"
PORT = 8000
MAX_PORT_ATTEMPTS = 10


def create_server(handler):
	for port in range(PORT, PORT + MAX_PORT_ATTEMPTS):
		try:
			return ThreadingHTTPServer((HOST, port), handler)
		except OSError:
			continue

	raise OSError(
		f"Khong the mo cong tu {PORT} den {PORT + MAX_PORT_ATTEMPTS - 1}."
	)


def main() -> None:
	"""Serve the web app and open the login page in the default browser."""
	handler = partial(SimpleHTTPRequestHandler, directory=str(PROJECT_DIR))
	server = create_server(handler)
	login_url = f"http://{HOST}:{server.server_port}/Login/"

	print(f"Ung dung dang chay tai {login_url}")
	print("Nhan Ctrl+C de dung ung dung.")
	webbrowser.open(login_url)

	try:
		server.serve_forever()
	except KeyboardInterrupt:
		print("\nDa dung ung dung.")
	finally:
		server.server_close()


if __name__ == "__main__":
	main()
