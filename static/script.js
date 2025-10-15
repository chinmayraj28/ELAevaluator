async function evaluateFormula() {
    const formulaInput = document.getElementById('formula');
    const formula = formulaInput.value.trim();
    
    const errorDiv = document.getElementById('error');
    const loadingDiv = document.getElementById('loading');
    const resultDiv = document.getElementById('result');
    
    // Hide previous results and errors
    errorDiv.classList.remove('show');
    resultDiv.classList.remove('show');
    
    if (!formula) {
        showError('Please enter a formula');
        return;
    }
    
    // Show loading
    loadingDiv.classList.add('show');
    
    try {
        const response = await fetch('/evaluate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ formula: formula })
        });
        
        const data = await response.json();
        
        loadingDiv.classList.remove('show');
        
        if (!response.ok) {
            showError(data.error || 'An error occurred');
            return;
        }
        
        displayTruthTable(data);
        
    } catch (error) {
        loadingDiv.classList.remove('show');
        showError('Failed to connect to server: ' + error.message);
    }
}

function showError(message) {
    const errorDiv = document.getElementById('error');
    errorDiv.textContent = message;
    errorDiv.classList.add('show');
}

function displayTruthTable(data) {
    const resultDiv = document.getElementById('result');
    const displayFormula = document.getElementById('displayFormula');
    const table = document.getElementById('truthTable');
    
    // Display formula
    displayFormula.textContent = data.formula;
    
    // Clear previous table
    table.innerHTML = '';
    
    // Create table header
    const thead = document.createElement('thead');
    const headerRow = document.createElement('tr');
    
    // Add variable columns
    data.variables.forEach(variable => {
        const th = document.createElement('th');
        th.textContent = variable;
        headerRow.appendChild(th);
    });
    
    // Add result column
    const resultTh = document.createElement('th');
    resultTh.textContent = 'Result';
    headerRow.appendChild(resultTh);
    
    thead.appendChild(headerRow);
    table.appendChild(thead);
    
    // Create table body
    const tbody = document.createElement('tbody');
    
    data.truth_table.forEach(row => {
        const tr = document.createElement('tr');
        
        // Add variable values
        data.variables.forEach(variable => {
            const td = document.createElement('td');
            td.textContent = row[variable];
            tr.appendChild(td);
        });
        
        // Add result value
        const resultTd = document.createElement('td');
        resultTd.textContent = row.result;
        resultTd.classList.add('result-col');
        tr.appendChild(resultTd);
        
        tbody.appendChild(tr);
    });
    
    table.appendChild(tbody);
    
    // Show result section
    resultDiv.classList.add('show');
    
    // Smooth scroll to results
    resultDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

// Allow Enter key to submit
document.getElementById('formula').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        evaluateFormula();
    }
});
