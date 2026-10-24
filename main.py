from loader import load_data
from anki_builder import build_deck

cards = load_data("data/sample_vocab.csv")
build_deck(cards, "output/magyar.apkg")

