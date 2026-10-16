from typing import List


def printer_queue_order(pages: List[int]) -> List[int]:
    """
    Problem 1: Round-robin printer.

    Given the number of pages for each document (in submission order),
    simulate round-robin printing (one page at a time, front of queue
    to back of queue) and return the document indices in the order
    they finish printing.

    Args:
        pages: pages[i] is the number of pages in document i.

    Returns:
        List of document numbers in the order they finish printing.
    """
    queue = []

    for i in range(len(pages)):
        if pages[i] > 0:
            queue.append([i, pages[i]])

    result = []

    while len(queue) > 0:
        document = queue.pop(0)

        index = document[0]
        remaining_pages = document[1] - 1

        if remaining_pages == 0:
            result.append(index)
        else:
            queue.append([index, remaining_pages])

    return result
    pass


if __name__ == "__main__":
    # Example sanity check (see test.py for the real test cases)
    print(printer_queue_order([1, 1, 1]))  # expected: [0, 1, 2]
