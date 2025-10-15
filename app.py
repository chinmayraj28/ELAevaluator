from flask import Flask, render_template, request, jsonify
from base import Formula, Evaluator
import io
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    try:
        data = request.get_json()
        formula_string = data.get('formula', '')
        
        if not formula_string:
            return jsonify({'error': 'Please enter a formula'}), 400
        
        # Create evaluator
        evaluator = Evaluator(startString=formula_string)
        
        # Get variables
        vars_list = evaluator.vars
        
        # Generate truth table data
        truth_table = []
        n = len(vars_list)
        
        for combination in range(pow(2, n)):
            ground_truth = {}
            row = {}
            
            # Set variable values
            for id, var in enumerate(vars_list):
                value = (combination >> id) & 1
                ground_truth[var] = value
                row[var] = value
            
            # Evaluate formula
            try:
                result = evaluator.formula.evaluate(ground_truth)
                row['result'] = result
                truth_table.append(row)
            except Exception as e:
                return jsonify({'error': f'Error evaluating formula: {str(e)}'}), 400
        
        return jsonify({
            'variables': vars_list,
            'truth_table': truth_table,
            'formula': formula_string
        })
    
    except Exception as e:
        return jsonify({'error': f'Invalid formula: {str(e)}'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
