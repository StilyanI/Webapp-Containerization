document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.event-btn');
    const resultsTable = document.getElementById('results-table').querySelector('tbody');

    buttons.forEach(button => {
        button.addEventListener('click', async () => {
            buttons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');

            try {
                const response = await fetch(`/get_results/${button.dataset.eventId}`);
                const results = await response.json();
                
                resultsTable.innerHTML = results.map(result => `
                    <tr>
                        <td>${result.place}</td>
                        <td>${result.team}</td>
                        <td>${result.participant}</td>
                        <td>${result.result}</td>
                    </tr>
                `).join('');
            } catch (error) {
                console.error('Error fetching results:', error);
            }
        });
    });
});