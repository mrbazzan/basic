
from threading import Thread
import time


class EventBinder:
    callbacks = []

    def __call__(self, func):
        self.callbacks.append(func)
        return func

    def fire(self, *args):
        for func in self.callbacks:
            func(*args)


class Downloader:
    def __init__(self, url_list):
        self.url_list = url_list
        self.done = EventBinder()

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
        self.done.fire(count, end_time - start_time)


if __name__ == "__main__":
    downloader = Downloader(range(1,13))

    @downloader.done
    def _(count, time_elapsed):
        print(f"Fetched {count} files in {time_elapsed} seconds.")

    @downloader.done
    def _(count, time_elapsed):
        print(f"{count} downloaded in {time_elapsed/60.0:.3f} seconds.")

    downloader.start_downloads()
    print("Waiting for the result...")

