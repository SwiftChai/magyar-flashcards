import genanki

flashcard_model = genanki.Model(
    1386718137,
    'Magyar Flashcard',
    fields=[
        {'name': 'English'},
        {'name': 'Hungarian'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{English}}',
            'afmt': '{{Hungarian}}{{tts hu_HU:Hungarian}}',
        },
    ],
#add css
)


def build_deck(cards, output_path):
    colors_deck = genanki.Deck(
        1624221929,
        'Hungarian Colors')
    for card in cards:
        flashcard_note = genanki.Note(
            model=flashcard_model,
            fields=[card.english, card.hungarian])
        colors_deck.add_note(flashcard_note)

    genanki.Package(colors_deck).write_to_file(output_path)
