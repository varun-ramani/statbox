def generate_batches(start, stop, size):
    num_batches = int((stop - start) / size) + 1

    batches = []

    for i in range(0, num_batches):
        batch_start = start + i*size
        batch_end = batch_start + size-1

        if batch_end > stop:
            batches.append((batch_start, stop))
        else:
            batches.append((batch_start, batch_end))

    return batches