document.addEventListener('DOMContentLoaded', function () {
    const canvas = document.getElementById('graficoTipos');
    if (!canvas) return;

    // Lê os dados do dataset do canvas (não do ctx!)
    const tiposData = JSON.parse(canvas.dataset.tipos);

    const ctx = canvas.getContext('2d');

    const labels = Object.keys(tiposData);
    const dataValues = Object.values(tiposData);

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Quantidade',
                data: dataValues,
                backgroundColor: '#ebb624ff'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false, // permite usar o height do container
            plugins: {
                legend: { display: false },
                title: {
                    display: true,
                    text: 'Distribuição dos 16 Tipos de Pele',
                    color: 'white',
                    font: { size: 16 }
                }
            },
            scales: {
                x: { ticks: { color: 'white' } },
                y: { 
                    ticks: { 
                        color: 'white',
                        precision: 0,      // força valores inteiros
                        stepSize: 1        // incrementa de 1 em 1
                    },
                    beginAtZero: true
                }
            }
        }
    });
});
