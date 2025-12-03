import argparse
from pprint import pprint
from textwrap import wrap

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--file",
        required=True,
        type=str,
        help="Path to safe comibination input file"
    )

    return parser.parse_args()

def import_product_id(filepath):
    product_ids = list()
    with open(filepath, "r") as file:
        file_content = file.read()
        product_ids = file_content.split(",")

    return product_ids

def get_real_ranges(product_ids):
    real_ranges = list()
    for prod_id in product_ids:
        id_range = dict()
        id_range['start'] = prod_id.split("-")[0]
        id_range['end'] = prod_id.split("-")[1]
        real_ranges.append(id_range)

    return real_ranges

def check_for_bad_id(prod_id_ranges):
    bad_ids = set()
    for r in prod_id_ranges:
        pprint(r)
        start = int(r['start'])
        end = int(r['end'])
        for i in range(start, end+1 ):
            len_of_id = len(str(i))
            width = max(1, len_of_id // 2)
            split_id = wrap(str(i), width )
            for x in range(len(split_id)):
                for y in range(x+1, len(split_id)):
                    if split_id[x] == split_id[y]:
                        bad_id = split_id[x]+split_id[y]
                        if not bad_id.startswith('0'):
                            bad_ids.add(int(bad_id))
    return bad_ids

def main():
    args = parse_args()

    product_ids = import_product_id(args.file)

    prod_id_ranges = get_real_ranges(product_ids)

    bad_ids = check_for_bad_id(prod_id_ranges)

    bad_id_sum = int()
    for bad_id in bad_ids:
        bad_id_sum += bad_id
    pprint(bad_id_sum)

if __name__ == "__main__":
    main()
