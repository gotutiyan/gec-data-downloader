import argparse

def main(args):
    m2_contents = [open(f'10gec_annotations/A{i}.m2').read().replace('|||0\n', f'|||{i-1}\n').split('\n\n') for i in range(1, 10+1)]
    final_m2 = []
    for sent_id in range(len(m2_contents[0])):
        new_m2 = []
        for ref_id in range(10):
            c = m2_contents[ref_id][sent_id]
            c = c.split('\n')
            if ref_id != 0:
                c = c[1:]  # remove 'S ' line for other than the first reference.
            new_m2 += c
        final_m2.append('\n'.join(new_m2))
    print('\n\n'.join(final_m2))
            
        


def get_parser():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = get_parser()
    main(args)