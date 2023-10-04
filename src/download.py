import pickle
from pathlib import Path

from ucimlrepo import fetch_ucirepo

UCI_WINE_ID = 186


def main():
    data_dir = Path(__file__).parents[1] / 'data'
    data_dir.mkdir(parents=True, exist_ok=True)

    wine_quality = fetch_ucirepo(id=UCI_WINE_ID)

    with open('data/wine_quality.pkl', 'wb') as file:
        pickle.dump(wine_quality, file)


if __name__ == '__main__':
    main()
