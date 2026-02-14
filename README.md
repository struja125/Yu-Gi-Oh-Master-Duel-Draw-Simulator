# Yu-Gi-Oh! Master Duel Draw Simulator

A Python-based card draw simulator that mimics the gacha/pack opening mechanics of Yu-Gi-Oh! Master Duel with realistic rarity odds.

## Disclaimer

**This is an unofficial, non-commercial fan project.**

This project is not affiliated with, endorsed by, or connected to Konami Digital Entertainment, the Yu-Gi-Oh! franchise, or any of its subsidiaries. Yu-Gi-Oh! and all related names, characters, and imagery are trademarks of Konami Holdings Corporation.

This simulator is created purely for educational and entertainment purposes. No copyright infringement is intended. This project does not include any copyrighted assets such as card images, official artwork, or logos.

## Data Source

Card data is retrieved from the [YGOProDeck API](https://ygoprodeck.com/api-guide/), which provides a free and open database of Yu-Gi-Oh! card information. Please refer to their [terms of service](https://ygoprodeck.com/terms-of-service/) for usage guidelines.

## Features

- Simulates Master Duel pack opening with realistic rarity odds
- Supports all four rarity tiers: UR (Ultra Rare), SR (Super Rare), R (Rare), N (Normal)
- Two draw modes: with duplicates and distinct cards only
- Automatically fetches up-to-date card data from YGOProDeck API

## Rarity Odds

The simulator uses the following approximate pull rates:
- **Ultra Rare (UR)**: 2.5%
- **Super Rare (SR)**: 7.5%
- **Rare (R)**: 35%
- **Normal (N)**: 55%

## Requirements

- Python 3.6 or higher
- `requests` library (for fetching card data)

Install the required library:
```bash
pip install requests
```

## Usage

### Step 1: Fetch Card Database

First, run the database fetcher to download the latest Master Duel card data:

```bash
python FatchCardsFromDB.py
```

This creates `master_duel_cards.txt` containing all Master Duel cards with their rarities.

### Step 2: Draw Cards

**Option A - Random Draw (duplicates allowed):**
```bash
python RandomDraw.py
```
Draws 100 random cards. The same card can appear multiple times.

**Option B - Distinct Draw (no duplicates):**
```bash
python DistinctRandomDraw.py
```
Draws 100 unique cards. Each card can only appear once.

### Step 3: View Results

Both scripts output results to `DrawnCards.txt`, sorted alphabetically.

## File Structure

| File | Description |
|------|-------------|
| `FatchCardsFromDB.py` | Fetches card data from YGOProDeck API |
| `RandomDraw.py` | Draws 100 cards with duplicates allowed |
| `DistinctRandomDraw.py` | Draws 100 unique cards |
| `master_duel_cards.txt` | Local card database (generated) |
| `DrawnCards.txt` | Draw results output (generated) |

## License

MIT License

Copyright (c) 2026 Strahinja Miljković

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## Acknowledgments

- [YGOProDeck](https://ygoprodeck.com/) for providing the card database API
- The Yu-Gi-Oh! community for inspiration
