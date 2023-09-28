from rick_and_morty_api import RnMApi

import json
import argparse

def main():
    api = RnMApi()

    stats = api.series_info()
    print(f'There is total of {stats["total_episodes"]} of Rick and Morty episodes.', end=' ')
    print(f'First episode came out {stats["first_episode"]}')
    
    search_result = api.find_episode(name=title)
    search_result_pretty = json.dumps(search_result, indent=2)
    print(search_result_pretty)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-t', '--title', 
        default='Pilot', type=str, help='Episode title'
    )

    title = parser.parse_args().title

    main()
