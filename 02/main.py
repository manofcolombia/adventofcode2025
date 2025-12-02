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
    bad_ids = list()
    for r in prod_id_ranges:
        pprint(r)
        start = int(r['start'])
        end = int(r['end'])
        for i in range(start, end+1 ):
            len_of_id = len(str(i))
            split_id = wrap(str(i), len_of_id // 2 )
            pprint(split_id)
            if split_id[0] == split_id[1]:
                bad_ids.append(i)
    return bad_ids

def main():
    args = parse_args()

    product_ids = import_product_id(args.file)

    prod_id_ranges = get_real_ranges(product_ids)

    bad_ids = check_for_bad_id(prod_id_ranges)

    pprint(bad_ids)

if __name__ == "__main__":
    main()
