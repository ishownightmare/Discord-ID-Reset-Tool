class Paginator:
    def __init__(self, items, page_size=5):
        self.items = items
        self.page_size = page_size
        self.current_page = 0

    def get_page(self, page: int):
        start = page * self.page_size
        end = start + self.page_size
        return self.items[start:end]
