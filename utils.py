# Returns count and percentage of each item
def breakdown_by_item(items):
    none_num = items[None]
    items.pop(None)
    items['noemailfound'] = none_num

    total = sum([items[key] for key in items])

    return {
        key: {
            "count": items[key],
            "percentage": (items[key] / total) * 100,
            "proportion": (items[key] / total)
        } for key in items
    }

# Generates a histogram from breakdown_by_item
def print_histogram(items):
    breakdown = breakdown_by_item(items)

    for key in breakdown:
        print("{:80}:{:20} {:5}".format(key, "#" * int((int(breakdown[key]['percentage']) / 5)), breakdown[key]['count']))