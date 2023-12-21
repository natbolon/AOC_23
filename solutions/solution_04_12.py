import numpy as np
import argparse

def get_points(input):
    total_points = 0
    if isinstance(input, str):
        input = input.split('\n')
    
    for card in input:
        winners, gotten = card.split(':')[1].split('|')
        
        winners = set([int(c) for c in winners.split()])
        gotten = set([int(c) for c in gotten.split()])
        match_ = winners.intersection(gotten)

        if len(match_) == 1:
            total_points += 1
        elif len(match_) > 1:
            total_points += 2**(len(match_) - 1)
    
    return total_points

def get_num_cards(input):
    
    if isinstance(input, str):
        input = input.split('\n')
    
    cards_to_process = np.array([1]*len(input))
    for idx, card in enumerate(input):
        winners, gotten = card.split(':')[1].split('|')
        
        winners = set([int(c) for c in winners.split()])
        gotten = set([int(c) for c in gotten.split()])
        match_ = winners.intersection(gotten)

        for i in range(1, len(match_) + 1):
            if i < len(cards_to_process):
                cards_to_process[idx + i] += cards_to_process[idx]

    return sum(cards_to_process)

def main(path, challenge):
    with open(path, 'r') as f:
        input = f.readlines()

    if challenge == 1:
        return get_points(input)
    
    elif challenge == 2:
        return get_num_cards(input)

    raise ValueError('Invalid Challenge number selection.')

if __name__=="__main__":
    

    parser = argparse.ArgumentParser(description='Advent of Code 2023. Challenge Day 4.')
    parser.add_argument('challenge',  type=int, default=1, choices=[1, 2], 
                        help='an integer, 1 or 2, to indicate which challenge to execute')
    parser.add_argument('file_path', type=str, required=True,  
                        help="Path to input file. Example: 'data/input_04_12.txt'")

    args = parser.parse_args()
    main(args.file_path, args.challenge)