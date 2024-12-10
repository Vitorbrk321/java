function calcularCompra(produto, numParcelas) {
    // Verifica se os dados do produto estão corretos
    if (!produto || typeof produto.preco !== "number" || produto.preco <= 0) {
        console.log("Produto inválido ou preço incorreto.");
        return;
    }

    const preco = produto.preco;

    if (numParcelas === 0) {
        // Compra à vista com desconto de 10%
        const valorComDesconto = preco * 0.9;
        console.log(`Compra à vista. Valor com desconto: R$ ${valorComDesconto.toFixed(2)}`);
    } else if (numParcelas >= 1 && numParcelas <= 10) {
        // Parcelamento sem juros
        const valorParcela = preco / numParcelas;
        console.log(`Compra parcelada em ${numParcelas}x sem juros. Cada parcela: R$ ${valorParcela.toFixed(2)}`);
    } else if (numParcelas >= 11 && numParcelas <= 12) {
        // Parcelamento com 2% de juros
        const precoComJuros = preco * 1.02;
        const valorParcela = precoComJuros / numParcelas;
        console.log(`Compra parcelada em ${numParcelas}x com 2% de juros. Cada parcela: R$ ${valorParcela.toFixed(2)}`);
    } else {
        // Número de parcelas não permitido
        console.log("Número de parcelas não permitido.");
    }
}

// Exemplos de chamadas da função
const produto = { nome: "Smartphone", preco: 1500 };

calcularCompra(produto, 0);  // Compra à vista
calcularCompra(produto, 5);  // Parcelado em 5x sem juros
calcularCompra(produto, 11); // Parcelado em 11x com juros
calcularCompra(produto, 13); // Parcelas não permitidas
