#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination

This module provides a `Server` class for paginating a database
of popular baby names.
"""

import csv
from typing import List, Dict


class Server:
    """
    Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset

        Returns:
            List[List]: The dataset excluding the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0

        Returns:
            Dict[int, List]: A dictionary mapping index to dataset rows.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieves a specific page of data from the dataset.

        Args:
            index (int, optional): The starting index (0-indexed).
            Defaults to None.
            page_size (int, optional): The number of items per page.
            Defaults to 10.

        Returns:
            Dict: A dictionary containing pagination information.
                - 'index': Index of the first item in the current page.
                - 'next_index': Index of the first item in the next
                page (or None if no next page).
                - 'page_size': The current page size.
                - 'data': Actual page of the dataset.
        """
        dataset = self.indexed_dataset()
        data_length = len(dataset)
        assert 0 <= index < data_length
        response = {}
        data = []
        response['index'] = index
        for i in range(page_size):
            while True:
                curr = dataset.get(index)
                index += 1
                if curr is not None:
                    break
            data.append(curr)
        response['data'] = data
        response['page_size'] = len(data)
        response['next_index'] = index if dataset.get(index) else None
        return response
