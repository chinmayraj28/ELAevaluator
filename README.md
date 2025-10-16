# ELAevaluator

Elementary Logic Evaluator - A tool to evaluate propositional logic formulas and generate truth tables.

## Features

- Evaluate propositional logic formulas
- Generate complete truth tables
- Web interface for easy interaction
- Support for all standard logical operators

## Supported Operators

- `!` - NOT (Negation)
- `^` - AND (Conjunction)
- `|` - OR (Disjunction)
- `->` - IMPLIES (Implication)
- `<->` - BICONDITIONAL (Equivalence)

## Installation

### Using Conda (Recommended)

```bash
conda env create -f environment.yml
conda activate proplogic
```

### Using pip

**On Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**On Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

### Web Interface (New!)

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser to: `http://localhost:5000`

3. Enter your formula with spaces between operators and variables:
   - Example: `p ^ q`
   - Example: `( p | q ) -> r`
   - Example: `! p <-> q`

4. Click "Generate Truth Table" to see the results!

### Command Line

```bash
python base.py
```

Then enter your formula when prompted. The truth table will be saved to `answers.txt`.

## Formula Syntax

- Use **spaces** between operators and variables
- Use **parentheses** `( )` for grouping expressions
- Variables can be any letters (p, q, r, etc.)

### Examples

- `p ^ q` - p AND q
- `p | q` - p OR q
- `! p` - NOT p
- `p -> q` - p IMPLIES q
- `( p ^ q ) | r` - (p AND q) OR r
- `p <-> q` - p BICONDITIONAL q

## Project Structure

```
├── app.py              # Flask web application
├── base.py             # Core logic evaluation engine
├── requirements.txt    # Python dependencies
├── environment.yml     # Conda environment setup
├── templates/
│   └── index.html     # Web interface HTML
└── static/
    ├── style.css      # Styling
    └── script.js      # Frontend logic
```

## Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Logic Engine**: Custom Python implementation

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is available under the MIT License - see the LICENSE file for details.

## Acknowledgments

Original logic engine created by neosouwchuan at King's College London.

Web interface contributed by chinmayraj28.
