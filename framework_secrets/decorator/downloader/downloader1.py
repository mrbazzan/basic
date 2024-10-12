
from threading import Thread
import time


class Downloader:
    def __init__(self, url_list):
        self.url_list = url_list

    def done(self, func):
        self.callback = func
        return func

    def start_downloads(self):
        thread = Thread(target=self.download_all)
        thread.start()

    def download_all(self):
        count = 0
        start_time = time.time()
        for url in self.url_list:
            print("Downloading: ", url)
            time.sleep(0.3)  # jump back to the main thread due to the wait.
            count += 1

        end_time = time.time()
        self.callback(count, end_time - start_time)


if __name__ == "__main__":
    downloader = Downloader(range(1,13))

    @downloader.done
    def ondone(num_downloaded, time_elapsed):
        print(f"Fetched {num_downloaded} files in {time_elapsed} seconds.")

    downloader.start_downloads()
    print("Waiting for the result...")

